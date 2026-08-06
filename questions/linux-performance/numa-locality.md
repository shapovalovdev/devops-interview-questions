---
title: Recognize NUMA locality as a performance constraint
theme: linux-performance
difficulty: senior
type: scenario
tags: [linux, performance, cpu, memory, capacity-planning]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/mm/numa_memory_policy.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Recognize NUMA locality as a performance constraint

When should a Linux performance investigation consider NUMA placement?

## Answer guide

- Consider NUMA when a multi-socket or multi-node machine has memory-heavy or latency-sensitive work with uneven CPU use, remote-memory access, or inconsistent per-thread performance. Linux NUMA policy controls where a process allocates memory, but defaults and topology matter.
- Measure topology, CPU affinity, memory placement, remote versus local access indicators, and workload performance before changing policy. Keep threads and their frequently accessed memory close where tests demonstrate a material gain.
- Binding can reduce scheduling flexibility and cause local-node exhaustion. Do not copy a tuning profile across hardware or virtual machines; validate failover, memory growth, and tail latency under realistic load.

## References

- [Linux kernel: NUMA memory policy](https://www.kernel.org/doc/html/latest/admin-guide/mm/numa_memory_policy.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux NUMA memory policy](https://www.kernel.org/doc/html/latest/admin-guide/mm/numa_memory_policy.html)
- Manual or specification: [numactl(8)](https://man7.org/linux/man-pages/man8/numactl.8.html)
- Maintainer or personal blog: [Brendan Gregg — performance analysis](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [numa_maps documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
