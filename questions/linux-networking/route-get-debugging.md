---
title: Debug a Linux route with ip route get
theme: linux-networking
difficulty: middle
type: troubleshooting
tags: [linux, networking, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man8/ip-route.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug a Linux route with ip route get

How would you find why a Linux host chooses an unexpected network path?

## Answer guide

- Query `ip route get <destination>` and, for a realistic flow, include source, input interface, mark, protocol, and ports where the command supports them. This asks the kernel for the route it would use, instead of relying on a visually scanned route table.
- Compare that decision with `ip rule show`, route tables, address scope, and any VPN, VRF, or firewall mark configuration. Policy routing can select a different table before ordinary longest-prefix route selection applies.
- Confirm the chosen next hop is reachable with neighbour state and packet evidence. Route changes can break return paths, management access, or another traffic class; stage changes with an explicit source/destination test matrix and retain an out-of-band rollback route.

## References

- [ip-route(8): route lookup and policy-routing options](https://man7.org/linux/man-pages/man8/ip-route.8.html)
- Further reading (blog): [Red Hat: Linux network troubleshooting commands](https://www.redhat.com/en/blog/linux-network-troubleshooting-commands)
