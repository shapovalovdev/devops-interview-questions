---
title: Investigate a growing CPU run queue
theme: linux-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, cpu, monitoring, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/scheduler/sched-nice-design.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a growing CPU run queue

How would you triage sustained runnable-task growth on a Linux host?

## Answer guide

- Confirm sustained runnable work with interval metrics, then inspect per-CPU usage, process and thread CPU, affinity, cgroup CPU limits, steal time, and request rate. A run queue means work wants CPU; it does not establish why it cannot receive it.
- Separate hot application code from scheduler imbalance, throttling, interrupt load, virtualization contention, and retry amplification. Collect profiles or stack samples only after bounding their overhead and correlating them with the affected service interval.
- Do not use a single run-queue threshold for every machine. Core count, workload parallelism, latency objectives, and CPU frequency vary; increasing concurrency can worsen queueing and tail latency when the bottleneck is already saturated.

## References

- [Linux kernel: scheduler design](https://www.kernel.org/doc/html/latest/scheduler/sched-nice-design.html)
- Further reading (blog): [Brendan Gregg — The Linux Scheduler](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)

## What to learn next

- Official documentation: [Linux scheduler documentation](https://www.kernel.org/doc/html/latest/scheduler/index.html)
- Manual or specification: [sched(7)](https://man7.org/linux/man-pages/man7/sched.7.html)
- Maintainer or personal blog: [Brendan Gregg — perf examples](https://www.brendangregg.com/perf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [perf sched](https://www.brendangregg.com/perf.html)
