# DNSSEC Analysis Report: uaemex.mx

**Analysis Date:** 2025-11-29T14:49:40.833764

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns1-06.azure-dns.com
- **Responsible Email:** azuredns-hostmaster.microsoft.com
- **Serial:** 1
- **Refresh:** 3600s
- **Retry:** 300s
- **Expire:** 2419200s
- **Minimum TTL:** 300s
- **Record TTL:** 3600s

## NS Records

Total: 4

- ns4-06.azure-dns.info (TTL: 172800s)
- ns1-06.azure-dns.com (TTL: 172800s)
- ns2-06.azure-dns.net (TTL: 172800s)
- ns3-06.azure-dns.org (TTL: 172800s)

## A Records

Total: 1

- 148.215.154.13 (TTL: 230s)

## MX Records

Total: 1

- uaemex-mx.mail.protection.outlook.com (Priority: 0, TTL: 87s)

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

- **Domain:** uaemex.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
uaemex.mx
├── ns4-06.azure-dns.info (TTL: 172800s)
├── ns1-06.azure-dns.com (TTL: 172800s)
├── ns2-06.azure-dns.net (TTL: 172800s)
└── ns3-06.azure-dns.org (TTL: 172800s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
