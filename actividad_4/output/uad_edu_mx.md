# DNSSEC Analysis Report: uad.edu.mx

**Analysis Date:** 2025-12-01T10:10:14.522337

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## A Records

Total: 1

- 189.197.190.212 (TTL: 3600s)

## MX Records

Total: 5

- aspmx2.googlemail.com\032 (Priority: 10, TTL: 3600s)
- aspmx.l.google.com (Priority: 1, TTL: 3600s)
- alt1.aspmx.l.google.com\032 (Priority: 10, TTL: 3600s)
- aspmx3.googlemail.com\032\032 (Priority: 10, TTL: 3600s)
- alt2.aspmx.l.google.com (Priority: 10, TTL: 3600s)

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

- **Domain:** uad.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| uad.edu.mx | No | No | No | Unsigned |
| edu.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `uad.edu.mx`
