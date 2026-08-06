---
title: Triage a failed Linux neighbour entry
theme: linux-networking
difficulty: middle
type: troubleshooting
tags: [linux, networking, troubleshooting]
sources:
  - url: https://www.man7.org/linux/man-pages/man8/ip-neighbour.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a failed Linux neighbour entry

What does a `FAILED` neighbour entry indicate, and how do you investigate it?

## Answer guide

- Linux neighbour entries bind an IP neighbour to a link-layer address on a shared link. IPv4 entries are commonly called the ARP table; `FAILED` means neighbour resolution did not establish a usable binding.
- Check `ip neigh`, the interface carrier/VLAN, the selected route, and captures for ARP or IPv6 neighbour-discovery requests and replies. Verify the peer address, duplicate addressing, switch-port configuration, and the correct L2 broadcast domain.
- Flushing neighbours can force another lookup but is not a root-cause fix and can disrupt active traffic. Static entries and proxy ARP/NDP have operational consequences; use them only with an owned design and remove emergency workarounds after the underlying L2 or addressing fault is corrected.

## References

- [ip-neighbour(8): Linux neighbour-table states](https://www.man7.org/linux/man-pages/man8/ip-neighbour.8.html)
- Further reading (blog): [Red Hat: network troubleshooting with packet captures](https://www.redhat.com/en/blog/network-packet-captures)
