---
title: Investigate a process memory-growth incident
theme: processes
difficulty: senior
type: troubleshooting
tags: [linux, processes, memory, oom, performance, incident-response]
sources:
  - url: https://man7.org/linux/man-pages/man5/proc_pid_status.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a process memory-growth incident

How would you determine whether a process memory increase is a leak, cache growth, or a limit/accounting misunderstanding?

## Answer guide

- Establish the scope and accounting domain first: host versus cgroup, process versus process group, anonymous versus file-backed memory, and resident versus virtual address space. Values such as `VmRSS` are useful snapshots, but do not alone identify ownership or reclaimability.
- Build a time series around workload, deploys, request mix, cache behavior, garbage collection, and cgroup memory events. Compare process maps and allocator/application metrics where available; a stable cache with eviction behavior is different from monotonically retained unreachable allocations.
- Check the configured cgroup memory controls and the kernel’s OOM evidence before changing limits. Increasing a limit can protect one process while moving failure to its node or neighbors; a forced restart may restore capacity but loses diagnostic state.
- Mitigate based on impact: reduce concurrency or traffic, bound caches, roll back the triggering version, or add capacity. Then reproduce with representative load and define alerts on growth rate, memory pressure, and OOM events rather than a single RSS number.

## References

- [proc_pid_status(5): process memory fields](https://man7.org/linux/man-pages/man5/proc_pid_status.5.html)
- [cgroup v2 memory controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- [proc(5): memory and process information](https://man7.org/linux/man-pages/man5/proc.5.html)
- Free book: [Linux kernel memory management documentation](https://www.kernel.org/doc/html/latest/mm/)
- Further reading (blog): [Brendan Gregg: Linux memory analysis](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)

## What to learn next

- Official documentation: [man7 proc_pid_status(5)](https://man7.org/linux/man-pages/man5/proc_pid_status.5.html)
- Manual or specification: [Linux cgroup v2 memory controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat — Linux performance](https://www.redhat.com/en/topics/linux/what-is-linux)
- Hands-on guide: [Linux kernel memory documentation](https://www.kernel.org/doc/html/latest/mm/)
