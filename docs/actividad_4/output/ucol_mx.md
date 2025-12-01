# DNSSEC Analysis Report: ucol.mx

**Analysis Date:** 2025-12-01T10:07:19.094028

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** volcan.ucol.mx
- **Responsible Email:** postmaster.ucol.mx
- **Serial:** 2025112801
- **Refresh:** 604800s
- **Retry:** 86400s
- **Expire:** 2419200s
- **Minimum TTL:** 604800s
- **Record TTL:** 21600s

## NS Records

Total: 2

- orion.ucol.mx (TTL: 21600s)
- volcan.ucol.mx (TTL: 21600s)

## MX Records

Total: 5

- ASPMX3.GOOGLEMAIL.COM (Priority: 30, TTL: 4419s)
- ALT2.ASPMX.L.GOOGLE.COM (Priority: 20, TTL: 4419s)
- ASPMX2.GOOGLEMAIL.COM (Priority: 30, TTL: 4419s)
- ALT1.ASPMX.L.GOOGLE.COM (Priority: 20, TTL: 4419s)
- ASPMX.L.GOOGLE.COM (Priority: 10, TTL: 4419s)

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

- **Domain:** ucol.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
ucol.mx
├── orion.ucol.mx (TTL: 21600s)
└── volcan.ucol.mx (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| ucol.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `ucol.mx`
