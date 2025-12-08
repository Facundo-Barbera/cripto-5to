# DNSSEC Analysis Report: sat.gob.mx

**Analysis Date:** 2025-12-07T17:53:28.358361

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** huitzilopochtli.sat.gob.mx
- **Responsible Email:** seguridad.sat.gob.mx
- **Serial:** 2030100501
- **Refresh:** 300s
- **Retry:** 300s
- **Expire:** 300s
- **Minimum TTL:** 300s
- **Record TTL:** 300s

## NS Records

Total: 6

- tlahuizcalpantecuhtli.sat.gob.mx (TTL: 188s)
- quetzalcoatl.sat.gob.mx (TTL: 188s)
- ns2.sat.gob.mx (TTL: 188s)
- huitzilopochtli.sat.gob.mx (TTL: 188s)
- xolotl.sat.gob.mx (TTL: 188s)
- tochtli.sat.gob.mx (TTL: 188s)

## A Records

Total: 4

- 3.162.112.83 (TTL: 288s)
- 3.162.112.52 (TTL: 288s)
- 3.162.112.61 (TTL: 288s)
- 3.162.112.21 (TTL: 288s)

## MX Records

Total: 2

- mx1.sat.gob.mx (Priority: 0, TTL: 300s)
- mx.sat.gob.mx (Priority: 5, TTL: 300s)

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

- **Domain:** sat.gob.mx
- **Parent Zone:** gob.mx
- **Level:** 3

### Nameserver Hierarchy

```
sat.gob.mx
├── tlahuizcalpantecuhtli.sat.gob.mx (TTL: 188s)
├── quetzalcoatl.sat.gob.mx (TTL: 188s)
├── ns2.sat.gob.mx (TTL: 188s)
├── huitzilopochtli.sat.gob.mx (TTL: 188s)
├── xolotl.sat.gob.mx (TTL: 188s)
└── tochtli.sat.gob.mx (TTL: 188s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (gob.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| sat.gob.mx | No | No | No | Unsigned |
| gob.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `sat.gob.mx`
