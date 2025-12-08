# DNSSEC Analysis Report: nic.mx

**Analysis Date:** 2025-12-07T17:53:16.853117

## Summary

- **DNSSEC Enabled:** False
- **Validation Status:** disabled
- **Has Signatures:** False
- **Has DS Record:** False
- **NSEC Type:** none

---

## SOA Records

- **Primary Server:** a.nic.mx
- **Responsible Email:** hostmaster.nic.mx
- **Serial:** 2025090301
- **Refresh:** 3600s
- **Retry:** 900s
- **Expire:** 604800s
- **Minimum TTL:** 1800s
- **Record TTL:** 300s

## NS Records

Total: 6

- a.nic.mx (TTL: 300s)
- c.mx-ns.mx (TTL: 300s)
- o.mx-ns.mx (TTL: 300s)
- c.nic.mx (TTL: 300s)
- b.nic.mx (TTL: 300s)
- m.mx-ns.mx (TTL: 300s)

## A Records

Total: 4

- 200.94.180.61 (TTL: 242s)
- 200.94.180.58 (TTL: 242s)
- 200.94.180.60 (TTL: 242s)
- 200.94.180.59 (TTL: 242s)

## AAAA Records

Total: 4

- 2001:1250::60 (TTL: 242s)
- 2001:1250::61 (TTL: 242s)
- 2001:1250::58 (TTL: 242s)
- 2001:1250::59 (TTL: 242s)

## MX Records

Total: 2

- mail-ax.axtel-mty.nic.net.mx (Priority: 15, TTL: 300s)
- mail-tri.triara-mty.nic.net.mx (Priority: 20, TTL: 300s)

---

# DNSSEC Records

## DNSKEY Records

No DNSKEY records found.

## RRSIG Records

No RRSIG records found.

## DS Records

No DS records found in parent zone.

## NSEC/NSEC3 Records

- **Type:** NONE
- **NSEC Present:** False
- **NSEC3 Present:** False
- **NSEC3PARAM Present:** False
- **Opt-Out:** False

---

## DNS Tree Structure

- **Domain:** nic.mx
- **Parent Zone:** mx
- **Level:** 2

### Nameserver Hierarchy

```
nic.mx
├── a.nic.mx (TTL: 300s)
├── c.mx-ns.mx (TTL: 300s)
├── o.mx-ns.mx (TTL: 300s)
├── c.nic.mx (TTL: 300s)
├── b.nic.mx (TTL: 300s)
└── m.mx-ns.mx (TTL: 300s)
```

### Cryptographic Chain of Trust

No DS record found in parent zone (mx). Chain of trust not established.

### Full Chain of Trust to Root

| Zone | DNSKEY | DS | RRSIG | Status |
|------|--------|----|----- |--------|
| nic.mx | No | No | No | Unsigned |
| mx | Yes | Yes | Yes | Signed |
| . | Yes | N/A | Yes | Signed (Root) |

**Chain Status:** Broken at `nic.mx`
