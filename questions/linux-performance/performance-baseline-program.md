---
title: Establish a Linux performance baseline program
theme: linux-performance
difficulty: staff
type: scenario
tags: [linux, performance, monitoring, capacity-planning, governance]
sources:
  - url: https://www.kernel.org/doc/html/latest/accounting/psi.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish a Linux performance baseline program

How would you make host-performance baselines useful across a fleet?

## Answer guide

- Define service-facing objectives and a small, versioned host signal set: CPU demand and saturation, memory availability and pressure, I/O latency and queueing, network errors, and workload throughput. Segment data by hardware class, kernel, runtime, tenant, and workload instead of averaging unrelated hosts.
- Capture healthy and peak baselines with time windows, workload descriptors, sampling fidelity, ownership, retention, and access controls. Review drift after kernel, instance-type, storage, application, or traffic changes and link dashboards to runbooks and capacity decisions.
- A broad dashboard without workload context creates noisy comparisons and false confidence. Do not use one global threshold as an SLO; validate alerts against incidents and prevent collection overhead or cardinality from becoming a fleet-wide cost.

## References

- [Linux kernel: Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Further reading (blog): [Brendan Gregg — The USE Method](https://www.brendangregg.com/usemethod.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- Maintainer or personal blog: [Brendan Gregg — USE Method](https://www.brendangregg.com/usemethod.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Linux performance tools](https://www.brendangregg.com/linuxperf.html)
