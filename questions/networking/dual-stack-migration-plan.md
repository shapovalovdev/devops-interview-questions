---
title: Plan a dual-stack migration
theme: networking
difficulty: senior
type: scenario
tags: [networking, dns, deployment, reliability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc8200.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc6724.html
    source_type: standard
    verified_on: 2026-08-06
---

# Plan a dual-stack migration

How would you introduce IPv6 to an IPv4 production service with measurable risk controls?

## Answer guide

- Inventory every hop: clients, DNS, CDN/load balancer, firewall/WAF, service listeners, outbound dependencies, logging, and incident tooling. IPv6 must be designed as an equivalent production path, not added only at the public edge.
- Allocate documented non-overlapping IPv6 prefixes, deploy and test routing/security policies, then expose a controlled dual-stack endpoint. Address selection is host-policy dependent, so validate real client behaviour and both success rate and latency by family.
- Publish AAAA only after the IPv6 path meets availability and security criteria. Use a canary name or limited audience first, retain A records for compatibility, and make AAAA withdrawal a tested rollback action.
- Track separate capacity, error, and abuse signals for IPv4 and IPv6. Missing IPv6 logging or rate limits creates an operational blind spot even when functional tests pass.

## References

- [RFC 8200: IPv6 specification](https://www.rfc-editor.org/rfc/rfc8200.html)
- [RFC 6724: Default address selection for IPv6](https://www.rfc-editor.org/rfc/rfc6724.html)
- [RIPE NCC IPv6 documentation](https://www.ripe.net/publications/docs/ripe-554/)
