# DNSSEC-Analyzer

A school project to analyze and validate DNSSEC configurations for domain names, focused on `.mx` (México) domains.

## What it does

- Checks if a domain has DNSSEC enabled
- Validates the chain of trust (DS, DNSKEY, RRSIG records)
- Provides a web interface to view results
- Includes CLI tools for batch analysis and RFC validation

## Tech Stack

- Python / Flask
- dnspython for DNS queries

## Running the Web Interface

The web frontend should be accessed via:

### Vercel (Recommended for Production)

Hosted on [Vercel](https://vercel.com) as a serverless application:
- API endpoints run as Python serverless functions (`/api/*`)
- Static frontend served from `/static`

### Docker (Recommended for Local Development)

Run the full web application locally with Docker Compose (includes hot-reload):

```bash
docker compose up
```

App will be available at `http://localhost:5050`

## Running CLI Tools Locally

For local command-line analysis, use the CLI tools in the `analyzer/` directory.

### Prerequisites

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

### DNSSEC Batch Analyzer

Analyze multiple domains from a file and generate detailed reports:

```bash
python analyzer/generator.py <domains_file.txt> [output_directory]
```

- `<domains_file.txt>` - Required: Path to a text file containing domains (one per line)
- `[output_directory]` - Optional: Directory for output reports (default: `dnssec_reports`)

Example:
```bash
python analyzer/generator.py domains_mx.txt dnssec_reports
```

### RFC Validator

Validate a single domain against DNSSEC RFC compliance:

```bash
python analyzer/rfc_validator.py <domain>
```

- `<domain>` - Required: Domain name to validate

Example:
```bash
python analyzer/rfc_validator.py unam.mx
```

This will generate a detailed compliance report and save it as `{domain}_rfc_validation.json`.

## Credits

- Alberto Boughton Reyes (A01178500)
- Valeria Garcia Hernandez (A01742811)
- Facundo Bautista Barbera (A01066843)
- Emiliano Ruiz López (A01659693)
- Daniel Garnelo Martinez (A00573086)
