# DNSSEC Analysis Report: mx.

**Analysis Date:** 2025-12-07T17:53:20.027040

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
- **Serial:** 1765151350
- **Refresh:** 900s
- **Retry:** 900s
- **Expire:** 604800s
- **Minimum TTL:** 1800s
- **Record TTL:** 21600s

## NS Records

Total: 6

- e.mx-ns.mx (TTL: 21600s)
- x.mx-ns.mx (TTL: 21600s)
- o.mx-ns.mx (TTL: 21600s)
- m.mx-ns.mx (TTL: 21600s)
- i.mx-ns.mx (TTL: 21600s)
- c.mx-ns.mx (TTL: 21600s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 2
- **TTL:** 5953s

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

- **Total Signatures:** 6
- **TTL:** 21543s

### DNSKEY Signatures (2)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 12884
- **Signer:** mx
- **Labels:** 1
- **Original TTL:** 86400s
- **Inception:** 2025-12-02T09:00:00
- **Expiration:** 2026-01-31T09:00:00
- **Days Until Expiration:** 54
- **Status:** VALID

#### Signature 2

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** mx
- **Labels:** 1
- **Original TTL:** 86400s
- **Inception:** 2025-12-05T18:00:00
- **Expiration:** 2026-01-04T18:00:00
- **Days Until Expiration:** 28
- **Status:** VALID

### SOA Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** mx
- **Labels:** 1
- **Original TTL:** 86400s
- **Inception:** 2025-12-06T18:00:00
- **Expiration:** 2026-01-05T18:00:00
- **Days Until Expiration:** 29
- **Status:** VALID

### TXT Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** mx
- **Labels:** 1
- **Original TTL:** 86400s
- **Inception:** 2025-12-05T18:00:00
- **Expiration:** 2026-01-04T18:00:00
- **Days Until Expiration:** 28
- **Status:** VALID

### NSEC3PARAM Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** mx
- **Labels:** 1
- **Original TTL:** 86400s
- **Inception:** 2025-12-05T18:00:00
- **Expiration:** 2026-01-04T18:00:00
- **Days Until Expiration:** 28
- **Status:** VALID

### NS Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 43480
- **Signer:** mx
- **Labels:** 1
- **Original TTL:** 86400s
- **Inception:** 2025-12-05T18:00:00
- **Expiration:** 2026-01-04T18:00:00
- **Days Until Expiration:** 28
- **Status:** VALID

## DS Records

- **Total DS Records:** 1
- **TTL:** 82454s

### DS Record 1

- **Key Tag:** 12884
- **Algorithm:** RSA/SHA-256 (8)
- **Digest Type:** SHA-256 (2)
- **Digest:** `250b2b75df2df867e7b8e362c52ee6e994d8aa0e4f850dd8bb94099daef2461d`

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
- **TTL:** 21600s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 0
- **Salt:** 86161318ad1a1e2f

---

## DNS Tree Structure

- **Domain:** mx.
- **Parent Zone:** 
- **Level:** 2

### Nameserver Hierarchy

```
mx.
├── e.mx-ns.mx (TTL: 21600s)
├── x.mx-ns.mx (TTL: 21600s)
├── o.mx-ns.mx (TTL: 21600s)
├── m.mx-ns.mx (TTL: 21600s)
├── i.mx-ns.mx (TTL: 21600s)
└── c.mx-ns.mx (TTL: 21600s)
```

### Cryptographic Chain of Trust

DS record exists in parent zone (), establishing cryptographic chain of trust.

```
 (parent zone)
  └── DS Record → mx.
      └── KeyTag: 12884, Algorithm: RSA/SHA-256
```

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Complete - Full trust path to root
