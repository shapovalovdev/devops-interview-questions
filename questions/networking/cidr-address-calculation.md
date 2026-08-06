---
title: Calculate an IPv4 CIDR range
theme: networking
difficulty: junior
type: theory
tags: [networking, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc4632.html
    source_type: standard
    verified_on: 2026-08-06
---

# Calculate an IPv4 CIDR range

What does `192.0.2.64/26` mean, and why does getting the prefix wrong cause operational outages?

## Answer guide

- CIDR writes an address plus the number of leading network bits. `/26` leaves six host bits, so the block has 64 addresses; `192.0.2.64/26` spans `.64` through `.127`, with `.64` as the network address in conventional IPv4 subnetting.
- The prefix, not a historical class, determines whether two addresses are on-link and which route is more specific. Route selection commonly favors the longest matching prefix, so a mistaken broad route can divert unrelated traffic.
- In a traditional broadcast subnet, the all-zero host value is the network address and the all-one value is directed broadcast; platform and cloud rules may reserve further addresses. Do not blindly subtract two when calculating usable addresses for every provider or point-to-point design.
- Validate a planned prefix against all existing routes and peering ranges. Overlapping RFC 1918 blocks are a frequent source of VPN, Kubernetes, and merger connectivity failures.

## References

- [RFC 4632: Classless Inter-domain Routing](https://www.rfc-editor.org/rfc/rfc4632.html)
- [Cloudflare learning: What is CIDR?](https://www.cloudflare.com/learning/network-layer/what-is-cidr/)
