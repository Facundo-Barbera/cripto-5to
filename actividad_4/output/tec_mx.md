# DNSSEC Analysis Report: tec.mx

**Analysis Date:** 2025-11-29T14:48:38.014764

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
- **Serial:** 154
- **Refresh:** 10800s
- **Retry:** 3600s
- **Expire:** 2419200s
- **Minimum TTL:** 900s
- **Record TTL:** 3600s

## NS Records

Total: 2

- ns1e.itesm.mx (TTL: 3600s)
- ns2e.itesm.mx (TTL: 3600s)

## A Records

Total: 2

- 45.60.86.212 (TTL: 841s)
- 45.60.115.212 (TTL: 841s)

## MX Records

Total: 1

- tec-mx.mail.protection.outlook.com (Priority: 0, TTL: 3458s)

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

- **Domain:** tec.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
tec.mx
├── ns1e.itesm.mx (TTL: 3600s)
└── ns2e.itesm.mx (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
