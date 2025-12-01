# DNSSEC Analysis Report: umm.edu.mx

**Analysis Date:** 2025-12-01T10:07:14.776451

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** lee.ns.cloudflare.com
- **Responsible Email:** dns.cloudflare.com
- **Serial:** 2388099016
- **Refresh:** 10000s
- **Retry:** 2400s
- **Expire:** 604800s
- **Minimum TTL:** 1800s
- **Record TTL:** 1800s

## NS Records

Total: 2

- tess.ns.cloudflare.com (TTL: 21600s)
- lee.ns.cloudflare.com (TTL: 21600s)

## A Records

Total: 2

- 172.66.154.95 (TTL: 300s)
- 104.20.40.233 (TTL: 300s)

## AAAA Records

Total: 2

- 2606:4700:10::6814:28e9 (TTL: 300s)
- 2606:4700:10::ac42:9a5f (TTL: 300s)

## MX Records

Total: 1

- umm-edu-mx.mail.protection.outlook.com (Priority: 0, TTL: 300s)

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

- **Domain:** umm.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
umm.edu.mx
├── tess.ns.cloudflare.com (TTL: 21600s)
└── lee.ns.cloudflare.com (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| umm.edu.mx | No | No | No | Unsigned |
| edu.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `umm.edu.mx`
