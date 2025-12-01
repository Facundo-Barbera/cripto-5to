# DNSSEC Analysis Report: uas.edu.mx

**Analysis Date:** 2025-12-01T10:07:12.599769

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** dns.uas.edu.mx
- **Responsible Email:** please_set_email.absolutely.nowhere
- **Serial:** 444
- **Refresh:** 10800s
- **Retry:** 3600s
- **Expire:** 2419200s
- **Minimum TTL:** 900s
- **Record TTL:** 21600s

## NS Records

Total: 1

- dns.fca.uas.edu.mx (TTL: 21600s)

## A Records

Total: 1

- 148.227.1.12 (TTL: 18949s)

## MX Records

Total: 1

- aspmx.l.google.com (Priority: 10, TTL: 18305s)

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

- **Domain:** uas.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
uas.edu.mx
└── dns.fca.uas.edu.mx (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| uas.edu.mx | No | No | No | Unsigned |
| edu.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `uas.edu.mx`
