# DNSSEC Analysis Report: udlc.edu.mx

**Analysis Date:** 2025-12-01T10:11:11.075508

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** rs13a.registrar-servers.com
- **Responsible Email:** cpanel.tech.namecheap.com
- **Serial:** 2025062500
- **Refresh:** 86400s
- **Retry:** 7200s
- **Expire:** 3600000s
- **Minimum TTL:** 86400s
- **Record TTL:** 21600s

## NS Records

Total: 2

- rs13a.registrar-servers.com (TTL: 21600s)
- rs13b.registrar-servers.com (TTL: 21600s)

## A Records

Total: 1

- 198.54.126.51 (TTL: 1200s)

## MX Records

Total: 3

- mx1-hosting.jellyfish.systems (Priority: 10, TTL: 1200s)
- mx2-hosting.jellyfish.systems (Priority: 20, TTL: 1200s)
- mx3-hosting.jellyfish.systems (Priority: 30, TTL: 1200s)

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

- **Domain:** udlc.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
udlc.edu.mx
├── rs13a.registrar-servers.com (TTL: 21600s)
└── rs13b.registrar-servers.com (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| udlc.edu.mx | No | No | No | Unsigned |
| edu.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `udlc.edu.mx`
