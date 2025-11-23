# DNSSEC Analysis Report: ipn.mx

**Analysis Date:** 2025-11-23T15:36:56.718931

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** enabled_incomplete
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** dns3.ipn.mx
- **Responsible Email:** tic.ipn.mx
- **Serial:** 2025112120
- **Refresh:** 10800s
- **Retry:** 1800s
- **Expire:** 1209600s
- **Minimum TTL:** 10800s
- **Record TTL:** 3418s

## NS Records

Total: 3

- dns2.ipn.mx (TTL: 1619s)
- dns1.ipn.mx (TTL: 1619s)
- dns3.ipn.mx (TTL: 1619s)

## A Records

Total: 1

- 20.64.80.120 (TTL: 963s)

## MX Records

Total: 1

- ipn-mx.mail.protection.outlook.com (Priority: 0, TTL: 3419s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 2
- **TTL:** 86219s

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

- **Type:** NONE
- **NSEC Present:** False
- **NSEC3 Present:** False
- **NSEC3PARAM Present:** True
- **Opt-Out:** False

### NSEC3PARAM Details

- **Count:** 1
- **TTL:** 3419s

#### NSEC3PARAM Record 1

- **Hash Algorithm:** 1
- **Flags:** 0
- **Iterations:** 1
- **Salt:** bd7619cce6c97e8f

---

## DNS Tree Structure

- **Domain:** ipn.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
ipn.mx
├── dns2.ipn.mx (TTL: 1619s)
├── dns1.ipn.mx (TTL: 1619s)
└── dns3.ipn.mx (TTL: 1619s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
