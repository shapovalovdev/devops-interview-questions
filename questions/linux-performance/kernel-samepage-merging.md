---
title: Evaluate kernel samepage merging safely
theme: linux-performance
difficulty: senior
type: scenario
tags: [linux, performance, memory, virtualization, security]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/mm/ksm.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Evaluate kernel samepage merging safely

What trade-offs should a platform team evaluate before enabling Kernel Samepage Merging?

## Answer guide

- KSM can merge identical anonymous memory pages and reclaim duplicates, which can improve density for suitable workloads such as similar virtual machines. Evaluate actual deduplication opportunity, scanning CPU cost, memory pressure, and the platform's tenant isolation model.
- Test the exact kernel, workload mix, and operational controls in a nonproduction environment, then observe pages shared, pages scanned, CPU use, latency, and memory headroom. Document ownership, rollback, and the interaction with cgroups and migration.
- KSM is not free memory and may create performance or security concerns depending on deployment. Enabling it globally without evidence can waste CPU or create cross-workload implications; treat it as a capacity decision with explicit risk acceptance.

## References

- [Linux kernel: Kernel Samepage Merging](https://www.kernel.org/doc/html/latest/admin-guide/mm/ksm.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux KSM documentation](https://www.kernel.org/doc/html/latest/admin-guide/mm/ksm.html)
- Manual or specification: [cgroups(7)](https://man7.org/linux/man-pages/man7/cgroups.7.html)
- Maintainer or personal blog: [Brendan Gregg — memory performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Meta Engineering](https://engineering.fb.com/)
- Hands-on guide: [Linux memory management](https://www.kernel.org/doc/html/latest/admin-guide/mm/index.html)
