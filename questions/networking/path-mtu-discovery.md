---
title: Diagnose a path MTU discovery black hole
theme: networking
difficulty: middle
type: troubleshooting
tags: [networking, tcp, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1191.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc8201.html
    source_type: standard
    verified_on: 2026-08-06
---

# Diagnose a path MTU discovery black hole

Why can small requests work while larger responses hang across a VPN or tunnel?

## Answer guide

- The path MTU is the smallest packet size a path can carry without fragmentation. IPv4 Path MTU Discovery relies on a router returning ICMP "fragmentation needed" when a packet with Don't Fragment set is too large; IPv6 routers do not fragment forwarded packets and rely on ICMPv6 Packet Too Big.
- A tunnel adds encapsulation overhead, reducing the effective inner MTU. If ICMP control messages are blocked, a sender can continue sending packets that disappear: small payloads work, while TLS certificates, downloads, or responses above the effective MTU stall.
- Confirm with packet capture and controlled packet-size probes in both directions. Inspect interface/tunnel MTUs, MSS negotiation/clamping, and firewall policy for ICMP/ICMPv6 errors; do not merely lower application payload limits.
- A low MTU is a throughput/CPU trade-off, while indiscriminate ICMP blocking breaks essential control signals. Test both IPv4 and IPv6 because their fragmentation rules differ.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 1191: Path MTU Discovery for IPv4](https://www.rfc-editor.org/rfc/rfc1191.html)
- [RFC 8201: Path MTU Discovery for IPv6](https://www.rfc-editor.org/rfc/rfc8201.html)
- [Cloudflare learning: What is MTU?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)
## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)
