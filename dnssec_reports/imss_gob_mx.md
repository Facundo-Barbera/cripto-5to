# DNSSEC Analysis Report: imss.gob.mx

**Analysis Date:** 2025-12-07T17:53:31.878983

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** ns204.a0.incapsecuredns.net
- **Responsible Email:** postmaster.imss.gob.mx
- **Serial:** 2009043642
- **Refresh:** 3600s
- **Retry:** 600s
- **Expire:** 1209600s
- **Minimum TTL:** 3600s
- **Record TTL:** 3122s

## NS Records

Total: 3

- ns204.a0.incapsecuredns.net (TTL: 784s)
- ns142.a1.incapsecuredns.net (TTL: 784s)
- ns212.a2.incapsecuredns.net (TTL: 784s)

## A Records

Total: 2

- 45.223.17.206 (TTL: 651s)
- 45.223.23.206 (TTL: 651s)

## MX Records

Total: 1

- mail2.imss.gob.mx (Priority: 10, TTL: 1399s)

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

- **Domain:** imss.gob.mx
- **Parent Zone:** gob.mx
- **Level:** 3

### Nameserver Hierarchy

```
imss.gob.mx
├── ns204.a0.incapsecuredns.net (TTL: 784s)
├── ns142.a1.incapsecuredns.net (TTL: 784s)
└── ns212.a2.incapsecuredns.net (TTL: 784s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (gob.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| imss.gob.mx | No | No | No | Unsigned |
| gob.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | No | Unsigned |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `imss.gob.mx`
