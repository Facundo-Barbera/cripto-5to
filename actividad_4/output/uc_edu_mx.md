# DNSSEC Analysis Report: uc.edu.mx

**Analysis Date:** 2025-11-29T14:50:07.591583

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns1.hostpapa.com
- **Responsible Email:** admin.hostpapa.ca
- **Serial:** 2025112802
- **Refresh:** 3600s
- **Retry:** 3600s
- **Expire:** 1209600s
- **Minimum TTL:** 10800s
- **Record TTL:** 21600s

## NS Records

Total: 2

- ns1.hostpapa.com (TTL: 21600s)
- ns2.hostpapa.com (TTL: 21600s)

## A Records

Total: 1

- 172.96.180.55 (TTL: 6751s)

## MX Records

Total: 1

- SMTP.GOOGLE.COM (Priority: 0, TTL: 14400s)

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

- **Domain:** uc.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
uc.edu.mx
├── ns1.hostpapa.com (TTL: 21600s)
└── ns2.hostpapa.com (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.
