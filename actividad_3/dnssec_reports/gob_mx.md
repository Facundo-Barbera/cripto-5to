# DNSSEC Analysis Report: gob.mx

**Analysis Date:** 2025-11-23T15:36:58.350229

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** enabled_incomplete
- **Has Signatures:** False
- **Has DS Record:** True
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** m.mx-ns.mx
- **Responsible Email:** hostmaster.nic.mx
- **Serial:** 1763924645
- **Refresh:** 900s
- **Retry:** 900s
- **Expire:** 604800s
- **Minimum TTL:** 1800s
- **Record TTL:** 86218s

## NS Records

Total: 6

- c.mx-ns.mx (TTL: 86218s)
- e.mx-ns.mx (TTL: 86218s)
- i.mx-ns.mx (TTL: 86218s)
- m.mx-ns.mx (TTL: 86218s)
- o.mx-ns.mx (TTL: 86218s)
- x.mx-ns.mx (TTL: 86218s)

## A Records

Total: 1

- 207.249.118.158 (TTL: 1610s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 2
- **TTL:** 86218s

### Key 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Size:** 1056 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

### Key 2

- **Algorithm:** RSA/SHA-256 (8)
- **Key Size:** 2080 bits
- **Flags:** 257
- **Protocol:** 3
- **Type:** KSK (Key Signing Key)
- **Zone Key:** True

## RRSIG Records

No RRSIG records found.

## DS Records

- **Total DS Records:** 1
- **TTL:** 86218s

### DS Record 1

- **Key Tag:** 12884
- **Algorithm:** RSA/SHA-256 (8)
- **Digest Type:** SHA-256 (2)
- **Digest:** `9b78b7939aeced1ee9a65cede1d20bc21f43f908e66ae2636ae0e191554eea47`

## NSEC/NSEC3 Records

- **Type:** NONE
- **NSEC Present:** False
- **NSEC3 Present:** False
- **NSEC3PARAM Present:** True
- **Opt-Out:** False

### NSEC3PARAM Details

- **Count:** 1
- **TTL:** 86219s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 0
- **Salt:** c53e9a024dea76c4

---

## DNS Tree Structure

- **Domain:** gob.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
gob.mx
├── c.mx-ns.mx (TTL: 86218s)
├── e.mx-ns.mx (TTL: 86218s)
├── i.mx-ns.mx (TTL: 86218s)
├── m.mx-ns.mx (TTL: 86218s)
├── o.mx-ns.mx (TTL: 86218s)
└── x.mx-ns.mx (TTL: 86218s)
```

### Cryptographic Chain of Trust

DS record exists in parent zone (mx), establishing cryptographic chain of trust.

```
mx (parent zone)
  └── DS Record → gob.mx
      └── KeyTag: 12884, Algorithm: RSA/SHA-256
```
