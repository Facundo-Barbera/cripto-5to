# DNSSEC Analyzer - Improvements TODO

## Priority: Required Features for Final Delivery

### Feature A: Batch Domain Analysis (Required - 50 domains)

Implement batch scanning system with pre-loaded .mx domains.

#### Backend

- [x] Create `/api/analyze/batch` endpoint that accepts array of domains
- [x] Add progress tracking for batch operations
- [x] Return aggregated results with summary statistics
- [x] Create `domains_mx.txt` with 50 .mx domains (prioritize DNSSEC-enabled)

#### Frontend

- [x] Add "Batch Mode" toggle/tab in UI
- [x] Textarea input for multiple domains (one per line)
- [x] "Load Default 50" button to populate with .mx domains
- [x] Progress indicator during batch scan
- [x] Results table with sortable columns (domain, DNSSEC status, score)
- [x] Export results to CSV/JSON

#### Research: Find 50 .mx domains

- [x] Mexican government domains (.gob.mx) - likely have DNSSEC
- [x] Mexican universities (.edu.mx)
- [x] Mexican banks and financial institutions
- [x] Large Mexican companies
- [x] NIC Mexico (nic.mx) - registry, definitely has DNSSEC

---

### Feature B: AI-Powered Recommendations (Gemini Integration)

Add LLM-generated recommendations based on scan results.

#### Backend

- [x] Create `/api/recommendations` endpoint
- [x] Integrate Gemini API (REST API)
- [x] Build prompt template with scan results context
- [x] Support `mode` parameter: `executive` | `technical`
- [x] Handle API errors gracefully (rate limits, unavailable)
- [x] Cache recommendations to avoid redundant API calls

#### Frontend

- [x] Add "Recommendations" section in results (collapsed by default)
- [x] Toggle switch: "Executive Summary" / "Technical Details"
- [x] Loading state while waiting for LLM response
- [x] Markdown rendering for LLM output
- [x] Error state if LLM unavailable

#### Prompt Design

- [x] Executive mode: Business impact, risk level, action items for management
- [x] Technical mode: Specific DNS records to add, configuration steps, RFC references

---

## Priority: Bug Fixes

### Fix: URL Input Sanitization

Currently `https://unam.mx` breaks the chain analysis.

- [x] Strip protocol (`http://`, `https://`)
- [x] Strip `www.` prefix (optional, configurable)
- [x] Strip trailing slashes and paths (`/page/something`)
- [x] Validate resulting domain format
- [x] Show user the "cleaned" domain being analyzed

**Location:** `app.py` and `analyzer/generator.py`

---

## Phase 1: Domain Status Detection

Add pre-flight checks to detect domain status before running DNSSEC analysis.

### Backend (`analyzer/generator.py`)

- [x] Create `check_domain_status()` method that returns domain state
- [x] Detect `NXDOMAIN` - domain does not exist
- [x] Detect `SERVFAIL` - DNS server failure
- [x] Detect `Timeout` - DNS server not responding
- [x] Detect missing NS records - domain registered but not configured
- [x] Detect missing A/AAAA records - domain exists but no address
- [x] Add `domain_status` field to analysis response

### Frontend (`public/js/app.js`)

- [x] Handle `domain_status` in API response
- [x] Show appropriate error/info message based on status
- [x] Don't render DNSSEC chain if domain doesn't exist

---

## Phase 2: Additional DNS Security Analysis

Make the tool useful even for domains without DNSSEC.

### Email Authentication Records

- [x] **SPF** - Query TXT records, parse SPF policy
- [x] **DKIM** - Check for common DKIM selectors
- [x] **DMARC** - Query `_dmarc.domain` TXT record

### Certificate Authority Authorization

- [x] **CAA Records** - Query CAA, show which CAs can issue certs

### UI for New Features

- [x] Add new section "Email Security" in results
- [x] Add new section "Certificate Policy" (CAA) in results
- [x] Add i18n translations for new sections

---

## Phase 3: DNS Infrastructure Analysis

- [x] NS diversity check (different networks/providers)
- [x] IPv6 support (AAAA records presence)
- [x] TTL analysis (appropriate values)
- [x] DNS provider detection

---

## Notes

- **Feature A & B are required** for final delivery - COMPLETE
- **Bug fix** (URL sanitization) - COMPLETE
- **Phase 1** (Domain status detection) - COMPLETE
- **Phase 2** (Email security: SPF, DKIM, DMARC, CAA) - COMPLETE
- **Phase 3** (DNS infrastructure analysis) - COMPLETE

## .mx Domains

File `domains_mx.txt` contains 50 domains organized by category:
- Registry (nic.mx)
- Government (.gob.mx)
- Universities (.edu.mx)
- Financial institutions
- Large companies
- Media
- Tech companies
