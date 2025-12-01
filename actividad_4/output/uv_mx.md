# DNSSEC Analysis Report: uv.mx

**Analysis Date:** 2025-11-29T14:48:55.417367

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

- ns3.uv.mx (TTL: 3600s)
- ns1.uv.mx (TTL: 3600s)
- ns2.uv.mx (TTL: 3600s)

## A Records

Total: 1

- 20.88.208.126 (TTL: 2892s)

## MX Records

Total: 1

- uv-mx.mail.protection.outlook.com (Priority: 0, TTL: 2525s)

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
├── ns3.uv.mx (TTL: 3600s)
├── ns1.uv.mx (TTL: 3600s)
└── ns2.uv.mx (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
