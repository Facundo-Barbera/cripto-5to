# DNSSEC Analyzer - Improvements TODO

## Priority: Required Features for Final Delivery

### Feature A: Batch Domain Analysis (Required - 50 domains)

Implement batch scanning system with pre-loaded .mx domains.

#### Backend

- [ ] Create `/api/analyze/batch` endpoint that accepts array of domains
- [ ] Add progress tracking for batch operations
- [ ] Return aggregated results with summary statistics
- [ ] Create `domains_mx.txt` with 50 .mx domains (prioritize DNSSEC-enabled)

#### Frontend

- [ ] Add "Batch Mode" toggle/tab in UI
- [ ] Textarea input for multiple domains (one per line)
- [ ] "Load Default 50" button to populate with .mx domains
- [ ] Progress indicator during batch scan
- [ ] Results table with sortable columns (domain, DNSSEC status, score)
- [ ] Export results to CSV/JSON

#### Research: Find 50 .mx domains

- [ ] Mexican government domains (.gob.mx) - likely have DNSSEC
- [ ] Mexican universities (.edu.mx)
- [ ] Mexican banks and financial institutions
- [ ] Large Mexican companies
- [ ] NIC Mexico (nic.mx) - registry, definitely has DNSSEC

---

### Feature B: AI-Powered Recommendations (Gemini Integration)

Add LLM-generated recommendations based on scan results.

#### Backend

- [ ] Create `/api/recommendations` endpoint
- [ ] Integrate Gemini API (google-generativeai package)
- [ ] Build prompt template with scan results context
- [ ] Support `mode` parameter: `executive` | `technical`
- [ ] Handle API errors gracefully (rate limits, unavailable)
- [ ] Cache recommendations to avoid redundant API calls

#### Frontend

- [ ] Add "Recommendations" section in results (collapsed by default)
- [ ] Toggle switch: "Executive Summary" / "Technical Details"
- [ ] Loading state while waiting for LLM response
- [ ] Markdown rendering for LLM output
- [ ] Error state if LLM unavailable

#### Prompt Design

- [ ] Executive mode: Business impact, risk level, action items for management
- [ ] Technical mode: Specific DNS records to add, configuration steps, RFC references

---

## Priority: Bug Fixes

### Fix: URL Input Sanitization

Currently `https://unam.mx` breaks the chain analysis.

- [ ] Strip protocol (`http://`, `https://`)
- [ ] Strip `www.` prefix (optional, configurable)
- [ ] Strip trailing slashes and paths (`/page/something`)
- [ ] Validate resulting domain format
- [ ] Show user the "cleaned" domain being analyzed

**Location:** `app.py` and/or `analyzer/generator.py`

---

## Phase 1: Domain Status Detection

Add pre-flight checks to detect domain status before running DNSSEC analysis.

### Backend (`analyzer/generator.py`)

- [ ] Create `check_domain_status()` method that returns domain state
- [ ] Detect `NXDOMAIN` - domain does not exist
- [ ] Detect `SERVFAIL` - DNS server failure
- [ ] Detect `Timeout` - DNS server not responding
- [ ] Detect missing NS records - domain registered but not configured
- [ ] Detect missing A/AAAA records - domain exists but no address
- [ ] Add `domain_status` field to analysis response

### Frontend (`static/js/app.js`)

- [ ] Handle `domain_status` in API response
- [ ] Show appropriate error/info message based on status
- [ ] Don't render DNSSEC chain if domain doesn't exist

---

## Phase 2: Additional DNS Security Analysis (Optional)

Make the tool useful even for domains without DNSSEC.

### Email Authentication Records

- [ ] **SPF** - Query TXT records, parse SPF policy
- [ ] **DKIM** - Check for common DKIM selectors
- [ ] **DMARC** - Query `_dmarc.domain` TXT record

### Certificate Authority Authorization

- [ ] **CAA Records** - Query CAA, show which CAs can issue certs

### UI for New Features

- [ ] Add new section "Email Security" in results
- [ ] Add new section "Certificate Policy" in results
- [ ] Add i18n translations for new sections

---

## Phase 3: DNS Infrastructure Analysis (Optional)

- [ ] NS diversity check (different networks/ASNs)
- [ ] IPv6 support (AAAA records presence)
- [ ] TTL analysis (appropriate values)
- [ ] DNS provider detection

---

## Notes

- **Feature A & B are required** for final delivery
- **Bug fix** (URL sanitization) should be done first - quick win
- Phase 1 is essential - currently the app silently fails on invalid domains
- Phase 2 adds value for the ~70% of domains without DNSSEC
- Phase 3 is nice-to-have for comprehensive DNS analysis

## .mx Domains to Research

Known DNSSEC-enabled .mx domains:
- `nic.mx` - Mexican domain registry (definitely has DNSSEC)
- `gob.mx` - Government portal
- `sat.gob.mx` - Tax authority

Need to verify and find ~47 more...
