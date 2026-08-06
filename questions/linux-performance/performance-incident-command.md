---
title: Lead a Linux performance incident
theme: linux-performance
difficulty: staff
type: scenario
tags: [linux, performance, incident-response, monitoring, reliability]
sources:
  - url: https://www.kernel.org/doc/html/latest/accounting/psi.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Lead a Linux performance incident

How should an incident commander organize a cross-layer Linux performance incident?

## Answer guide

- State the user impact, time window, change timeline, service objective, and current mitigation hypothesis. Assign parallel but bounded investigation tracks for application demand, CPU and scheduling, memory pressure, I/O, network, and dependencies, with one evidence timeline and a decision owner.
- Prefer reversible mitigation that protects customers, such as load shedding, traffic shifting, concurrency reduction, or rollback, while preserving snapshots and measurements. Communicate uncertainty and stop low-value data collection that adds load to the failing system.
- Avoid a tool-driven scavenger hunt or multiple uncoordinated restarts. Performance failures are often queueing cascades across layers; a host metric improvement is not resolution until user outcomes, error rate, and recovery stability are verified.

## References

- [Linux kernel: Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Further reading (blog): [Brendan Gregg — The USE Method](https://www.brendangregg.com/usemethod.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- Maintainer or personal blog: [Brendan Gregg — USE Method](https://www.brendangregg.com/usemethod.html)
- Technical blog: [Google SRE](https://sre.google/resources/)
- Hands-on guide: [Linux performance tools](https://www.brendangregg.com/linuxperf.html)
