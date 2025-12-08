# DNSSEC Analysis Report: sep.gob.mx

**Analysis Date:** 2025-12-07T17:53:44.766138

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** enabled_incomplete
- **Has Signatures:** True
- **Has DS Record:** False
- **NSEC Type:** NSEC3

---

## SOA Records

- **Primary Server:** sepviagridmaster.sep.gob.mx
- **Responsible Email:** rickardo\.gonzalez.nube.sep.gob.mx
- **Serial:** 44886
- **Refresh:** 10800s
- **Retry:** 1080s
- **Expire:** 2419200s
- **Minimum TTL:** 900s
- **Record TTL:** 60s

## NS Records

Total: 10

- ns1-04.azure-dns.com (TTL: 60s)
- ns2-08.azure-dns.net (TTL: 60s)
- ns3-04.azure-dns.org (TTL: 60s)
- dns2.sep.gob.mx (TTL: 60s)
- ns4-04.azure-dns.info (TTL: 60s)
- ns1-08.azure-dns.com (TTL: 60s)
- ns4-08.azure-dns.info (TTL: 60s)
- ib01.sep.gob.mx (TTL: 60s)
- ns2-04.azure-dns.net (TTL: 60s)
- ns3-08.azure-dns.org (TTL: 60s)

## A Records

Total: 1

- 168.255.121.123 (TTL: 245s)

## MX Records

Total: 2

- as.sep.gob.mx (Priority: 10, TTL: 300s)
- as2.sep.gob.mx (Priority: 10, TTL: 300s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 3
- **TTL:** 21533s

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

### Key 3

- **Algorithm:** RSA/SHA-256 (8)
- **Key Size:** 1056 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

## RRSIG Records

- **Total Signatures:** 8
- **TTL:** 60s

### NSEC3PARAM Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 49816
- **Signer:** sep.gob.mx
- **Labels:** 3
- **Original TTL:** 60s
- **Inception:** 2025-12-07T11:22:55
- **Expiration:** 2025-12-11T12:07:01
- **Days Until Expiration:** 3
- **Status:** VALID

### DNSKEY Signatures (2)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 49816
- **Signer:** sep.gob.mx
- **Labels:** 3
- **Original TTL:** 172800s
- **Inception:** 2025-12-06T21:32:10
- **Expiration:** 2025-12-10T21:41:23
- **Days Until Expiration:** 3
- **Status:** VALID

#### Signature 2

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 34064
- **Signer:** sep.gob.mx
- **Labels:** 3
- **Original TTL:** 172800s
- **Inception:** 2025-12-06T21:32:10
- **Expiration:** 2025-12-10T21:41:23
- **Days Until Expiration:** 3
- **Status:** VALID

### MX Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 49816
- **Signer:** sep.gob.mx
- **Labels:** 3
- **Original TTL:** 300s
- **Inception:** 2025-12-07T11:22:55
- **Expiration:** 2025-12-11T12:07:01
- **Days Until Expiration:** 3
- **Status:** VALID

### A Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 49816
- **Signer:** sep.gob.mx
- **Labels:** 3
- **Original TTL:** 300s
- **Inception:** 2025-12-07T07:18:15
- **Expiration:** 2025-12-11T07:44:54
- **Days Until Expiration:** 3
- **Status:** VALID

### SOA Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 49816
- **Signer:** sep.gob.mx
- **Labels:** 3
- **Original TTL:** 60s
- **Inception:** 2025-12-07T13:10:39
- **Expiration:** 2025-12-11T14:10:39
- **Days Until Expiration:** 3
- **Status:** VALID

### NS Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 49816
- **Signer:** sep.gob.mx
- **Labels:** 3
- **Original TTL:** 60s
- **Inception:** 2025-12-07T07:18:15
- **Expiration:** 2025-12-11T07:44:54
- **Days Until Expiration:** 3
- **Status:** VALID

### TXT Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 49816
- **Signer:** sep.gob.mx
- **Labels:** 3
- **Original TTL:** 60s
- **Inception:** 2025-12-07T09:04:13
- **Expiration:** 2025-12-11T09:16:36
- **Days Until Expiration:** 3
- **Status:** VALID

## DS Records

No DS records found in parent zone.

## NSEC/NSEC3 Records

- **Type:** NSEC3
- **NSEC Present:** False
- **NSEC3 Present:** True
- **NSEC3PARAM Present:** True
- **Opt-Out:** False

### NSEC3 Details

- **Count:** 3
- **TTL:** 60s

#### NSEC3 Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 10
- **Salt:** 1899a5d0ef32c752660473

#### NSEC3 Record 2

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 10
- **Salt:** 1899a5d0ef32c752660473

#### NSEC3 Record 3

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 10
- **Salt:** 1899a5d0ef32c752660473

### NSEC3PARAM Details

- **Count:** 1
- **TTL:** 60s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 10
- **Salt:** 1899a5d0ef32c752660473

---

## DNS Tree Structure

- **Domain:** sep.gob.mx
- **Parent Zone:** gob.mx
- **Level:** 3

### Nameserver Hierarchy

```
sep.gob.mx
├── ns1-04.azure-dns.com (TTL: 60s)
├── ns2-08.azure-dns.net (TTL: 60s)
├── ns3-04.azure-dns.org (TTL: 60s)
├── dns2.sep.gob.mx (TTL: 60s)
├── ns4-04.azure-dns.info (TTL: 60s)
├── ns1-08.azure-dns.com (TTL: 60s)
├── ns4-08.azure-dns.info (TTL: 60s)
├── ib01.sep.gob.mx (TTL: 60s)
├── ns2-04.azure-dns.net (TTL: 60s)
└── ns3-08.azure-dns.org (TTL: 60s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (gob.mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| sep.gob.mx | Yes | No | Yes | Signed |
| gob.mx | Yes | Yes | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `sep.gob.mx`
