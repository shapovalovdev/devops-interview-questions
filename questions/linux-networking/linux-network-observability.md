---
title: Design Linux host network observability
theme: linux-networking
difficulty: senior
type: scenario
tags: [linux, networking, monitoring, reliability]
sources:
  - url: https://docs.kernel.org/networking/statistics.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design Linux host network observability

What would a useful Linux network observability baseline include?

## Answer guide

- Combine interface counters and errors, link state, route/neighbour changes, socket and TCP statistics, DNS outcomes, connection-tracking pressure, and application request metrics. Label measurements by interface, namespace, workload, address family, and destination class where cardinality remains controlled.
- Establish symptoms at more than one layer: user-visible availability and latency, host packet drops/retransmissions, and path-specific synthetic probes. This prevents a healthy aggregate bandwidth graph from hiding a broken region, IPv6 path, or individual tenant.
- Counters alone do not identify causality, and high-cardinality flow telemetry can become expensive or expose sensitive data. Define retention, sampling, alerts, and packet-evidence access before an incident. Review baselines after kernel, CNI, NIC, routing, or traffic-pattern changes.

## References

- [Linux kernel: networking statistics](https://docs.kernel.org/networking/statistics.html)
- Further reading (blog): [Cloudflare: lessons from debugging network performance](https://blog.cloudflare.com/network-performance-update/)
