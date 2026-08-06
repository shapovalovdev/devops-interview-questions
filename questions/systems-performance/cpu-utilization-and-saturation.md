---
title: What is the difference between CPU utilization and CPU saturation?
theme: systems-performance
difficulty: junior
type: theory
tags: [linux, cpu, performance, monitoring]
sources:
  - url: https://www.brendangregg.com/usemethod.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# What is the difference between CPU utilization and CPU saturation?

## Answer guide

- CPU utilization is the percentage of time a CPU executes non-idle work. It answers whether capacity is busy, not whether runnable work is waiting.
- CPU saturation is queueing for CPU: runnable tasks wait because available CPUs cannot run them immediately. Linux load averages include runnable and uninterruptible tasks, so they are a clue, not a direct CPU-percent measure.
- Examine per-CPU imbalance, run-queue latency, throttling, and steal time before adding CPUs. A container CPU quota, lock contention, or I/O stalls can make a high load average misleading.

## References

- [Brendan Gregg: The USE Method](https://www.brendangregg.com/usemethod.html)
- [proc_loadavg kernel documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
- Further reading (blog): [Brendan Gregg — Linux Load Averages](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)

## What to learn next

- Official documentation: [Linux scheduler documentation](https://www.kernel.org/doc/html/latest/scheduler/index.html)
- Manual or specification: [uptime manual](https://man7.org/linux/man-pages/man1/uptime.1.html)
- Maintainer or personal blog: [Brendan Gregg — Linux Load Averages](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [perf scheduler analysis](https://www.brendangregg.com/perf.html)
