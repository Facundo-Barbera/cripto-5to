# DNSSEC Analysis Report: unison.mx

**Analysis Date:** 2025-12-01T10:06:56.422044

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** dns1.uson.mx
- **Responsible Email:** redes.unison.mx
- **Serial:** 2017653758
- **Refresh:** 10200s
- **Retry:** 3600s
- **Expire:** 1814400s
- **Minimum TTL:** 900s
- **Record TTL:** 3600s

## NS Records

Total: 3

- dns1.uson.mx (TTL: 3600s)
- sancarlos.noc.uson.mx (TTL: 3600s)
- dc1.unison.mx (TTL: 3600s)

## A Records

Total: 4

- 148.225.105.195 (TTL: 600s)
- 148.225.105.2 (TTL: 600s)
- 148.225.105.32 (TTL: 600s)
- 148.225.105.194 (TTL: 600s)

## MX Records

Total: 1

- unison-mx.mail.protection.outlook.com (Priority: 0, TTL: 3600s)

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

- **Domain:** unison.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
unison.mx
├── dns1.uson.mx (TTL: 3600s)
├── sancarlos.noc.uson.mx (TTL: 3600s)
└── dc1.unison.mx (TTL: 3600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| unison.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `unison.mx`
