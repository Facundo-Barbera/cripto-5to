# DNSSEC Analysis Report: buap.mx

**Analysis Date:** 2025-12-01T10:06:47.486304

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** dns1.buap.mx
- **Responsible Email:** please_set_email.absolutely.nowhere
- **Serial:** 3794
- **Refresh:** 10800s
- **Retry:** 3600s
- **Expire:** 2419200s
- **Minimum TTL:** 900s
- **Record TTL:** 21600s

## NS Records

Total: 2

- eco.buap.mx (TTL: 21600s)
- dns1.buap.mx (TTL: 21600s)

## A Records

Total: 2

- 45.60.86.125 (TTL: 90s)
- 45.60.113.125 (TTL: 90s)

## MX Records

Total: 2

- d35d9d16f40e054b9d3ebf71042431.mail.outlook.com (Priority: 5, TTL: 3600s)
- buap-mx.mail.protection.outlook.com (Priority: 0, TTL: 3600s)

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

- **Domain:** buap.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
buap.mx
├── eco.buap.mx (TTL: 21600s)
└── dns1.buap.mx (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| buap.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `buap.mx`
