# DNSSEC Analysis Report: uic.mx

**Analysis Date:** 2025-11-29T14:49:15.579579

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** uicsistmg.uic.edu.mx
- **Responsible Email:** hostmaster.uic.edu.mx
- **Serial:** 412
- **Refresh:** 900s
- **Retry:** 600s
- **Expire:** 86400s
- **Minimum TTL:** 3600s
- **Record TTL:** 3600s

## NS Records

Total: 2

- uicsistmg.uic.edu.mx (TTL: 3600s)
- mail.uic.mx (TTL: 3600s)

## A Records

Total: 1

- 23.92.208.70 (TTL: 3600s)

## MX Records

Total: 1

- correo.uic.mx (Priority: 10, TTL: 3600s)

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

- **Domain:** uic.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
uic.mx
├── uicsistmg.uic.edu.mx (TTL: 3600s)
└── mail.uic.mx (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
