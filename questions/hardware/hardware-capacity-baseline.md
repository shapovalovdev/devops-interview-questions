---
title: Build a hardware capacity baseline
theme: hardware
difficulty: middle
type: scenario
tags: [hardware, capacity-planning, monitoring, reliability]
sources:
  - url: https://sre.google/sre-book/handling-overload/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build a hardware capacity baseline

What measurements do you need to decide whether a physical server fleet has enough capacity?

## Answer guide

- Measure service demand and headroom alongside CPU time, runnable work, memory pressure, storage latency/queueing, network throughput/errors, power, thermal state, and failure-domain capacity.
- Use peak and failure scenarios, not fleet averages: capacity must cover maintenance, a host or rack loss, and growth within the lead time to procure and deploy hardware.
- Define saturation and latency thresholds per workload and revisit forecasts after architecture or traffic changes. Buying for CPU alone can leave storage, memory, cooling, or network as the limiting resource.

## References

- [Google SRE Book: Handling overload](https://sre.google/sre-book/handling-overload/)
- Further reading (blog): [Backblaze: Enterprise drive reliability](https://www.backblaze.com/blog/enterprise-drive-reliability/)
