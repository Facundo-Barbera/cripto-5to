# DNSSEC Analysis Report: ipn.mx

**Analysis Date:** 2025-11-29T14:48:41.638108

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** enabled_incomplete
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** NSEC3

---

## SOA Records

- **Primary Server:** dns3.ipn.mx
- **Responsible Email:** tic.ipn.mx
- **Serial:** 2025112804
- **Refresh:** 10800s
- **Retry:** 1800s
- **Expire:** 1209600s
- **Minimum TTL:** 10800s
- **Record TTL:** 3600s

## NS Records

Total: 3

- dns1.ipn.mx (TTL: 1800s)
- dns2.ipn.mx (TTL: 1800s)
- dns3.ipn.mx (TTL: 1800s)

## A Records

Total: 1

- 20.64.80.120 (TTL: 2469s)

## MX Records

Total: 1

- ipn-mx.mail.protection.outlook.com (Priority: 0, TTL: 3600s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 2
- **TTL:** 86400s

### Key 1

- **Algorithm:** RSA/SHA-512 (10)
- **Key Size:** 2080 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

### Key 2

- **Algorithm:** RSA/SHA-512 (10)
- **Key Size:** 2080 bits
- **Flags:** 257
- **Protocol:** 3
- **Type:** KSK (Key Signing Key)
- **Zone Key:** True

## RRSIG Records

No RRSIG records found.

## DS Records

No DS records found in parent zone.

## NSEC/NSEC3 Records

- **Type:** NSEC3
- **NSEC Present:** False
- **NSEC3 Present:** True
- **NSEC3PARAM Present:** True
- **Opt-Out:** False

### NSEC3 Details

- **Count:** 0
- **TTL:** Nones

### NSEC3PARAM Details

- **Count:** 1
- **TTL:** 3600s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 1
- **Salt:** adabc49b1f947ef5

---

## DNS Tree Structure

- **Domain:** ipn.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
ipn.mx
├── dns1.ipn.mx (TTL: 1800s)
├── dns2.ipn.mx (TTL: 1800s)
└── dns3.ipn.mx (TTL: 1800s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
