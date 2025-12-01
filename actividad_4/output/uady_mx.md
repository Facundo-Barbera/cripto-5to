# DNSSEC Analysis Report: uady.mx

**Analysis Date:** 2025-12-01T10:07:31.008274

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** tunku.uady.mx
- **Responsible Email:** soporte.tunku.uady.mx
- **Serial:** 2025120101
- **Refresh:** 3600s
- **Retry:** 1200s
- **Expire:** 1814400s
- **Minimum TTL:** 7200s
- **Record TTL:** 21600s

## NS Records

Total: 3

- kuklincloud.uady.mx (TTL: 20161s)
- dziu.uady.mx (TTL: 20161s)
- tunku.uady.mx (TTL: 20161s)

## A Records

Total: 1

- 20.169.251.95 (TTL: 18331s)

## MX Records

Total: 2

- mail.uady.mx (Priority: 0, TTL: 7728s)
- mail2.uady.mx (Priority: 5, TTL: 7728s)

---

# DNSSEC Records

## DNSKEY Records

No DNSKEY records found.

## RRSIG Records

No RRSIG records found.

## DS Records

No DS records found in parent zone.

## NSEC/NSEC3 Records

- **Type:** NONE
- **NSEC Present:** False
- **NSEC3 Present:** False
- **NSEC3PARAM Present:** False
- **Opt-Out:** False

---

## DNS Tree Structure

- **Domain:** uady.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
uady.mx
├── kuklincloud.uady.mx (TTL: 20161s)
├── dziu.uady.mx (TTL: 20161s)
└── tunku.uady.mx (TTL: 20161s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| uady.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `uady.mx`
