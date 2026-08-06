---
title: Distinguish free memory from available memory
theme: linux-performance
difficulty: junior
type: theory
tags: [linux, performance, memory, monitoring]
sources:
  - url: https://man7.org/linux/man-pages/man5/proc_meminfo.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish free memory from available memory

Why can a healthy Linux host show little free memory?

## Answer guide

- Linux uses otherwise idle RAM for page cache and other reclaimable caches, so `MemFree` alone is not a capacity decision. `/proc/meminfo` exposes `MemAvailable` as an estimate of memory available for starting new applications without swapping.
- Evaluate available memory with page-fault, reclaim, swap, pressure-stall, and application-latency signals. Record the workload and cgroup limits because host-wide memory can look healthy while a container is near its own limit.
- Dropping caches or treating cache as waste commonly harms performance by forcing storage reads. Escalate when reclaim or swap is sustained, allocations fail, or latency rises; verify leaks and limits before simply increasing RAM.

## References

- [proc_meminfo(5): memory accounting fields](https://man7.org/linux/man-pages/man5/proc_meminfo.5.html)
- Further reading (blog): [Brendan Gregg — Linux Performance Tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux memory-management documentation](https://www.kernel.org/doc/html/latest/admin-guide/mm/index.html)
- Manual or specification: [proc_meminfo(5)](https://man7.org/linux/man-pages/man5/proc_meminfo.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Meta Engineering](https://engineering.fb.com/)
- Hands-on guide: [procps vmstat(8)](https://man7.org/linux/man-pages/man8/vmstat.8.html)
