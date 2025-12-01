# DNSSEC Analysis Report: utm.edu.mx

**Analysis Date:** 2025-12-01T10:11:08.580509

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns1e.itesm.mx
- **Responsible Email:** please_set_email.absolutely.nowhere
- **Serial:** 35
- **Refresh:** 10800s
- **Retry:** 3600s
- **Expire:** 2419200s
- **Minimum TTL:** 900s
- **Record TTL:** 3600s

## NS Records

Total: 2

- ns2e.itesm.mx (TTL: 3600s)
- ns1e.itesm.mx (TTL: 3600s)

## MX Records

Total: 2

- 1340699817.mail.exchangelabs.com (Priority: 0, TTL: 3600s)
- utm-edu-mx.mail.protection.outlook.com (Priority: 0, TTL: 3600s)

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

- **Domain:** utm.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
utm.edu.mx
├── ns2e.itesm.mx (TTL: 3600s)
└── ns1e.itesm.mx (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| utm.edu.mx | No | No | No | Unsigned |
| edu.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `utm.edu.mx`
