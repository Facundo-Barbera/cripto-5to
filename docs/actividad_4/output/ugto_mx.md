# DNSSEC Analysis Report: ugto.mx

**Analysis Date:** 2025-12-01T10:07:01.388548

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns3.ugto.mx
- **Responsible Email:** soporte.ugto.mx
- **Serial:** 2025102210
- **Refresh:** 3600s
- **Retry:** 600s
- **Expire:** 604800s
- **Minimum TTL:** 3600s
- **Record TTL:** 3600s

## NS Records

Total: 2

- nic2.ugto.mx (TTL: 3600s)
- ns3.ugto.mx (TTL: 3600s)

## A Records

Total: 1

- 148.214.50.10 (TTL: 3600s)

## MX Records

Total: 1

- ugto-mx.mail.protection.outlook.com (Priority: 0, TTL: 1369s)

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

- **Domain:** ugto.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
ugto.mx
├── nic2.ugto.mx (TTL: 3600s)
└── ns3.ugto.mx (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| ugto.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `ugto.mx`
