---
title: Investigate excess context switching
theme: linux-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, cpu, debugging, monitoring]
sources:
  - url: https://man7.org/linux/man-pages/man8/vmstat.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate excess context switching

When are context switches a performance problem, and how do you investigate them?

## Answer guide

- Treat context-switch rate as a symptom: compare it per request and against a baseline, then identify the involved threads, run queues, blocking calls, interrupts, and wakeup patterns. `vmstat` can expose aggregate context switches but cannot identify their cause.
- Use targeted scheduler tracing or profiling with bounded duration to distinguish useful I/O blocking from lock contention, thread-pool churn, busy polling, or excessive concurrency. Correlate findings with CPU migration and tail latency.
- A high rate is not inherently harmful; event-driven and I/O-heavy workloads can switch frequently. Do not tune kernel scheduler knobs first, and avoid invasive tracing on an overloaded production host without an overhead and data-handling plan.

## References

- [vmstat(8): context-switch statistics](https://man7.org/linux/man-pages/man8/vmstat.8.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux scheduler documentation](https://www.kernel.org/doc/html/latest/scheduler/index.html)
- Manual or specification: [vmstat(8)](https://man7.org/linux/man-pages/man8/vmstat.8.html)
- Maintainer or personal blog: [Brendan Gregg — performance tools](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [perf sched](https://www.brendangregg.com/perf.html)
