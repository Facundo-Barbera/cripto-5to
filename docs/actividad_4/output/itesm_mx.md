# DNSSEC Analysis Report: itesm.mx

**Analysis Date:** 2025-12-01T10:06:45.364928

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
- **Serial:** 132
- **Refresh:** 10800s
- **Retry:** 3600s
- **Expire:** 2419200s
- **Minimum TTL:** 900s
- **Record TTL:** 3053s

## NS Records

Total: 2

- ns2e.itesm.mx (TTL: 830s)
- ns1e.itesm.mx (TTL: 830s)

## MX Records

Total: 1

- itesm-mx.mail.protection.outlook.com (Priority: 0, TTL: 2541s)

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

- **Domain:** itesm.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
itesm.mx
├── ns2e.itesm.mx (TTL: 830s)
└── ns1e.itesm.mx (TTL: 830s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| itesm.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `itesm.mx`
