import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._send_error(400, 'Invalid JSON')
            return

        if not data or 'analysis' not in data:
            self._send_error(400, 'Analysis data is required')
            return

        analysis = data['analysis']
        mode = data.get('mode', 'executive')
        language = data.get('language', 'en')

        if mode not in ('executive', 'technical'):
            self._send_error(400, 'Mode must be "executive" or "technical"')
            return

        if language not in ('en', 'es'):
            language = 'en'

        # Check for API key
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self._send_error(503, 'AI recommendations not available - API key not configured')
            return

        try:
            from analyzer.llm_advisor import LLMAdvisor
            advisor = LLMAdvisor(api_key=api_key)
            recommendations = advisor.get_recommendations(analysis, mode=mode, language=language)
            self._send_json(200, {
                'recommendations': recommendations,
                'mode': mode,
                'language': language
            })
        except ImportError as e:
            self._send_error(503, f'AI recommendations module not available: {str(e)}')
        except Exception as e:
            self._send_error(500, f'Failed to generate recommendations: {str(e)}')

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
