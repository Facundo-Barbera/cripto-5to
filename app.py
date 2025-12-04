from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from analyzer.rfc_validator import RFCValidator
from analyzer.generator import sanitize_domain, DNSSECAnalyzer
from analyzer.llm_advisor import LLMAdvisor
import uuid
import threading
import time
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# In-memory storage for batch jobs
batch_jobs = {}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/presentation')
def presentation():
    return render_template('presentation.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'domain' not in data:
        return jsonify({'error': 'Domain is required'}), 400

    original_input = data['domain'].strip()
    domain = sanitize_domain(original_input)

    if not domain:
        return jsonify({'error': 'Domain cannot be empty'}), 400

    try:
        # Pre-flight domain status check
        analyzer = DNSSECAnalyzer()
        domain_status = analyzer.check_domain_status(domain)

        # If domain can't be analyzed, return status info
        if not domain_status['can_analyze']:
            response = {
                'domain': domain,
                'domain_status': domain_status,
                'error': domain_status['message']
            }
            if original_input.lower() != domain:
                response['sanitized_from'] = original_input
            return jsonify(response), 400

        validator = RFCValidator()
        result = validator.validate(domain)

        # Add domain status to response
        result['domain_status'] = domain_status

        # Add sanitization info to response
        if original_input.lower() != domain:
            result['sanitized_from'] = original_input
            result['domain'] = domain

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def run_batch_analysis(job_id, domains):
    """Background task to run batch analysis"""
    job = batch_jobs[job_id]
    analyzer = DNSSECAnalyzer(delay_seconds=0.5)
    validator = RFCValidator()

    for i, domain in enumerate(domains):
        if job['status'] == 'cancelled':
            break

        clean_domain = sanitize_domain(domain)
        if not clean_domain:
            job['results'].append({
                'domain': domain,
                'status': 'error',
                'error': 'Invalid domain',
                'dnssec_enabled': False,
                'chain_complete': False,
                'rfc_score': 0,
                'rfc_total': 0,
                'rfc_percentage': 0
            })
            job['completed'] += 1
            continue

        try:
            # Check domain status first
            domain_status = analyzer.check_domain_status(clean_domain)

            if not domain_status['can_analyze']:
                job['results'].append({
                    'domain': clean_domain,
                    'status': 'error',
                    'error': domain_status['message'],
                    'domain_status': domain_status['status'],
                    'dnssec_enabled': False,
                    'chain_complete': False,
                    'rfc_score': 0,
                    'rfc_total': 0,
                    'rfc_percentage': 0
                })
            else:
                result = validator.validate(clean_domain)
                dnssec_summary = result.get('analysis', {}).get('dnssec', {}).get('summary', {})
                rfc_compliance = result.get('rfc_compliance', {})

                job['results'].append({
                    'domain': clean_domain,
                    'status': 'success',
                    'error': None,
                    'dnssec_enabled': dnssec_summary.get('dnssec_enabled', False),
                    'chain_complete': dnssec_summary.get('chain_complete', False),
                    'rfc_score': rfc_compliance.get('passed', 0),
                    'rfc_total': rfc_compliance.get('total', 0),
                    'rfc_percentage': rfc_compliance.get('percentage', 0)
                })

        except Exception as e:
            job['results'].append({
                'domain': clean_domain,
                'status': 'error',
                'error': str(e),
                'dnssec_enabled': False,
                'chain_complete': False,
                'rfc_score': 0,
                'rfc_total': 0,
                'rfc_percentage': 0
            })

        job['completed'] += 1
        time.sleep(0.1)  # Small delay between domains

    # Calculate summary
    results = job['results']
    job['summary'] = {
        'dnssec_enabled_count': sum(1 for r in results if r.get('dnssec_enabled')),
        'dnssec_disabled_count': sum(1 for r in results if not r.get('dnssec_enabled')),
        'chain_complete_count': sum(1 for r in results if r.get('chain_complete')),
        'errors_count': sum(1 for r in results if r.get('status') == 'error'),
        'average_rfc_score': sum(r.get('rfc_percentage', 0) for r in results) / len(results) if results else 0
    }
    job['status'] = 'completed'


@app.route('/api/analyze/batch', methods=['POST'])
def start_batch_analysis():
    """Start a new batch analysis job"""
    data = request.get_json()

    if not data or 'domains' not in data:
        return jsonify({'error': 'Domains array is required'}), 400

    domains = data['domains']
    if not isinstance(domains, list) or len(domains) == 0:
        return jsonify({'error': 'Domains must be a non-empty array'}), 400

    # Limit to 100 domains max
    if len(domains) > 100:
        return jsonify({'error': 'Maximum 100 domains allowed per batch'}), 400

    job_id = str(uuid.uuid4())
    batch_jobs[job_id] = {
        'id': job_id,
        'status': 'running',
        'total': len(domains),
        'completed': 0,
        'results': [],
        'summary': None,
        'started_at': datetime.now().isoformat()
    }

    # Start background thread
    thread = threading.Thread(target=run_batch_analysis, args=(job_id, domains))
    thread.daemon = True
    thread.start()

    return jsonify({
        'job_id': job_id,
        'status': 'running',
        'total': len(domains)
    })


@app.route('/api/analyze/batch/<job_id>', methods=['GET'])
def get_batch_status(job_id):
    """Get status and results of a batch job"""
    if job_id not in batch_jobs:
        return jsonify({'error': 'Job not found'}), 404

    job = batch_jobs[job_id]
    return jsonify({
        'job_id': job['id'],
        'status': job['status'],
        'total': job['total'],
        'completed': job['completed'],
        'progress': (job['completed'] / job['total'] * 100) if job['total'] > 0 else 0,
        'results': job['results'],
        'summary': job['summary'],
        'started_at': job['started_at']
    })


@app.route('/api/domains/default', methods=['GET'])
def get_default_domains():
    """Get the default list of .mx domains"""
    try:
        domains_file = os.path.join(os.path.dirname(__file__), 'domains_mx.txt')
        with open(domains_file, 'r') as f:
            domains = [
                line.strip() for line in f
                if line.strip() and not line.strip().startswith('#')
            ]
        return jsonify({'domains': domains})
    except FileNotFoundError:
        return jsonify({'error': 'Default domains file not found'}), 404


@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    """Generate AI-powered recommendations based on analysis results"""
    data = request.get_json()

    if not data or 'analysis' not in data:
        return jsonify({'error': 'Analysis data is required'}), 400

    mode = data.get('mode', 'executive')
    if mode not in ['executive', 'technical']:
        return jsonify({'error': 'Mode must be "executive" or "technical"'}), 400

    analysis = data['analysis']

    try:
        advisor = LLMAdvisor()
        recommendations = advisor.get_recommendations(analysis, mode)
        return jsonify({
            'domain': analysis.get('domain', 'unknown'),
            'mode': mode,
            'recommendations': recommendations
        })
    except ValueError as e:
        # API key not configured
        return jsonify({'error': 'AI recommendations not available. API key not configured.'}), 503
    except RuntimeError as e:
        # LLM generation failed
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': f'Failed to generate recommendations: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
