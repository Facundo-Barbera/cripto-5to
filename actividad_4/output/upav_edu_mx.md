# DNSSEC Analysis Report: upav.edu.mx

**Analysis Date:** 2025-11-29T14:49:38.989124

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** enabled_incomplete
- **Has Signatures:** False
- **Has DS Record:** True
- **NSEC Type:** NSEC3

---

## SOA Records

- **Primary Server:** ns1.akkyservicios.mx
- **Responsible Email:** hostmaster.akkyservicios.mx.upav.edu.mx
- **Serial:** 1763841721
- **Refresh:** 3600s
- **Retry:** 900s
- **Expire:** 604800s
- **Minimum TTL:** 1800s
- **Record TTL:** 21600s

## NS Records

Total: 3

- ns3.akkyservicios.mx (TTL: 21600s)
- ns2.akkyservicios.mx (TTL: 21600s)
- ns1.akkyservicios.mx (TTL: 21600s)

## A Records

Total: 1

- 50.21.179.29 (TTL: 3148s)

## MX Records

Total: 6

- smtp-relay.gmail.com (Priority: 15, TTL: 3600s)
- aspmx.l.google.com (Priority: 1, TTL: 3600s)
- alt2.aspmx.l.google.com (Priority: 5, TTL: 3600s)
- alt4.aspmx.l.google.com (Priority: 10, TTL: 3600s)
- alt3.aspmx.l.google.com (Priority: 10, TTL: 3600s)
- alt1.aspmx.l.google.com (Priority: 5, TTL: 3600s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 3
- **TTL:** 3600s

### Key 1

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Size:** 1056 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

### Key 2

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Size:** 2080 bits
- **Flags:** 257
- **Protocol:** 3
- **Type:** KSK (Key Signing Key)
- **Zone Key:** True

### Key 3

- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Key Size:** 1056 bits
- **Flags:** 256
- **Protocol:** 3
- **Type:** ZSK (Zone Signing Key)
- **Zone Key:** True

## RRSIG Records

No RRSIG records found.

## DS Records

- **Total DS Records:** 1
- **TTL:** 21600s

### DS Record 1

- **Key Tag:** 10848
- **Algorithm:** RSASHA1-NSEC3-SHA1 (7)
- **Digest Type:** SHA-256 (2)
- **Digest:** `a199322c018925f9507d2fbacab2f6dbba9bd97aa26b53b6895c3ab5a2e93b1d`

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
- **TTL:** 0s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 10
- **Salt:** aab2eef8b719fd26

---

## DNS Tree Structure

- **Domain:** upav.edu.mx
- **Parent Zone:** edu.mx
- **Level:** 3

### Nameserver Hierarchy

```
upav.edu.mx
├── ns3.akkyservicios.mx (TTL: 21600s)
├── ns2.akkyservicios.mx (TTL: 21600s)
└── ns1.akkyservicios.mx (TTL: 21600s)
```

### Cryptographic Chain of Trust

DS record exists in parent zone (edu.mx), establishing cryptographic chain of trust.

```
edu.mx (parent zone)
  └── DS Record → upav.edu.mx
      └── KeyTag: 10848, Algorithm: RSASHA1-NSEC3-SHA1
```
