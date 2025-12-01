import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from http.server import BaseHTTPRequestHandler
import json

# Default 50 Mexican domains for batch analysis
DEFAULT_DOMAINS = [
    # Registry and DNS infrastructure
    "nic.mx",
    # Government (.gob.mx)
    "gob.mx",
    "sat.gob.mx",
    "imss.gob.mx",
    "sep.gob.mx",
    "segob.gob.mx",
    "sre.gob.mx",
    "banxico.gob.mx",
    "inegi.gob.mx",
    "conacyt.gob.mx",
    "shcp.gob.mx",
    "salud.gob.mx",
    "economia.gob.mx",
    "cfe.gob.mx",
    "pemex.gob.mx",
    # Universities and Education (.edu.mx)
    "unam.mx",
    "ipn.mx",
    "itesm.mx",
    "uag.mx",
    "uanl.mx",
    "udg.mx",
    "buap.mx",
    "uaemex.mx",
    "uabc.mx",
    "uach.mx",
    # Financial Institutions
    "bbva.mx",
    "banorte.com.mx",
    "santander.com.mx",
    "hsbc.com.mx",
    "citibanamex.com.mx",
    "scotiabank.com.mx",
    # Major Companies and Corporations
    "telmex.com.mx",
    "telcel.com",
    "televisa.com.mx",
    "tv-azteca.com.mx",
    "liverpool.com.mx",
    "cemex.com.mx",
    "bimbo.com.mx",
    "femsa.com.mx",
    "elektra.com.mx",
    "walmart.com.mx",
    "coppel.com.mx",
    "oxxo.com.mx",
    # Media and News
    "eluniversal.com.mx",
    "reforma.com.mx",
    "milenio.com",
    # Technology and Services
    "mercadolibre.com.mx",
    "amazon.com.mx",
]


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self._send_json(200, {
            'domains': DEFAULT_DOMAINS,
            'count': len(DEFAULT_DOMAINS)
        })

    def _send_json(self, status: int, data: dict):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
