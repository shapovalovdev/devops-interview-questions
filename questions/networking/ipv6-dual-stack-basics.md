---
title: Operate a dual-stack service
theme: networking
difficulty: middle
type: scenario
tags: [networking, dns, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc8200.html
    source_type: standard
    verified_on: 2026-08-06
  - url: https://www.rfc-editor.org/rfc/rfc4861.html
    source_type: standard
    verified_on: 2026-08-06
---

# Operate a dual-stack service

What must you validate before publishing an AAAA record for an existing IPv4 service?

## Answer guide

- IPv6 is not just a longer IPv4 address: it has a different base header, uses Neighbor Discovery rather than ARP, and has different fragmentation and ICMP requirements. An AAAA record makes IPv6-capable clients attempt the IPv6 path.
- Validate end-to-end IPv6: address assignment, default route, DNS response, listener binding, load balancer/proxy behaviour, firewall policy, observability, and return traffic. Test from independent IPv6 networks, not only the server itself.
- Keep security policy functionally equivalent across IP families. A frequent outage/security gap is exposing a service through IPv6 while only maintaining IPv4 firewall rules and monitoring.
- Roll out AAAA deliberately and measure connection success/latency by address family. Do not remove IPv4 solely because IPv6 works in one environment; partner, client, and provider support can differ.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 8200: Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200.html)
- [RFC 4861: IPv6 Neighbor Discovery](https://www.rfc-editor.org/rfc/rfc4861.html)
- [Cloudflare learning: What is IPv6?](https://www.cloudflare.com/learning/ddos/glossary/internet-protocol-version-6-ipv6/)
## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)
