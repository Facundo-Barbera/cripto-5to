# DNSSEC Analysis Report: upchiapas.edu.mx

**Analysis Date:** 2025-12-01T10:10:11.459805

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** valid
- **Has Signatures:** True
- **Has DS Record:** True
- **NSEC Type:** NSEC3

---

## SOA Records

- **Primary Server:** ns1.akkyservicios.mx
- **Responsible Email:** hostmaster.akkyservicios.mx.upchiapas.edu.mx
- **Serial:** 1764360295
- **Refresh:** 3600s
- **Retry:** 900s
- **Expire:** 604800s
- **Minimum TTL:** 1800s
- **Record TTL:** 21600s

## NS Records

Total: 3

- ns1.akkyservicios.mx (TTL: 21600s)
- ns2.akkyservicios.mx (TTL: 21600s)
- ns3.akkyservicios.mx (TTL: 21600s)

## A Records

Total: 1

- 20.237.247.210 (TTL: 3600s)

## MX Records

Total: 7

- alt4.aspmx.l.google.com (Priority: 10, TTL: 3600s)
- alt1.aspmx.l.google.com (Priority: 5, TTL: 3600s)
- aspmx3.googlemail.com (Priority: 10, TTL: 3600s)
- aspmx2.googlemail.com (Priority: 10, TTL: 3600s)
- alt2.aspmx.l.google.com (Priority: 5, TTL: 3600s)
- aspmx.l.google.com (Priority: 1, TTL: 3600s)
- alt3.aspmx.l.google.com (Priority: 10, TTL: 3600s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 2
- **TTL:** 3600s

### Key 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Size:** 2080 bits
- **Flags:** 257
- **Protocol:** 3
- **Type:** KSK (Key Signing Key)
- **Zone Key:** True

### Key 2

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Size:** 1056 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

## RRSIG Records

- **Total Signatures:** 8
- **TTL:** 0s

### NSEC3PARAM Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 23312
- **Signer:** upchiapas.edu.mx
- **Labels:** 3
- **Original TTL:** 0s
- **Inception:** 2025-11-28T13:04:55
- **Expiration:** 2025-12-28T14:04:55
- **Days Until Expiration:** 27
- **Status:** VALID

### DNSKEY Signatures (2)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 41013
- **Signer:** upchiapas.edu.mx
- **Labels:** 3
- **Original TTL:** 3600s
- **Inception:** 2025-11-28T13:04:55
- **Expiration:** 2025-12-28T14:04:55
- **Days Until Expiration:** 27
- **Status:** VALID

#### Signature 2

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 23312
- **Signer:** upchiapas.edu.mx
- **Labels:** 3
- **Original TTL:** 3600s
- **Inception:** 2025-11-28T13:04:55
- **Expiration:** 2025-12-28T14:04:55
- **Days Until Expiration:** 27
- **Status:** VALID

### SOA Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 23312
- **Signer:** upchiapas.edu.mx
- **Labels:** 3
- **Original TTL:** 172800s
- **Inception:** 2025-11-28T13:04:55
- **Expiration:** 2025-12-28T14:04:55
- **Days Until Expiration:** 27
- **Status:** VALID

### A Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 23312
- **Signer:** upchiapas.edu.mx
- **Labels:** 3
- **Original TTL:** 3600s
- **Inception:** 2025-11-28T13:04:55
- **Expiration:** 2025-12-28T14:04:55
- **Days Until Expiration:** 27
- **Status:** VALID

### TXT Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 23312
- **Signer:** upchiapas.edu.mx
- **Labels:** 3
- **Original TTL:** 3600s
- **Inception:** 2025-11-28T13:04:55
- **Expiration:** 2025-12-28T14:04:55
- **Days Until Expiration:** 27
- **Status:** VALID

### NS Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 23312
- **Signer:** upchiapas.edu.mx
- **Labels:** 3
- **Original TTL:** 172800s
- **Inception:** 2025-11-28T13:04:55
- **Expiration:** 2025-12-28T14:04:55
- **Days Until Expiration:** 27
- **Status:** VALID

### MX Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 23312
- **Signer:** upchiapas.edu.mx
- **Labels:** 3
- **Original TTL:** 3600s
- **Inception:** 2025-11-28T13:04:55
- **Expiration:** 2025-12-28T14:04:55
- **Days Until Expiration:** 27
- **Status:** VALID

## DS Records

- **Total DS Records:** 1
- **TTL:** 21600s

### DS Record 1

- **Key Tag:** 41013
- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Digest Type:** SHA-256 (2)
- **Digest:** `9df5f2a04c3ccbc5fb4419fb40b794fc27e51ce0dbef5c02bb11aff76b8987e7`

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
- **Iterations:** 10
- **Salt:** d872f0ed7d897bce

#### NSEC3 Record 2

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 10
- **Salt:** d872f0ed7d897bce

#### NSEC3 Record 3

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 10
- **Salt:** d872f0ed7d897bce

### NSEC3PARAM Details

- **Count:** 1
- **TTL:** 0s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 10
- **Salt:** d872f0ed7d897bce

---

## DNS Tree Structure

- **Domain:** upchiapas.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
upchiapas.edu.mx
├── ns1.akkyservicios.mx (TTL: 21600s)
├── ns2.akkyservicios.mx (TTL: 21600s)
└── ns3.akkyservicios.mx (TTL: 21600s)
```

### Cryptographic Chain of Trust

DS record exists in parent zone (edu.mx), establishing cryptographic chain of trust.

```
edu.mx (parent zone)
  └── DS Record → upchiapas.edu.mx
      └── KeyTag: 41013, Algorithm: RSASHA1-NSEC3-SHA1
```

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| upchiapas.edu.mx | Yes | Yes | Yes | Signed |
| edu.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Complete - Full trust path to root
