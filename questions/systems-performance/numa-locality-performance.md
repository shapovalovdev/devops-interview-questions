---
title: How can NUMA locality cause a performance regression on a large host?
theme: systems-performance
difficulty: senior
type: scenario
tags: [linux, memory, cpu, performance]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/mm/numa_memory_policy.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How can NUMA locality cause a performance regression on a large host?

## Answer guide

- NUMA systems have memory nodes with different access costs. A workload can suffer when threads run on one node while frequently accessing memory allocated on another, even when total CPU and memory appear available.
- Inspect topology, CPU affinity, memory placement, migrations, and workload sharding. Test a placement change with representative traffic rather than assuming pinning is universally faster.
- Balance locality against scheduler flexibility, failover, and uneven utilization. Container placement, virtual-machine topology, transparent memory behavior, and hardware generation affect results, so document the tested environment.

## References

- [Linux kernel: NUMA memory policy](https://www.kernel.org/doc/html/latest/admin-guide/mm/numa_memory_policy.html)
- [numactl manual](https://man7.org/linux/man-pages/man8/numactl.8.html)
- Further reading (personal blog): [Brendan Gregg — Linux performance analysis in 60s](https://www.brendangregg.com/blog/2015-12-03/linux-perf-60s-video.html)

## What to learn next

- Official documentation: [Linux NUMA policy](https://www.kernel.org/doc/html/latest/admin-guide/mm/numa_memory_policy.html)
- Manual or specification: [numactl manual](https://man7.org/linux/man-pages/man8/numactl.8.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/blog/2015-12-03/linux-perf-60s-video.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Linux perf tools](https://www.brendangregg.com/perf.html)
