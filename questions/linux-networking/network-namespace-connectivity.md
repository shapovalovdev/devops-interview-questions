---
title: Debug connectivity across a Linux network namespace
theme: linux-networking
difficulty: middle
type: troubleshooting
tags: [linux, networking, containers, troubleshooting, ckne]
sources:
  - url: https://man7.org/linux/man-pages/man7/network_namespaces.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Debug connectivity across a Linux network namespace

How do network namespaces change Linux network troubleshooting?

## Answer guide

- A network namespace isolates network devices, protocol stacks, routing tables, firewall rules, and related networking state. Commands run in the host namespace can therefore look healthy while the workload namespace lacks an address, route, DNS configuration, or policy.
- Enter or target the affected namespace deliberately, then repeat the same evidence chain: interfaces, addresses, routes, neighbour state, sockets, resolver path, and packets. Map veth pairs, bridges, and namespace IDs so both ends of the boundary are known.
- Do not move interfaces or alter namespace firewall state casually on a production host; such changes can sever workloads. Container runtimes and CNI plugins own much of this topology, so repair their declared configuration and validate that recreation produces the intended state.

## References

- [network_namespaces(7): Linux network namespace isolation](https://man7.org/linux/man-pages/man7/network_namespaces.7.html)
- Further reading (blog): [Red Hat: network troubleshooting with packet captures](https://www.redhat.com/en/blog/network-packet-captures)
