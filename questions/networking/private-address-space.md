---
title: Use private IPv4 address space safely
theme: networking
difficulty: junior
type: scenario
tags: [networking, security, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1918.html
    source_type: standard
    verified_on: 2026-08-06
---

# Use private IPv4 address space safely

Which IPv4 ranges are private, and what must you plan before connecting two private networks?

## Answer guide

- RFC 1918 reserves `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16` for private internets. They are not globally unique and should not be advertised as public Internet routes.
- Before joining networks through a VPN, transit gateway, or acquisition, inventory every prefix. Identical or overlapping private ranges make an unambiguous route impossible without renumbering, translation, or carefully scoped proxying.
- NAT can conserve public addresses or bridge a controlled boundary, but it does not solve identity, authorization, observability, or all protocol behaviours. Record the original and translated address in telemetry where possible.
- Reserve non-overlapping blocks by environment, region, and future growth rather than allocating random /24s. A plan must also leave space for service, pod, and remote-access ranges.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918.html)
- [Cloudflare learning: What is a private IP address?](https://www.cloudflare.com/learning/network-layer/what-is-a-private-ip-address/)
## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)
