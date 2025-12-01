# DNSSEC Analysis Report: ipn.mx

**Analysis Date:** 2025-11-27T10:56:03.851630

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
- **Serial:** 2025112572
- **Refresh:** 10800s
- **Retry:** 1800s
- **Expire:** 1209600s
- **Minimum TTL:** 10800s
- **Record TTL:** 3600s

## NS Records

Total: 3

- dns3.ipn.mx (TTL: 1692s)
- dns2.ipn.mx (TTL: 1692s)
- dns1.ipn.mx (TTL: 1692s)

## A Records

Total: 1

- 20.64.80.120 (TTL: 569s)

## MX Records

Total: 1

- ipn-mx.mail.protection.outlook.com (Priority: 0, TTL: 1730s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 2
- **TTL:** 21600s

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

- **Count:** 3
- **TTL:** 10800s

#### NSEC3 Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 1
- **Salt:** f3a7b355cfc90a2c

#### NSEC3 Record 2

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 1
- **Salt:** f3a7b355cfc90a2c

#### NSEC3 Record 3

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 1
- **Salt:** f3a7b355cfc90a2c

### NSEC3PARAM Details

- **Count:** 1
- **TTL:** 736s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 1
- **Salt:** f3f14e0c838ae7de

---

## DNS Tree Structure

- **Domain:** ipn.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
ipn.mx
├── dns3.ipn.mx (TTL: 1692s)
├── dns2.ipn.mx (TTL: 1692s)
└── dns1.ipn.mx (TTL: 1692s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
