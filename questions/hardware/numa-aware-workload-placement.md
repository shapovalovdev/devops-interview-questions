---
title: Place a latency-sensitive workload on a NUMA server
theme: hardware
difficulty: senior
type: scenario
tags: [hardware, cpu, memory, virtualization, performance, reliability]
sources:
  - url: https://docs.kernel.org/mm/numa.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Place a latency-sensitive workload on a NUMA server

How do NUMA topology and placement affect a latency-sensitive workload?

## Answer guide

- A NUMA system has memory nodes with different access costs. Keep CPU execution, memory allocation, and where relevant device locality aligned when the workload is demonstrably sensitive to remote-memory latency.
- Inspect topology and actual memory placement, then test a representative workload before imposing affinity or memory policies.
- Over-pinning can strand capacity, reduce scheduler flexibility, and worsen failure recovery. Treat NUMA tuning as a measured optimization, not a universal default.

## References

- [Linux kernel NUMA memory policy documentation](https://docs.kernel.org/mm/numa.html)
- Further reading (blog): [Backblaze: Enterprise drive reliability](https://www.backblaze.com/blog/enterprise-drive-reliability/)

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
