# DNSSEC Analysis Report: unach.mx

**Analysis Date:** 2025-12-01T10:10:32.955999

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** dns.unach.mx
- **Responsible Email:** root.dns.unach.mx
- **Serial:** 2025101001
- **Refresh:** 3600s
- **Retry:** 3600s
- **Expire:** 604800s
- **Minimum TTL:** 3600s
- **Record TTL:** 3600s

## NS Records

Total: 2

- dns2.unach.mx (TTL: 3600s)
- dns.unach.mx (TTL: 3600s)

## A Records

Total: 1

- 35.209.142.91 (TTL: 300s)

## MX Records

Total: 5

- ALT3.ASPMX.L.GOOGLE.COM (Priority: 10, TTL: 2580s)
- ASPMX.L.GOOGLE.COM (Priority: 1, TTL: 2580s)
- ALT1.ASPMX.L.GOOGLE.COM (Priority: 5, TTL: 2580s)
- ALT4.ASPMX.L.GOOGLE.COM (Priority: 10, TTL: 2580s)
- ALT2.ASPMX.L.GOOGLE.COM (Priority: 5, TTL: 2580s)

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

- **Domain:** unach.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
unach.mx
├── dns2.unach.mx (TTL: 3600s)
└── dns.unach.mx (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| unach.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `unach.mx`
