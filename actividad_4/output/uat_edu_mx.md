# DNSSEC Analysis Report: uat.edu.mx

**Analysis Date:** 2025-12-01T10:10:19.569123

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns1-05.azure-dns.com
- **Responsible Email:** administrator.uat.edu.mx
- **Serial:** 294
- **Refresh:** 900s
- **Retry:** 600s
- **Expire:** 86400s
- **Minimum TTL:** 3600s
- **Record TTL:** 3600s

## NS Records

Total: 4

- ns4-05.azure-dns.info (TTL: 2335s)
- ns2-05.azure-dns.net (TTL: 2335s)
- ns1-05.azure-dns.com (TTL: 2335s)
- ns3-05.azure-dns.org (TTL: 2335s)

## MX Records

Total: 1

- uat-edu-mx.mail.protection.outlook.com (Priority: 0, TTL: 1177s)

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

- **Domain:** uat.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
uat.edu.mx
├── ns4-05.azure-dns.info (TTL: 2335s)
├── ns2-05.azure-dns.net (TTL: 2335s)
├── ns1-05.azure-dns.com (TTL: 2335s)
└── ns3-05.azure-dns.org (TTL: 2335s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| uat.edu.mx | No | No | No | Unsigned |
| edu.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `uat.edu.mx`
