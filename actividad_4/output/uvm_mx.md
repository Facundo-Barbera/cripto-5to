# DNSSEC Analysis Report: uvm.mx

**Analysis Date:** 2025-11-29T14:49:17.440266

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** enabled_incomplete
- **Has Signatures:** False
- **Has DS Record:** True
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** margot.ns.cloudflare.com
- **Responsible Email:** dns.cloudflare.com
- **Serial:** 2389784702
- **Refresh:** 10000s
- **Retry:** 2400s
- **Expire:** 604800s
- **Minimum TTL:** 1800s
- **Record TTL:** 1800s

## NS Records

Total: 2

- margot.ns.cloudflare.com (TTL: 86400s)
- thaddeus.ns.cloudflare.com (TTL: 86400s)

## A Records

Total: 2

- 104.18.35.78 (TTL: 161s)
- 172.64.152.178 (TTL: 161s)

## AAAA Records

Total: 2

- 2606:4700:4402::ac40:98b2 (TTL: 300s)
- 2606:4700:4401::6812:234e (TTL: 300s)

## MX Records

Total: 5

- aspmx.l.google.com (Priority: 1, TTL: 300s)
- aspmx2.googlemail.com (Priority: 10, TTL: 300s)
- aspmx3.googlemail.com (Priority: 10, TTL: 300s)
- alt1.aspmx.l.google.com (Priority: 5, TTL: 300s)
- alt2.aspmx.l.google.com (Priority: 5, TTL: 300s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 2
- **TTL:** 3600s

### Key 1

- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Key Size:** 256 bits
- **Flags:** 257
- **Protocol:** 3
- **Type:** KSK (Key Signing Key)
- **Zone Key:** True

### Key 2

- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Key Size:** 256 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

## RRSIG Records

No RRSIG records found.

## DS Records

- **Total DS Records:** 1
- **TTL:** 17584s

### DS Record 1

- **Key Tag:** 2371
- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Digest Type:** SHA-256 (2)
- **Digest:** `de795a37e8d3fe5e50cbe2864de1ea2d5056490ec3e26d4923b720142138fb39`

## NSEC/NSEC3 Records

- **Type:** NONE
- **NSEC Present:** False
- **NSEC3 Present:** False
- **NSEC3PARAM Present:** False
- **Opt-Out:** False

---

## DNS Tree Structure

- **Domain:** uvm.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
uvm.mx
├── margot.ns.cloudflare.com (TTL: 86400s)
└── thaddeus.ns.cloudflare.com (TTL: 86400s)
```

### Cryptographic Chain of Trust

DS record exists in parent zone (mx), establishing cryptographic chain of trust.

```
mx (parent zone)
  └── DS Record → uvm.mx
      └── KeyTag: 2371, Algorithm: ECDSA-P256/SHA-256
```
