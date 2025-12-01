# DNSSEC Analysis Report: ucm.mx

**Analysis Date:** 2025-12-01T10:07:21.380461

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns1.ucm.mx
- **Responsible Email:** hostmaster.ucm.mx
- **Serial:** 1746391940
- **Refresh:** 43200s
- **Retry:** 3600s
- **Expire:** 1209600s
- **Minimum TTL:** 10800s
- **Record TTL:** 21600s

## NS Records

Total: 5

- freedns4.registrar-servers.com (TTL: 1800s)
- freedns2.registrar-servers.com (TTL: 1800s)
- freedns1.registrar-servers.com (TTL: 1800s)
- freedns5.registrar-servers.com (TTL: 1800s)
- freedns3.registrar-servers.com (TTL: 1800s)

## A Records

Total: 1

- 187.188.28.51 (TTL: 1799s)

## MX Records

Total: 1

- atenea.ucm.mx (Priority: 10, TTL: 1799s)

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

- **Domain:** ucm.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
ucm.mx
├── freedns4.registrar-servers.com (TTL: 1800s)
├── freedns2.registrar-servers.com (TTL: 1800s)
├── freedns1.registrar-servers.com (TTL: 1800s)
├── freedns5.registrar-servers.com (TTL: 1800s)
└── freedns3.registrar-servers.com (TTL: 1800s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| ucm.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `ucm.mx`
