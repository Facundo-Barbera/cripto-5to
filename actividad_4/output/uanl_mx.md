# DNSSEC Analysis Report: uanl.mx

**Analysis Date:** 2025-11-29T14:48:45.265270

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** uanldns.dsi.uanl.mx
- **Responsible Email:** hostmaster.uanl.mx
- **Serial:** 2025052758
- **Refresh:** 10800s
- **Retry:** 3600s
- **Expire:** 1209600s
- **Minimum TTL:** 86400s
- **Record TTL:** 2400s

## NS Records

Total: 2

- dns2.uanl.mx (TTL: 2400s)
- uanldns.dsi.uanl.mx (TTL: 2400s)

## A Records

Total: 1

- 148.234.5.222 (TTL: 176s)

## MX Records

Total: 4

- mx04.hornetsecurity.com (Priority: 13, TTL: 2400s)
- mx03.hornetsecurity.com (Priority: 12, TTL: 2400s)
- mx02.hornetsecurity.com (Priority: 11, TTL: 2400s)
- mx01.hornetsecurity.com (Priority: 10, TTL: 2400s)

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

- **Domain:** uanl.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
uanl.mx
├── dns2.uanl.mx (TTL: 2400s)
└── uanldns.dsi.uanl.mx (TTL: 2400s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
