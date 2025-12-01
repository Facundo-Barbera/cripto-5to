from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from analyzer.rfc_validator import RFCValidator

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'domain' not in data:
        return jsonify({'error': 'Domain is required'}), 400

    domain = data['domain'].strip().lower()
    if not domain:
        return jsonify({'error': 'Domain cannot be empty'}), 400

    try:
        validator = RFCValidator()
        result = validator.validate(domain)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
