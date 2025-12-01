# DNSSEC Analysis Report: ulsab.edu.mx

**Analysis Date:** 2025-12-01T10:11:22.544983

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** dns1.akkyhosting26.mx
- **Responsible Email:** cops.nic.mx
- **Serial:** 2025110302
- **Refresh:** 3600s
- **Retry:** 1800s
- **Expire:** 1209600s
- **Minimum TTL:** 86400s
- **Record TTL:** 21600s

## NS Records

Total: 4

- dns4.akkyhosting26.mx (TTL: 21600s)
- dns2.akkyhosting26.mx (TTL: 21600s)
- dns3.akkyhosting26.mx (TTL: 21600s)
- dns1.akkyhosting26.mx (TTL: 21600s)

## A Records

Total: 1

- 170.10.162.192 (TTL: 14400s)

## MX Records

Total: 6

- ALT3.ASPMX.L.GOOGLE.COM (Priority: 10, TTL: 14400s)
- ASPMX.L.GOOGLE.COM (Priority: 1, TTL: 14400s)
- smtp.GOOGLE.COM (Priority: 1, TTL: 14400s)
- ALT2.ASPMX.L.GOOGLE.COM (Priority: 5, TTL: 14400s)
- ALT1.ASPMX.L.GOOGLE.COM (Priority: 5, TTL: 14400s)
- ALT4.ASPMX.L.GOOGLE.COM (Priority: 10, TTL: 14400s)

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

- **Domain:** ulsab.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
ulsab.edu.mx
├── dns4.akkyhosting26.mx (TTL: 21600s)
├── dns2.akkyhosting26.mx (TTL: 21600s)
├── dns3.akkyhosting26.mx (TTL: 21600s)
└── dns1.akkyhosting26.mx (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (edu.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| ulsab.edu.mx | No | No | No | Unsigned |
| edu.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `ulsab.edu.mx`
