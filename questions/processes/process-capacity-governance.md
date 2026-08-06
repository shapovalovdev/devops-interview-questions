---
title: Govern fleet process capacity and limits
theme: processes
difficulty: staff
type: scenario
tags: [linux, processes, capacity-planning, limits, performance, governance]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern fleet process capacity and limits

How would you prevent process, PID, and descriptor exhaustion across a large Linux fleet?

## Answer guide

- Model capacity at several scopes: per-process rlimits, service cgroups, node-wide PID and descriptor ceilings, and aggregate workload growth. Include normal peaks, deployment overlap, crash loops, batch bursts, and noisy-neighbor behavior rather than sizing only for steady state.
- Standardize defensible defaults with explicit workload overrides. A high process or descriptor limit is not free: each task and open file consumes kernel memory and operational attention, and broad unlimited settings can turn one leak into node-wide failure.
- Instrument utilization, growth rate, saturation events, and rejected work by cgroup and service. Couple alerts to user impact and headroom, then drill into ownership before raising a ceiling; many incidents require fixing fan-out, reaping, connection pooling, or retry behavior.
- Make capacity decisions a cross-team process with security, finance, and application owners. Test load shedding and recovery, document escalation thresholds, and continuously revise forecasts as runtime versions, tenant mix, and deployment patterns change.

## References

- [Linux kernel sysctl documentation](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html)
- [getrlimit(2): per-process resource limits](https://man7.org/linux/man-pages/man2/getrlimit.2.html)
- [cgroup v2: pids controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Free book: [Systems Performance, Second Edition companion](https://www.brendangregg.com/systems-performance-2nd-edition-book.html)
- Further reading (blog): [Brendan Gregg: Linux performance tools](https://www.brendangregg.com/blog/2015-12-03/linux-perf-tools-in-500-lines.html)

## What to learn next

- Official documentation: [Linux kernel sysctl docs](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html)
- Manual or specification: [Linux cgroup v2 pids controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Google SRE — capacity planning](https://sre.google/sre-book/addressing-cascading-failures/)
- Hands-on guide: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
