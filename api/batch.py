import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from http.server import BaseHTTPRequestHandler
import json
from analyzer.rfc_validator import RFCValidator
from analyzer.generator import sanitize_domain, DNSSECAnalyzer


class handler(BaseHTTPRequestHandler):
    """
    Batch analysis endpoint for Vercel.

    Since Vercel is stateless, this processes a single domain at a time.
    The frontend calls this endpoint for each domain sequentially.

    POST /api/batch
    Body: { "domain": "example.com" }

    Returns the analysis result for the single domain.
    """

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._send_error(400, 'Invalid JSON')
            return

        if not data or 'domain' not in data:
            self._send_error(400, 'Domain is required')
            return

        # Sanitize the domain input
        raw_domain = data['domain']
        domain = sanitize_domain(raw_domain)

        if not domain:
            self._send_error(400, 'Domain cannot be empty')
            return

        try:
            # Check domain status first
            analyzer = DNSSECAnalyzer(timeout=8)
            status = analyzer.check_domain_status(domain)

            if not status.get('can_analyze', False):
                # Return error status for domains that can't be analyzed
                self._send_json(200, {
                    'domain': domain,
                    'original_input': raw_domain if raw_domain != domain else None,
                    'status': status.get('status', 'ERROR'),
                    'error': status.get('message', 'Cannot analyze domain'),
                    'dnssec_enabled': False,
                    'chain_complete': False,
                    'rfc_score': '0/0',
                    'rfc_percentage': 0
                })
                return

            # Perform full analysis
            validator = RFCValidator()
            result = validator.validate(domain)

            # Extract summary data for batch results
            analysis = result.get('analysis', {})
            dnssec = analysis.get('dnssec', {})
            summary = dnssec.get('summary', {})
            rfc_compliance = result.get('rfc_compliance', {})

            self._send_json(200, {
                'domain': domain,
                'original_input': raw_domain if raw_domain != domain else None,
                'status': 'OK',
                'dnssec_enabled': summary.get('dnssec_enabled', False),
                'chain_complete': summary.get('chain_complete', False),
                'rfc_score': rfc_compliance.get('score', '0/0'),
                'rfc_percentage': rfc_compliance.get('percentage', 0),
                'full_result': result  # Include full result for detailed view
            })

        except Exception as e:
            self._send_json(200, {
                'domain': domain,
                'original_input': raw_domain if raw_domain != domain else None,
                'status': 'ERROR',
                'error': str(e),
                'dnssec_enabled': False,
                'chain_complete': False,
                'rfc_score': '0/0',
                'rfc_percentage': 0
            })

    def _send_json(self, status: int, data: dict):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def _send_error(self, status: int, message: str):
        self._send_json(status, {'error': message})

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
