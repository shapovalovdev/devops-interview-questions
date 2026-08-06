---
title: Investigate page-cache reclaim and memory pressure
theme: linux-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, memory, filesystem, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate page-cache reclaim and memory pressure

How can memory pressure degrade a file-serving workload before an OOM kill?

## Answer guide

- Memory pressure can force reclaim of page cache or anonymous pages, increasing fault, reclaim, writeback, and storage work before allocation failure occurs. Examine available memory, reclaim and fault rates, PSI, swap activity, cgroup events, and read latency together.
- Determine whether the pressure is host-wide or isolated to a cgroup, then reduce safe concurrency or memory demand, correct limits or leaks, and protect a tested working set. Validate the effect with a representative workload rather than only a lower cache figure.
- Page cache is normally beneficial, so “free memory” tuning is usually counterproductive. Reclaim counters alone do not prove a leak, and increasing a limit without capacity planning can move the failure to the host or another tenant.

## References

- [Linux kernel: memory-management concepts](https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux memory-management guide](https://www.kernel.org/doc/html/latest/admin-guide/mm/index.html)
- Manual or specification: [proc_meminfo(5)](https://man7.org/linux/man-pages/man5/proc_meminfo.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Meta Engineering](https://engineering.fb.com/)
- Hands-on guide: [Linux PSI documentation](https://www.kernel.org/doc/html/latest/accounting/psi.html)
