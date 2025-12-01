# DNSSEC Analysis Report: uat.edu.mx

**Analysis Date:** 2025-11-29T14:49:34.216968

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns1-06.azure-dns.com
- **Responsible Email:** administrator.uat.edu.mx
- **Serial:** 2004136045
- **Refresh:** 900s
- **Retry:** 600s
- **Expire:** 86400s
- **Minimum TTL:** 3600s
- **Record TTL:** 3600s

## NS Records

Total: 4

- ns4-06.azure-dns.info (TTL: 9694s)
- ns3-06.azure-dns.org (TTL: 9694s)
- ns1-06.azure-dns.com (TTL: 9694s)
- ns2-06.azure-dns.net (TTL: 9694s)

## MX Records

Total: 1

- uat-edu-mx.mail.protection.outlook.com (Priority: 0, TTL: 1118s)

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

- **Domain:** uat.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
uat.edu.mx
├── ns4-06.azure-dns.info (TTL: 9694s)
├── ns3-06.azure-dns.org (TTL: 9694s)
├── ns1-06.azure-dns.com (TTL: 9694s)
└── ns2-06.azure-dns.net (TTL: 9694s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.
