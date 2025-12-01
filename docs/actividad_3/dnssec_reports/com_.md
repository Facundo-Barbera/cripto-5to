# DNSSEC Analysis Report: com.

**Analysis Date:** 2025-11-27T10:55:59.333916

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** valid
- **Has Signatures:** True
- **Has DS Record:** True
- **NSEC Type:** NSEC3

---

## SOA Records

- **Primary Server:** a.gtld-servers.net
- **Responsible Email:** nstld.verisign-grs.com
- **Serial:** 1764261670
- **Refresh:** 1800s
- **Retry:** 900s
- **Expire:** 604800s
- **Minimum TTL:** 900s
- **Record TTL:** 30s

## NS Records

Total: 13

- a.gtld-servers.net (TTL: 21600s)
- i.gtld-servers.net (TTL: 21600s)
- m.gtld-servers.net (TTL: 21600s)
- g.gtld-servers.net (TTL: 21600s)
- d.gtld-servers.net (TTL: 21600s)
- h.gtld-servers.net (TTL: 21600s)
- e.gtld-servers.net (TTL: 21600s)
- b.gtld-servers.net (TTL: 21600s)
- c.gtld-servers.net (TTL: 21600s)
- l.gtld-servers.net (TTL: 21600s)
- k.gtld-servers.net (TTL: 21600s)
- j.gtld-servers.net (TTL: 21600s)
- f.gtld-servers.net (TTL: 21600s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 2
- **TTL:** 996s

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

- **Total Signatures:** 4
- **TTL:** 900s

### SOA Signatures (1)

#### Signature 1

- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Key Tag:** 46539
- **Signer:** com
- **Labels:** 1
- **Original TTL:** 900s
- **Inception:** 2025-11-27T09:45:50
- **Expiration:** 2025-12-04T10:55:50
- **Days Until Expiration:** 6
- **Status:** VALID

### DNSKEY Signatures (1)

#### Signature 1

- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Key Tag:** 19718
- **Signer:** com
- **Labels:** 1
- **Original TTL:** 86400s
- **Inception:** 2025-11-18T08:57:35
- **Expiration:** 2025-12-03T09:02:35
- **Days Until Expiration:** 5
- **Status:** VALID

### NSEC3PARAM Signatures (1)

#### Signature 1

- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Key Tag:** 46539
- **Signer:** com
- **Labels:** 1
- **Original TTL:** 86400s
- **Inception:** 2025-11-24T17:16:55
- **Expiration:** 2025-12-01T18:26:55
- **Days Until Expiration:** 4
- **Status:** VALID

### NS Signatures (1)

#### Signature 1

- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Key Tag:** 46539
- **Signer:** com
- **Labels:** 1
- **Original TTL:** 172800s
- **Inception:** 2025-11-24T17:16:55
- **Expiration:** 2025-12-01T18:26:55
- **Days Until Expiration:** 4
- **Status:** VALID

## DS Records

- **Total DS Records:** 1
- **TTL:** 10446s

### DS Record 1

- **Key Tag:** 19718
- **Algorithm:** ECDSA-P256/SHA-256 (13)
- **Digest Type:** SHA-256 (2)
- **Digest:** `8acbb0cd28f41250a80a491389424d341522d946b0da0c0291f2d3d771d7805a`

## NSEC/NSEC3 Records

- **Type:** NSEC3
- **NSEC Present:** False
- **NSEC3 Present:** True
- **NSEC3PARAM Present:** True
- **Opt-Out:** True

### NSEC3 Details

- **Count:** 3
- **TTL:** 900s

#### NSEC3 Record 1

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 0
- **Salt:** none

#### NSEC3 Record 2

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 0
- **Salt:** none

#### NSEC3 Record 3

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 0
- **Salt:** none

### NSEC3PARAM Details

- **Count:** 1
- **TTL:** 6696s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 0
- **Salt:** none

---

## DNS Tree Structure

- **Domain:** com.
- **Parent Zone:** 
- **Level:** 2

### Nameserver Hierarchy

```
com.
├── a.gtld-servers.net (TTL: 21600s)
├── i.gtld-servers.net (TTL: 21600s)
├── m.gtld-servers.net (TTL: 21600s)
├── g.gtld-servers.net (TTL: 21600s)
├── d.gtld-servers.net (TTL: 21600s)
├── h.gtld-servers.net (TTL: 21600s)
├── e.gtld-servers.net (TTL: 21600s)
├── b.gtld-servers.net (TTL: 21600s)
├── c.gtld-servers.net (TTL: 21600s)
├── l.gtld-servers.net (TTL: 21600s)
├── k.gtld-servers.net (TTL: 21600s)
├── j.gtld-servers.net (TTL: 21600s)
└── f.gtld-servers.net (TTL: 21600s)
```

### Cryptographic Chain of Trust

DS record exists in parent zone (), establishing cryptographic chain of trust.

```
 (parent zone)
  └── DS Record → com.
      └── KeyTag: 19718, Algorithm: ECDSA-P256/SHA-256
```
