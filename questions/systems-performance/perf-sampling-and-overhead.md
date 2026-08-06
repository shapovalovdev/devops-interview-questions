---
title: How do you use sampling profilers without distorting production performance?
theme: systems-performance
difficulty: middle
type: scenario
tags: [linux, performance, debugging, monitoring]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you use sampling profilers without distorting production performance?

## Answer guide

- Define a narrow question, target process, time window, and acceptable overhead. Start with low-rate sampling and validate that request latency, CPU, and error rates remain within an agreed safety margin.
- Preserve symbol, build, kernel, and workload metadata so stacks are interpretable. Sampling estimates where time is spent; enough samples and representative traffic are needed before trusting a small percentage difference.
- Limit access to captured data and follow perf-event permission policy. High sample rates, system-wide tracing, unbounded stack collection, and debug logging can consume resources or expose sensitive workload details.

## References

- [Linux kernel: perf events security](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html)
- [perf-stat manual](https://man7.org/linux/man-pages/man1/perf-stat.1.html)
- Further reading (blog): [Brendan Gregg — perf Examples](https://www.brendangregg.com/perf.html)

## What to learn next

- Official documentation: [perf security](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html)
- Manual or specification: [perf stat manual](https://man7.org/linux/man-pages/man1/perf-stat.1.html)
- Maintainer or personal blog: [Brendan Gregg — perf](https://www.brendangregg.com/perf.html)
- Technical blog: [Netflix TechBlog](https://netflixtechblog.com/)
- Hands-on guide: [perf tutorial](https://perf.wiki.kernel.org/)
