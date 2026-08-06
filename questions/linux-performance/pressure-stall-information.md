---
title: Use pressure stall information to find contention
theme: linux-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, cpu, memory, monitoring]
sources:
  - url: https://www.kernel.org/doc/html/latest/accounting/psi.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use pressure stall information to find contention

How does Linux PSI improve a performance investigation?

## Answer guide

- Pressure stall information measures time tasks are delayed because CPU, memory, or I/O resources are unavailable. Read both `some` pressure, where at least one task is stalled, and `full` pressure, where all non-idle tasks are stalled for that resource.
- Correlate PSI windows with application latency, throughput, cgroup limits, and conventional counters. Use the signals to narrow the resource class, then identify the runnable tasks, reclaim activity, or device queues responsible.
- PSI reports contention rather than a culprit or a universal threshold. Short bursts can be harmless and `full` semantics differ by resource, so alert thresholds must be tested against a service baseline and workload objectives.

## References

- [Linux kernel: Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Further reading (blog): [Brendan Gregg — Linux Performance Tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux PSI documentation](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Manual or specification: [proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Meta Engineering](https://engineering.fb.com/)
- Hands-on guide: [cgroup v2 documentation](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
