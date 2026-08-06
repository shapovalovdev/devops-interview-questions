---
title: Build a capacity model for a Linux service
theme: linux-performance
difficulty: staff
type: scenario
tags: [linux, performance, capacity-planning, reliability, governance]
sources:
  - url: https://www.kernel.org/doc/html/latest/accounting/psi.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build a capacity model for a Linux service

What should a capacity model for a Linux-hosted service prove before growth?

## Answer guide

- Model demand, resource consumption, saturation, error behavior, and tail latency against a stated workload unit. Include CPU, memory working set, I/O, network, limits, redundancy, maintenance capacity, and the service's recovery objectives rather than extrapolating from CPU percent alone.
- Validate the model with load tests and production observations across normal, peak, degraded, and failure conditions. Publish assumptions, uncertainty, headroom policy, scaling lead time, and an accountable review cadence for product and platform owners.
- Linear extrapolation often fails at queueing, cache, lock, quota, or downstream boundaries. Do not count spare aggregate fleet resources as service capacity until placement, failure domains, and noisy-neighbor constraints are demonstrated.

## References

- [Linux kernel: Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Further reading (blog): [Brendan Gregg — The USE Method](https://www.brendangregg.com/usemethod.html)

## What to learn next

- Official documentation: [Linux PSI documentation](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Manual or specification: [vmstat(8)](https://man7.org/linux/man-pages/man8/vmstat.8.html)
- Maintainer or personal blog: [Brendan Gregg — USE Method](https://www.brendangregg.com/usemethod.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Linux performance tools](https://www.brendangregg.com/linuxperf.html)
