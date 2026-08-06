---
title: How do you prove lock contention is causing an application latency regression?
theme: systems-performance
difficulty: senior
type: troubleshooting
tags: [linux, performance, debugging, monitoring]
sources:
  - url: https://www.kernel.org/doc/html/latest/locking/index.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you prove lock contention is causing an application latency regression?

## Answer guide

- Correlate latency with blocked or runnable threads, lock-wait duration, owner stacks, and workload concurrency. A hot function alone does not show that serialization, rather than useful work, is the limiter.
- Capture bounded stack or trace evidence around lock acquisition and contention, then compare a controlled concurrency or sharding change. Include kernel, runtime, and database locks when the request path crosses boundaries.
- Avoid blindly increasing threads: more contenders can worsen queueing and cache contention. Instrumentation can miss user-space locks or alter timings, so preserve uncertainty and verify the remedy with tail-latency and throughput results.

## References

- [Linux kernel locking documentation](https://www.kernel.org/doc/html/latest/locking/index.html)
- [perf-lock manual](https://man7.org/linux/man-pages/man1/perf-lock.1.html)
- Further reading (blog): [Brendan Gregg — Off-CPU Analysis](https://www.brendangregg.com/offcpuanalysis.html)

## What to learn next

- Official documentation: [Linux locking](https://www.kernel.org/doc/html/latest/locking/index.html)
- Manual or specification: [perf lock manual](https://man7.org/linux/man-pages/man1/perf-lock.1.html)
- Maintainer or personal blog: [Brendan Gregg — off-CPU analysis](https://www.brendangregg.com/offcpuanalysis.html)
- Technical blog: [Datadog Engineering](https://www.datadoghq.com/blog/engineering/)
- Hands-on guide: [perf tools](https://www.brendangregg.com/perf.html)
