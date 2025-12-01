# DNSSEC Analysis Report: udlap.mx

**Analysis Date:** 2025-11-29T14:49:02.520139

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** srvudlans02.udlap.mx
- **Responsible Email:** operacion.udlap.mx
- **Serial:** 2006046351
- **Refresh:** 3600s
- **Retry:** 7200s
- **Expire:** 1296000s
- **Minimum TTL:** 21600s
- **Record TTL:** 16188s

## NS Records

Total: 6

- srvudlans02.udlap.mx (TTL: 21600s)
- srvudlans03.udlap.mx (TTL: 21600s)
- ns1-35.azure-dns.com (TTL: 21600s)
- ns4-35.azure-dns.info (TTL: 21600s)
- ns2-35.azure-dns.net (TTL: 21600s)
- ns3-35.azure-dns.org (TTL: 21600s)

## A Records

Total: 2

- 45.60.11.114 (TTL: 17805s)
- 45.60.17.114 (TTL: 17805s)

## MX Records

Total: 1

- udlap-mx.mail.protection.outlook.com (Priority: 0, TTL: 3600s)

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

- **Domain:** udlap.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
udlap.mx
├── srvudlans02.udlap.mx (TTL: 21600s)
├── srvudlans03.udlap.mx (TTL: 21600s)
├── ns1-35.azure-dns.com (TTL: 21600s)
├── ns4-35.azure-dns.info (TTL: 21600s)
├── ns2-35.azure-dns.net (TTL: 21600s)
└── ns3-35.azure-dns.org (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
