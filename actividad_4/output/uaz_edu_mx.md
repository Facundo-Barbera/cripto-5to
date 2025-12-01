# DNSSEC Analysis Report: uaz.edu.mx

**Analysis Date:** 2025-12-01T10:10:35.204516

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** win-bas6e8tuskt
- **Responsible Email:** hostmaster
- **Serial:** 2111
- **Refresh:** 900s
- **Retry:** 600s
- **Expire:** 86400s
- **Minimum TTL:** 3600s
- **Record TTL:** 3600s

## NS Records

Total: 1

- win-bas6e8tuskt (TTL: 3600s)

## A Records

Total: 1

- 148.217.18.6 (TTL: 780s)

## MX Records

Total: 5

- alt4.aspmx.l.google.com (Priority: 10, TTL: 3600s)
- al2.aspmx.l.google.com (Priority: 5, TTL: 3600s)
- aspmx.l.google.com (Priority: 1, TTL: 3600s)
- alt1.aspmx.l.google.com (Priority: 5, TTL: 3600s)
- alt3.aspmx.l.google.com (Priority: 10, TTL: 3600s)

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

- **Domain:** uaz.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
uaz.edu.mx
└── win-bas6e8tuskt (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| uaz.edu.mx | No | No | No | Unsigned |
| edu.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `uaz.edu.mx`
