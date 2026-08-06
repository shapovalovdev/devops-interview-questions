---
title: Respond to sustained swap activity
theme: linux-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, memory, troubleshooting, reliability, lfcs]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to sustained swap activity

What should an operator do when a latency-sensitive Linux workload starts swapping?

## Answer guide

- Establish whether swap-in or swap-out is sustained and correlate it with memory PSI, reclaim, major faults, cgroup limits, and request latency. Swap is a backing-store mechanism, but repeated paging can sharply reduce useful work when the working set exceeds RAM.
- Protect availability by reducing nonessential load, stopping a confirmed runaway consumer when safe, and ensuring headroom for the affected cgroup and host. Investigate allocation growth, cache policy, memory limits, and reclaim behavior before selecting a permanent change.
- Do not disable swap or raise memory blindly during an incident. Some systems use swap intentionally, while a no-swap host may invoke the OOM killer sooner; changing policy without a workload test can exchange latency for abrupt termination.

## References

- [Linux kernel: memory-management concepts](https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux memory documentation](https://www.kernel.org/doc/html/latest/admin-guide/mm/index.html)
- Manual or specification: [vmstat(8)](https://man7.org/linux/man-pages/man8/vmstat.8.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [proc_meminfo(5)](https://man7.org/linux/man-pages/man5/proc_meminfo.5.html)
