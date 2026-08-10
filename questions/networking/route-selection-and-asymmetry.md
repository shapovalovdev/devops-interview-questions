---
title: Diagnose route selection and asymmetric paths
theme: networking
difficulty: middle
type: troubleshooting
tags: [networking, troubleshooting, reliability]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1812.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc4632.html
    source_type: standard
    verified_on: 2026-08-06
---

# Diagnose route selection and asymmetric paths

Why can a reachable destination still fail for a stateful service after a route change?

## Answer guide

- Forwarding selects a next hop from a routing table; CIDR deployments generally use the most-specific matching route before implementation-specific preferences. Inspect the actual route lookup in the sending namespace/device, not only the intended route configuration.
- The reverse path can differ. Asymmetry is not inherently broken, but stateful firewalls, NAT, load balancers, and source-address validation may require both directions to traverse compatible state or policy.
- Compare forward and return packet captures, source addresses, route tables, policy-routing rules, and middlebox state. A SYN reaching a server with a SYN-ACK returning through an unexpected boundary is a classic symptom.
- Avoid fixing by adding a broad static route without checking overlap and failover. Use explicit route ownership, route-change review, and tests for both directions and both IP families.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 1812: Requirements for IPv4 routers](https://www.rfc-editor.org/rfc/rfc1812.html)
- [RFC 4632: CIDR and longest-match routing](https://www.rfc-editor.org/rfc/rfc4632.html)
- [Cloudflare learning: What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)
## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)
