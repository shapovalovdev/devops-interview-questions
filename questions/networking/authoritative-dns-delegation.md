---
title: Debug an authoritative DNS delegation
theme: networking
difficulty: middle
type: troubleshooting
tags: [dns, networking, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1034.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc1912.html
    source_type: standard
    verified_on: 2026-08-06
---

# Debug an authoritative DNS delegation

A new subdomain works against its nameserver but fails for public resolvers. What delegation checks do you perform?

## Answer guide

- A child zone is visible only when its parent publishes a correct delegation (NS records, and glue where needed). Data loaded on the child authoritative server alone does not update the parent zone.
- Query the parent and each delegated authoritative server directly, then compare the delegation NS set, glue addresses, zone apex SOA/NS, and the desired record. Check that every advertised nameserver is reachable over the required transport and serves the same current zone.
- In-bailiwick nameserver names require usable glue at the parent to break the lookup dependency. Stale glue, mismatched nameserver sets, or a nameserver that only answers one address family can make failures intermittent.
- Wait for parent and resolver caches according to TTLs before declaring a correction ineffective. Do not use a recursive resolver's answer as proof that the authoritative data is correct; it may be cached.

## References

- [RFC 1034: DNS delegations and glue](https://www.rfc-editor.org/rfc/rfc1034.html)
- [RFC 1912: Common DNS operational errors](https://www.rfc-editor.org/rfc/rfc1912.html)
- [ICANN: DNS basics](https://www.icann.org/resources/pages/dns-2018-10-25-en)
