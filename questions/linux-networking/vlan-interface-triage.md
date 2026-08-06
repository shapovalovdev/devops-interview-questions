---
title: Triage a Linux VLAN interface
theme: linux-networking
difficulty: middle
type: troubleshooting
tags: [linux, networking, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man8/ip-link.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a Linux VLAN interface

What evidence would you gather when a Linux VLAN interface cannot reach peers?

## Answer guide

- Verify the parent interface, VLAN ID, administrative/carrier state, address, route, and the selected egress interface. `ip -d link show` exposes link details that a basic interface listing can hide.
- Compare the host tagging design with the switch-port mode and allowed VLAN list. A host that tags frames needs a compatible trunk; an access port expects untagged traffic. Capture on the parent where safe to confirm tags and direction.
- Avoid fixing a mismatch by adding permissive VLANs or changing a switch trunk without an approved path design. Wrong VLAN membership can create a segmentation incident. Apply the durable change through the network owner and confirm DNS, gateway, and return-path behavior afterward.

## References

- [ip-link(8): Linux VLAN link configuration](https://man7.org/linux/man-pages/man8/ip-link.8.html)
- Further reading (blog): [Red Hat: network troubleshooting with packet captures](https://www.redhat.com/en/blog/network-packet-captures)
