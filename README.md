# DNSSEC-Analyzer

A school project to analyze and validate DNSSEC configurations for domain names, focused on `.mx` (México) domains.

## What it does

- Checks if a domain has DNSSEC enabled
- Validates the chain of trust (DS, DNSKEY, RRSIG records)
- Provides a web interface to view results

## Quick Start

```bash
pip install -r requirements.txt
python app.py
```

## Tech Stack

- Python / Flask
- dnspython for DNS queries

## Deployment

Hosted on [Vercel](https://vercel.com) as a serverless application:
- API endpoints run as Python serverless functions (`/api/*`)
- Static frontend served from `/static`

### Docker

Run locally with Docker Compose (includes hot-reload):

```bash
docker compose up
```

App will be available at `http://localhost:5050`

## Credits

- Alberto Boughton Reyes (A01178500)
- Valeria Garcia Hernandez (A01742811)
- Facundo Bautista Barbera (A01066843)
- Emiliano Ruiz López (A01659693)
- Daniel Garnelo Martinez (A00573086)
