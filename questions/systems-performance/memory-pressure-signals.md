---
title: Which signals distinguish memory use from memory pressure on Linux?
theme: systems-performance
difficulty: middle
type: troubleshooting
tags: [linux, memory, performance, monitoring]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Which signals distinguish memory use from memory pressure on Linux?

## Answer guide

- High used memory is normal when Linux uses otherwise idle memory for page cache. Diagnose pressure with reclaim activity, page faults, swap traffic, PSI, allocation failures, and OOM events rather than used memory alone.
- Check the process and cgroup view as well as the host. A container can hit its memory limit while the host has free memory, and file cache may be reclaimable while anonymous memory is not.
- Correlate pressure with latency and workload changes. Increasing a limit without finding a leak, cache growth, or concurrency problem can move the failure to the host or postpone an OOM kill.

## References

- [Linux kernel: memory management concepts](https://www.kernel.org/doc/html/latest/admin-guide/mm/concepts.html)
- [Linux kernel: pressure stall information](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Further reading (blog): [Brendan Gregg — Linux Memory Analysis](https://www.brendangregg.com/blog/2014-09-11/linux-page-cache-hit-ratio.html)

## What to learn next

- Official documentation: [Linux PSI documentation](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Manual or specification: [proc meminfo documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
- Maintainer or personal blog: [Brendan Gregg — page cache](https://www.brendangregg.com/blog/2014-09-11/linux-page-cache-hit-ratio.html)
- Technical blog: [Meta Engineering](https://engineering.fb.com/)
- Hands-on guide: [cgroup v2 memory controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
