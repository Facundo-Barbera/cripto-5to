# DNSSEC Analysis Report: udg.mx

**Analysis Date:** 2025-12-01T10:06:39.972962

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** enabled_incomplete
- **Has Signatures:** True
- **Has DS Record:** False
- **NSEC Type:** NSEC3

---

## SOA Records

- **Primary Server:** e.ns.udg.mx
- **Responsible Email:** jaime.noc.udg.mx
- **Serial:** 320564
- **Refresh:** 10800s
- **Retry:** 1080s
- **Expire:** 2419200s
- **Minimum TTL:** 900s
- **Record TTL:** 21600s

## NS Records

Total: 3

- d.ns.udg.mx (TTL: 20085s)
- u.ns.udg.mx (TTL: 20085s)
- g.ns.udg.mx (TTL: 20085s)

## A Records

Total: 1

- 148.202.105.56 (TTL: 505s)

## AAAA Records

Total: 1

- 2001:1210:105:34:0:403:a8:1 (TTL: 19569s)

## MX Records

Total: 5

- alt1.aspmx.l.google.com (Priority: 5, TTL: 43s)
- alt2.aspmx.l.google.com (Priority: 5, TTL: 43s)
- alt3.aspmx.l.google.com (Priority: 10, TTL: 43s)
- aspmx.l.google.com (Priority: 1, TTL: 43s)
- alt4.aspmx.l.google.com (Priority: 10, TTL: 43s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 4
- **TTL:** 21600s

### Key 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Size:** 1056 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

### Key 2

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Size:** 1056 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

### Key 3

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Size:** 1056 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

### Key 4

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Size:** 2080 bits
- **Flags:** 257
- **Protocol:** 3
- **Type:** KSK (Key Signing Key)
- **Zone Key:** True

## RRSIG Records

- **Total Signatures:** 10
- **TTL:** 21600s

### AAAA Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 63917
- **Signer:** udg.mx
- **Labels:** 2
- **Original TTL:** 28800s
- **Inception:** 2025-11-30T18:54:08
- **Expiration:** 2025-12-04T19:05:40
- **Days Until Expiration:** 3
- **Status:** VALID

### SOA Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 63917
- **Signer:** udg.mx
- **Labels:** 2
- **Original TTL:** 28800s
- **Inception:** 2025-11-30T19:27:26
- **Expiration:** 2025-12-04T20:27:26
- **Days Until Expiration:** 3
- **Status:** VALID

### NS Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 63917
- **Signer:** udg.mx
- **Labels:** 2
- **Original TTL:** 28800s
- **Inception:** 2025-11-30T17:22:07
- **Expiration:** 2025-12-04T18:18:47
- **Days Until Expiration:** 3
- **Status:** VALID

### DNSKEY Signatures (2)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 63917
- **Signer:** udg.mx
- **Labels:** 2
- **Original TTL:** 172800s
- **Inception:** 2025-11-30T17:23:41
- **Expiration:** 2025-12-04T17:40:36
- **Days Until Expiration:** 3
- **Status:** VALID

#### Signature 2

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 41658
- **Signer:** udg.mx
- **Labels:** 2
- **Original TTL:** 172800s
- **Inception:** 2025-11-30T17:23:41
- **Expiration:** 2025-12-04T17:40:36
- **Days Until Expiration:** 3
- **Status:** VALID

### A Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 63917
- **Signer:** udg.mx
- **Labels:** 2
- **Original TTL:** 600s
- **Inception:** 2025-11-30T17:22:07
- **Expiration:** 2025-12-04T18:18:47
- **Days Until Expiration:** 3
- **Status:** VALID

### TXT Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 63917
- **Signer:** udg.mx
- **Labels:** 2
- **Original TTL:** 900s
- **Inception:** 2025-11-30T18:54:08
- **Expiration:** 2025-12-04T19:05:40
- **Days Until Expiration:** 3
- **Status:** VALID

### CAA Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 63917
- **Signer:** udg.mx
- **Labels:** 2
- **Original TTL:** 28800s
- **Inception:** 2025-11-30T18:54:08
- **Expiration:** 2025-12-04T19:05:40
- **Days Until Expiration:** 3
- **Status:** VALID

### MX Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 63917
- **Signer:** udg.mx
- **Labels:** 2
- **Original TTL:** 900s
- **Inception:** 2025-11-30T18:54:08
- **Expiration:** 2025-12-04T19:05:40
- **Days Until Expiration:** 3
- **Status:** VALID

### NSEC3PARAM Signatures (1)

#### Signature 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Tag:** 63917
- **Signer:** udg.mx
- **Labels:** 2
- **Original TTL:** 900s
- **Inception:** 2025-11-30T18:54:08
- **Expiration:** 2025-12-04T19:05:40
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
- **TTL:** 900s

#### NSEC3 Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 10
- **Salt:** 7af134e5155759e8ccef85

#### NSEC3 Record 2

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 10
- **Salt:** 7af134e5155759e8ccef85

#### NSEC3 Record 3

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 10
- **Salt:** 7af134e5155759e8ccef85

### NSEC3PARAM Details

- **Count:** 1
- **TTL:** 900s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 10
- **Salt:** 7af134e5155759e8ccef85

---

## DNS Tree Structure

- **Domain:** udg.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
udg.mx
├── d.ns.udg.mx (TTL: 20085s)
├── u.ns.udg.mx (TTL: 20085s)
└── g.ns.udg.mx (TTL: 20085s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| udg.mx | Yes | No | Yes | Signed |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `udg.mx`
