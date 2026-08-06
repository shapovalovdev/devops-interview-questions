---
title: Build a hardware capacity baseline
theme: hardware
difficulty: middle
type: scenario
tags: [hardware, capacity-planning, monitoring, reliability]
sources:
  - url: https://sre.google/sre-book/handling-overload/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build a hardware capacity baseline

What measurements do you need to decide whether a physical server fleet has enough capacity?

## Answer guide

- Measure service demand and headroom alongside CPU time, runnable work, memory pressure, storage latency/queueing, network throughput/errors, power, thermal state, and failure-domain capacity.
- Use peak and failure scenarios, not fleet averages: capacity must cover maintenance, a host or rack loss, and growth within the lead time to procure and deploy hardware.
- Define saturation and latency thresholds per workload and revisit forecasts after architecture or traffic changes. Buying for CPU alone can leave storage, memory, cooling, or network as the limiting resource.

## References

- [Google SRE Book: Handling overload](https://sre.google/sre-book/handling-overload/)
- Further reading (blog): [Backblaze: Enterprise drive reliability](https://www.backblaze.com/blog/enterprise-drive-reliability/)

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
