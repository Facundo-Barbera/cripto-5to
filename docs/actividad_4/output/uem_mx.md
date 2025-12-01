# DNSSEC Analysis Report: uem.mx

**Analysis Date:** 2025-12-01T10:11:19.190109

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** True
- **Has DS Record:** False
- **NSEC Type:** NSEC3

---

---

# DNSSEC Records

## DNSKEY Records

No DNSKEY records found.

## RRSIG Records

- **Total Signatures:** 1
- **TTL:** Nones

### NSEC3 Signatures (1)

#### Signature 1

- **Algorithm:** RSA/SHA-256 (8)
- **Key Tag:** 13071
- **Signer:** mx
- **Labels:** 2
- **Original TTL:** 1800s
- **Inception:** 2025-11-29T18:00:00
- **Expiration:** 2025-12-29T18:00:00
- **Days Until Expiration:** 28
- **Status:** VALID

## DS Records

No DS records found in parent zone.

## NSEC/NSEC3 Records

- **Type:** NSEC3
- **NSEC Present:** False
- **NSEC3 Present:** True
- **NSEC3PARAM Present:** False
- **Opt-Out:** True

### NSEC3 Details

- **Count:** 3
- **TTL:** 1800s

#### NSEC3 Record 1

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 0
- **Salt:** c4b62f0ddaf59fd0

#### NSEC3 Record 2

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 0
- **Salt:** c4b62f0ddaf59fd0

#### NSEC3 Record 3

- **Hash Algorithm:** 1
- **Flags:** 1
- **Iterations:** 0
- **Salt:** c4b62f0ddaf59fd0

---

## DNS Tree Structure

- **Domain:** uem.mx
- **Parent Zone:** mx
- **Level:** 2

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| uem.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `uem.mx`
