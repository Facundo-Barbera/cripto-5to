# DNSSEC Analysis Report: uaq.mx

**Analysis Date:** 2025-11-29T14:49:00.781447

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns1.uaq.mx
- **Responsible Email:** dns.uaq.mx
- **Serial:** 2025060514
- **Refresh:** 3600s
- **Retry:** 60s
- **Expire:** 604800s
- **Minimum TTL:** 1800s
- **Record TTL:** 21600s

## NS Records

Total: 2

- ns1.uaq.mx (TTL: 21600s)
- ns2.uaq.mx (TTL: 21600s)

## MX Records

Total: 1

- uaq-mx.mail.protection.outlook.com (Priority: 0, TTL: 3509s)

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

- **Domain:** uaq.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
uaq.mx
├── ns1.uaq.mx (TTL: 21600s)
└── ns2.uaq.mx (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
