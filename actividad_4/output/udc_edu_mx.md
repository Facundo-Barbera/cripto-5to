# DNSSEC Analysis Report: udc.edu.mx

**Analysis Date:** 2025-11-29T14:49:22.852463

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns47.domaincontrol.com
- **Responsible Email:** dns.jomax.net
- **Serial:** 2024082100
- **Refresh:** 28800s
- **Retry:** 7200s
- **Expire:** 604800s
- **Minimum TTL:** 600s
- **Record TTL:** 600s

## NS Records

Total: 2

- ns47.domaincontrol.com (TTL: 3600s)
- ns48.domaincontrol.com (TTL: 3600s)

## A Records

Total: 1

- 200.77.221.3 (TTL: 3600s)

## MX Records

Total: 5

- alt4.aspmx.l.google.com (Priority: 10, TTL: 3600s)
- alt3.aspmx.l.google.com (Priority: 10, TTL: 3600s)
- aspmx.l.google.com (Priority: 1, TTL: 3600s)
- alt1.aspmx.l.google.com (Priority: 5, TTL: 3600s)
- alt2.aspmx.l.google.com (Priority: 5, TTL: 3600s)

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

- **Domain:** udc.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
udc.edu.mx
├── ns47.domaincontrol.com (TTL: 3600s)
└── ns48.domaincontrol.com (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.
