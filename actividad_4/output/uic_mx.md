# DNSSEC Analysis Report: uic.mx

**Analysis Date:** 2025-12-01T10:07:24.151500

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** uicsistmg.uic.edu.mx
- **Responsible Email:** hostmaster.uic.edu.mx
- **Serial:** 412
- **Refresh:** 900s
- **Retry:** 600s
- **Expire:** 86400s
- **Minimum TTL:** 3600s
- **Record TTL:** 3600s

## NS Records

Total: 2

- mail.uic.mx (TTL: 3600s)
- uicsistmg.uic.edu.mx (TTL: 3600s)

## A Records

Total: 1

- 23.92.208.70 (TTL: 1759s)

## MX Records

Total: 1

- correo.uic.mx (Priority: 10, TTL: 3600s)

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

- **Domain:** uic.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
uic.mx
├── mail.uic.mx (TTL: 3600s)
└── uicsistmg.uic.edu.mx (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| uic.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `uic.mx`
