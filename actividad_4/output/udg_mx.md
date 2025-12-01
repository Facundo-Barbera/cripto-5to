# DNSSEC Analysis Report: udg.mx

**Analysis Date:** 2025-11-29T14:48:43.412847

## Summary

- **DNSSEC Enabled:** True
- **Validation Status:** enabled_incomplete
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** NSEC3

---

## SOA Records

- **Primary Server:** e.ns.udg.mx
- **Responsible Email:** jaime.noc.udg.mx
- **Serial:** 320192
- **Refresh:** 10800s
- **Retry:** 1080s
- **Expire:** 2419200s
- **Minimum TTL:** 900s
- **Record TTL:** 21600s

## NS Records

Total: 3

- u.ns.udg.mx (TTL: 21600s)
- d.ns.udg.mx (TTL: 21600s)
- g.ns.udg.mx (TTL: 21600s)

## A Records

Total: 1

- 148.202.105.56 (TTL: 191s)

## AAAA Records

Total: 1

- 2001:1210:105:34:0:403:a8:1 (TTL: 14124s)

## MX Records

Total: 5

- alt4.aspmx.l.google.com (Priority: 10, TTL: 900s)
- alt3.aspmx.l.google.com (Priority: 10, TTL: 900s)
- alt2.aspmx.l.google.com (Priority: 5, TTL: 900s)
- alt1.aspmx.l.google.com (Priority: 5, TTL: 900s)
- aspmx.l.google.com (Priority: 1, TTL: 900s)

---

# DNSSEC Records

## DNSKEY Records

- **Total Keys:** 4
- **TTL:** 172800s

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

- **Count:** 0
- **TTL:** Nones

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
├── u.ns.udg.mx (TTL: 21600s)
├── d.ns.udg.mx (TTL: 21600s)
└── g.ns.udg.mx (TTL: 21600s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.
