---
title: Build a Linux network capacity strategy
theme: linux-networking
difficulty: staff
type: scenario
tags: [linux, networking, capacity-planning, monitoring, reliability]
sources:
  - url: https://docs.kernel.org/networking/statistics.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build a Linux network capacity strategy

How would you plan Linux host network capacity for a growing platform?

## Answer guide

- Model demand by workload and path: bytes, packets, connections, new-flow rate, packet size, encryption/tunnel overhead, interrupt/CPU cost, and failure headroom. Use percentile and burst behavior, not only monthly average throughput.
- Join host counters and saturation signals with NIC, hypervisor, switch, load-balancer, and application SLO data. Capacity is constrained by the narrowest relevant resource, which may be connection tracking, CPU, queue depth, or a shared egress path rather than link speed.
- Turn the model into decisions: scale thresholds, test scenarios, procurement lead time, and a budget for redundancy. Overprovisioning every host is costly, while a single aggregate target hides noisy-neighbour and regional risk. Recalibrate after architecture or traffic changes and exercise the failure margin.

## References

- [Linux kernel: networking statistics](https://docs.kernel.org/networking/statistics.html)
- Further reading (blog): [Cloudflare: lessons from debugging network performance](https://blog.cloudflare.com/network-performance-update/)
