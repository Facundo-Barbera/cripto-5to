# DNSSEC Analysis Report: gob.mx

**Analysis Date:** 2025-12-07T17:53:25.834922

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** valid
- **Has Signatures:** True
- **Has DS Record:** True
- **NSEC Type:** NSEC3

---

## SOA Records

- **Primary Server:** m.mx-ns.mx
- **Responsible Email:** hostmaster.nic.mx
- **Serial:** 1765127238
- **Refresh:** 900s
- **Retry:** 900s
- **Expire:** 604800s
- **Minimum TTL:** 1800s
- **Record TTL:** 20939s

## NS Records

Total: 6

- m.mx-ns.mx (TTL: 1748s)
- e.mx-ns.mx (TTL: 1748s)
- i.mx-ns.mx (TTL: 1748s)
- c.mx-ns.mx (TTL: 1748s)
- o.mx-ns.mx (TTL: 1748s)
- x.mx-ns.mx (TTL: 1748s)

## A Records

Total: 1

- 207.249.118.158 (TTL: 1216s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 2
- **TTL:** 21600s

### Key 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Size:** 2080 bits
- **Flags:** 257
- **Protocol:** 3
- **Type:** KSK (Key Signing Key)
- **Zone Key:** True

### Key 2

- **Algorithm:** RSA/SHA-256 (8)
- **Key Size:** 1056 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

## RRSIG Records

- **Total Signatures:** 7
- **TTL:** 21097s

### NS Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** gob.mx
- **Labels:** 2
- **Original TTL:** 86400s
- **Inception:** 2025-12-05T18:00:00
- **Expiration:** 2026-01-04T18:00:00
- **Days Until Expiration:** 28
- **Status:** VALID

### A Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** gob.mx
- **Labels:** 2
- **Original TTL:** 3600s
- **Inception:** 2025-12-05T18:00:00
- **Expiration:** 2026-01-04T18:00:00
- **Days Until Expiration:** 28
- **Status:** VALID

### DNSKEY Signatures (2)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 12884
- **Signer:** gob.mx
- **Labels:** 2
- **Original TTL:** 86400s
- **Inception:** 2025-12-02T09:00:00
- **Expiration:** 2026-01-31T09:00:00
- **Days Until Expiration:** 54
- **Status:** VALID

#### Signature 2

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** gob.mx
- **Labels:** 2
- **Original TTL:** 86400s
- **Inception:** 2025-12-05T18:00:00
- **Expiration:** 2026-01-04T18:00:00
- **Days Until Expiration:** 28
- **Status:** VALID

### TXT Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** gob.mx
- **Labels:** 2
- **Original TTL:** 86400s
- **Inception:** 2025-12-05T18:00:00
- **Expiration:** 2026-01-04T18:00:00
- **Days Until Expiration:** 28
- **Status:** VALID

### SOA Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** gob.mx
- **Labels:** 2
- **Original TTL:** 86400s
- **Inception:** 2025-12-06T18:00:00
- **Expiration:** 2026-01-05T18:00:00
- **Days Until Expiration:** 29
- **Status:** VALID

### NSEC3PARAM Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** gob.mx
- **Labels:** 2
- **Original TTL:** 86400s
- **Inception:** 2025-12-05T18:00:00
- **Expiration:** 2026-01-04T18:00:00
- **Days Until Expiration:** 28
- **Status:** VALID

## DS Records

- **Total DS Records:** 1
- **TTL:** 10292s

### DS Record 1

- **Key Tag:** 12884
- **Algorithm:** RSA/SHA-256 (8)
- **Digest Type:** SHA-256 (2)
- **Digest:** `9b78b7939aeced1ee9a65cede1d20bc21f43f908e66ae2636ae0e191554eea47`

## NSEC/NSEC3 Records

- **Type:** NSEC3
- **NSEC Present:** False
- **NSEC3 Present:** True
- **NSEC3PARAM Present:** True
- **Opt-Out:** True

### NSEC3 Details

- **Count:** 3
- **TTL:** 1800s

#### NSEC3 Record 1

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 0
- **Salt:** 86161318ad1a1e2f

#### NSEC3 Record 2

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 0
- **Salt:** 86161318ad1a1e2f

#### NSEC3 Record 3

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 0
- **Salt:** 86161318ad1a1e2f

### NSEC3PARAM Details

- **Count:** 1
- **TTL:** 21542s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 0
- **Salt:** 86161318ad1a1e2f

---

## DNS Tree Structure

- **Domain:** gob.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
gob.mx
├── m.mx-ns.mx (TTL: 1748s)
├── e.mx-ns.mx (TTL: 1748s)
├── i.mx-ns.mx (TTL: 1748s)
├── c.mx-ns.mx (TTL: 1748s)
├── o.mx-ns.mx (TTL: 1748s)
└── x.mx-ns.mx (TTL: 1748s)
```

### Cryptographic Chain of Trust

DS record exists in parent zone (mx), establishing cryptographic chain of trust.

```
mx (parent zone)
  └── DS Record → gob.mx
      └── KeyTag: 12884, Algorithm: RSA/SHA-256
```

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| gob.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Complete - Full trust path to root
