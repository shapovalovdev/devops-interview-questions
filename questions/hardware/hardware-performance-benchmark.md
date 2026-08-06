---
title: Design a representative hardware performance benchmark
theme: hardware
difficulty: senior
type: scenario
tags: [hardware, cpu, storage, networking, capacity-planning, reliability]
sources:
  - url: https://sre.google/workbook/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a representative hardware performance benchmark

How do you compare two server platforms for a production workload?

## Answer guide

- Benchmark the real service or a validated workload model with production-like data shape, concurrency, storage, network, firmware, and observability; record tail latency and error behavior as well as throughput.
- Control variables, repeat runs, include warm-up and failure cases, and compare performance per cost, power, and rack resource rather than a synthetic CPU score alone.
- Publish assumptions and confidence bounds. A benchmark that excludes I/O, thermal behavior, or noisy-neighbor effects can select hardware that looks fast in a lab but regresses production SLOs.

## References

- [Google SRE Workbook: Monitoring distributed systems](https://sre.google/workbook/monitoring-distributed-systems/)
- Further reading (blog): [Backblaze: Enterprise drive reliability](https://www.backblaze.com/blog/enterprise-drive-reliability/)

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
