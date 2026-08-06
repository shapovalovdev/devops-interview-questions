---
title: Map a request to network layers
theme: networking
difficulty: junior
type: theory
tags: [networking, tcp, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc1122.html
    source_type: standard
    verified_on: 2026-08-06
---

# Map a request to network layers

When an HTTPS request fails, how do link, IP, transport, and application layers help you narrow the problem?

## Answer guide

- Treat layers as a diagnostic boundary, not a promise that every system implements a textbook OSI stack. Ethernet/Wi-Fi delivers frames on a local link; IP routes packets between networks; TCP or UDP identifies transport flows; TLS and HTTP are application protocols carried above them.
- Start from the lowest plausible failure: link/interface state and addressing, then route and IP reachability, then TCP/UDP ports and packet exchange, then TLS/HTTP semantics. A successful ping only demonstrates a particular IP control exchange; it does not prove a TCP service or HTTP route works.
- Capture observations at the boundary that failed: interface counters, route lookup, packet capture, socket state, and application/proxy logs. This prevents changing DNS or TLS settings when packets never leave the host.
- Middleboxes can blur layers: a firewall can reject TCP while IP routing works, and a proxy can return HTTP while the upstream is unreachable. State the protocol and endpoint actually tested.

## References

- [RFC 1122: Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1122.html)
- [Cloudflare learning: What is the OSI model?](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)
