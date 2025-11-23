# DNSSEC Analysis Report: unam.mx

**Analysis Date:** 2025-11-23T15:36:55.144212

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** enabled_incomplete
- **Has Signatures:** False
- **Has DS Record:** True
- **NSEC Type:** NSEC

---

## SOA Records

- **Primary Server:** ns1.unam.mx
- **Responsible Email:** dns.unam.mx
- **Serial:** 2025118104
- **Refresh:** 3600s
- **Retry:** 1200s
- **Expire:** 1814400s
- **Minimum TTL:** 300s
- **Record TTL:** 6275s

## NS Records

Total: 5

- ns5.unam.mx (TTL: 6275s)
- ns1.unam.mx (TTL: 6275s)
- ns3.unam.mx (TTL: 6275s)
- ns2.unam.mx (TTL: 6275s)
- ns4.unam.mx (TTL: 6275s)

## A Records

Total: 4

- 132.248.166.20 (TTL: 6275s)
- 132.248.166.18 (TTL: 6275s)
- 132.248.166.17 (TTL: 6275s)
- 132.248.166.19 (TTL: 6275s)

## AAAA Records

Total: 4

- 2001:1218:3000:180::20 (TTL: 6275s)
- 2001:1218:3000:180::17 (TTL: 6275s)
- 2001:1218:3000:180::18 (TTL: 6275s)
- 2001:1218:3000:180::19 (TTL: 6275s)

## MX Records

Total: 1

- unam-mx.mail.protection.outlook.com (Priority: 0, TTL: 6275s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 2
- **TTL:** 6275s

### Key 1

- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Key Size:** 256 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

### Key 2

- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Key Size:** 256 bits
- **Flags:** 257
- **Protocol:** 3
- **Type:** KSK (Key Signing Key)
- **Zone Key:** True

## RRSIG Records

No RRSIG records found.

## DS Records

- **Total DS Records:** 1
- **TTL:** 85475s

### DS Record 1

- **Key Tag:** 54058
- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Digest Type:** SHA-256 (2)
- **Digest:** `ea3eb01183e5bc13acac4692831ea81da9b6d8f402ab3ab4fa1a5c1ef52869e0`

## NSEC/NSEC3 Records

- **Type:** NSEC
- **NSEC Present:** True
- **NSEC3 Present:** False
- **NSEC3PARAM Present:** False
- **Opt-Out:** False

### NSEC Details

- **Count:** 1
- **TTL:** 118s

---

## DNS Tree Structure

- **Domain:** unam.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
unam.mx
├── ns5.unam.mx (TTL: 6275s)
├── ns1.unam.mx (TTL: 6275s)
├── ns3.unam.mx (TTL: 6275s)
├── ns2.unam.mx (TTL: 6275s)
└── ns4.unam.mx (TTL: 6275s)
```

### Cryptographic Chain of Trust

DS record exists in parent zone (mx), establishing cryptographic chain of trust.

```
mx (parent zone)
  └── DS Record → unam.mx
      └── KeyTag: 54058, Algorithm: ECDSA-P256/SHA-256
```
