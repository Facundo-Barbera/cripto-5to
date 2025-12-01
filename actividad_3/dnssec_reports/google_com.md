# DNSSEC Analysis Report: google.com

**Analysis Date:** 2025-11-27T10:54:27.861860

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns1.google.com
- **Responsible Email:** dns-admin.google.com
- **Serial:** 837044723
- **Refresh:** 900s
- **Retry:** 900s
- **Expire:** 1800s
- **Minimum TTL:** 60s
- **Record TTL:** 15s

## NS Records

Total: 4

- ns4.google.com (TTL: 21600s)
- ns2.google.com (TTL: 21600s)
- ns1.google.com (TTL: 21600s)
- ns3.google.com (TTL: 21600s)

## A Records

Total: 1

- 192.178.57.46 (TTL: 183s)

## AAAA Records

Total: 1

- 2607:f8b0:4012:82a::200e (TTL: 300s)

## MX Records

Total: 1

- smtp.google.com (Priority: 10, TTL: 292s)

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

- **Domain:** google.com
- **Parent Zone:** com
- **Level:** 2

### Nameserver Hierarchy

```
google.com
├── ns4.google.com (TTL: 21600s)
├── ns2.google.com (TTL: 21600s)
├── ns1.google.com (TTL: 21600s)
└── ns3.google.com (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (com). Chain of trust not established.
