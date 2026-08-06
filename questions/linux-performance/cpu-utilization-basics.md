---
title: Read CPU utilization before tuning
theme: linux-performance
difficulty: junior
type: troubleshooting
tags: [linux, performance, cpu, monitoring, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man1/top.1.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Read CPU utilization before tuning

How do you decide whether a Linux host is CPU-bound?

## Answer guide

- Establish the affected interval and workload, then examine CPU time by user, system, idle, iowait, steal, and interrupt context with tools such as `top`, `mpstat`, or `/proc/stat`. Relate host counters to request rate and latency rather than treating one high sample as proof.
- Check per-CPU balance and the busiest processes or threads. A machine can have spare aggregate CPU while one pinned thread, IRQ, run queue, quota, or NUMA placement creates latency for the workload.
- High CPU is not automatically the fault: it may be useful work, a retry storm, or a downstream wait pattern. Avoid changing scheduler settings or adding cores before capturing a baseline and ruling out I/O, throttling, and application lock contention.

## References

- [top(1): task and CPU summary fields](https://man7.org/linux/man-pages/man1/top.1.html)
- Further reading (blog): [Brendan Gregg — Linux Performance Tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux CPU scheduler documentation](https://www.kernel.org/doc/html/latest/scheduler/index.html)
- Manual or specification: [top(1)](https://man7.org/linux/man-pages/man1/top.1.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Linux perf tools](https://www.brendangregg.com/perf.html)
