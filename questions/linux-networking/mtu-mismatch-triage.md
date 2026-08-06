---
title: Diagnose an MTU mismatch on Linux
theme: linux-networking
difficulty: middle
type: troubleshooting
tags: [linux, networking, tcp, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man8/ip-link.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose an MTU mismatch on Linux

A service works for small requests but stalls for larger responses across a tunnel. How do you investigate MTU?

## Answer guide

- Inspect interface MTUs with `ip link show`, including tunnel, VLAN, bridge, and physical interfaces, then identify the effective end-to-end path. Encapsulation consumes bytes, so an unchanged inner MTU can exceed the underlying path.
- Test progressively sized traffic with a method appropriate to the protocol and observe packet captures, ICMP errors, retransmissions, and application latency. Distinguish an MTU problem from TCP window, proxy buffering, or application-size limits.
- Fix the path consistently: allow required ICMP packet-too-big/fragmentation feedback where the design depends on it, set a safe MTU or MSS strategy at the proper boundary, and test both directions. A blanket small MTU reduces efficiency; changing only one host can leave asymmetric or containerized paths broken.

## References

- [ip-link(8): Linux link attributes including MTU](https://man7.org/linux/man-pages/man8/ip-link.8.html)
- Further reading (blog): [Red Hat: network troubleshooting with packet captures](https://www.redhat.com/en/blog/network-packet-captures)
