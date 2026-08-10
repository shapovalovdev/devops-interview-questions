---
title: Diagnose a failed TCP three-way handshake
theme: networking
difficulty: middle
type: troubleshooting
tags: [tcp, networking, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9293.html
    source_type: standard
    verified_on: 2026-08-06
---

# Diagnose a failed TCP three-way handshake

A client times out connecting to a TCP service. How do SYN, SYN-ACK, ACK, refusal, and silence guide the investigation?

## Answer guide

- A normal active open sends SYN; the passive endpoint replies SYN-ACK; the initiator acknowledges it, after which both sides can exchange bytes. Capture at both endpoints or a reliable network tap to see where that sequence stops.
- SYN followed by RST normally means the reached host has no matching listener or a policy actively rejects the connection. Repeated SYNs with no reply usually indicates a drop, wrong route, security rule, or return-path problem; it is not proof that the application is down.
- A SYN-ACK observed leaving the server but not acknowledged points to a client-side or asymmetric-path issue. A completed handshake followed by failure moves the investigation to TLS/application behaviour.
- Avoid inferring state from one host's logs alone: NAT, load balancers, firewalls, and SYN proxies can originate or consume handshake packets. Record source/destination tuple, interface, and timestamps.

## References

- Further reading (blog): [Complementary networking practice article](https://blog.cloudflare.com/network-performance-update/)
- [RFC 9293: TCP connection establishment](https://www.rfc-editor.org/rfc/rfc9293.html)
- [Cloudflare learning: What is a TCP handshake?](https://www.cloudflare.com/learning/ddos/tcp-three-way-handshake/)
## What to learn next

- Official documentation: [RFC Editor](https://www.rfc-editor.org/)
- Manual or specification: [IANA protocol registries](https://www.iana.org/protocols)
- Maintainer or personal blog: [Julia Evans — networking articles](https://jvns.ca/categories/networking/)
- Technical blog: [Cloudflare networking engineering blog](https://blog.cloudflare.com/tag/networking/)
- Hands-on guide: [ns-3 documentation](https://www.nsnam.org/docs/)
