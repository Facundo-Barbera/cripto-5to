# DNSSEC Analysis Report: uv.mx

**Analysis Date:** 2025-12-01T10:06:58.995726

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns2.uv.mx
- **Responsible Email:** root.ns2.uv.mx
- **Serial:** 2025112601
- **Refresh:** 7200s
- **Retry:** 3600s
- **Expire:** 1209600s
- **Minimum TTL:** 43200s
- **Record TTL:** 3600s

## NS Records

Total: 3

- ns1.uv.mx (TTL: 3600s)
- ns2.uv.mx (TTL: 3600s)
- ns3.uv.mx (TTL: 3600s)

## A Records

Total: 1

- 20.88.208.126 (TTL: 1994s)

## MX Records

Total: 1

- uv-mx.mail.protection.outlook.com (Priority: 0, TTL: 2162s)

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

- **Domain:** uv.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
uv.mx
├── ns1.uv.mx (TTL: 3600s)
├── ns2.uv.mx (TTL: 3600s)
└── ns3.uv.mx (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| uv.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `uv.mx`
