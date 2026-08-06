---
title: When are high context-switch rates a performance concern?
theme: systems-performance
difficulty: middle
type: troubleshooting
tags: [linux, cpu, performance, debugging]
sources:
  - url: https://www.kernel.org/doc/html/latest/scheduler/index.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# When are high context-switch rates a performance concern?

## Answer guide

- Context switches are normal when threads block, wake, preempt, or yield. Treat a high rate as an investigation lead only when it correlates with CPU overhead, run-queue latency, lock contention, or application latency.
- Split voluntary and involuntary switches, inspect thread counts and wakeup sources, then profile scheduling events if the signal persists. Excessively small work units, busy synchronization, and oversubscription are common explanations.
- Establish a workload baseline before changing thread pools or affinity. Reducing switches can harm fairness or I/O concurrency, and virtualization or kernel version differences can change the observed rate.

## References

- [Linux kernel scheduler documentation](https://www.kernel.org/doc/html/latest/scheduler/index.html)
- [getrusage manual](https://man7.org/linux/man-pages/man2/getrusage.2.html)
- Further reading (blog): [Brendan Gregg — Context Switches](https://www.brendangregg.com/blog/2014-12-31/the-hidden-costs-of-context-switches.html)

## What to learn next

- Official documentation: [Linux scheduler](https://www.kernel.org/doc/html/latest/scheduler/index.html)
- Manual or specification: [perf sched manual](https://man7.org/linux/man-pages/man1/perf-sched.1.html)
- Maintainer or personal blog: [Brendan Gregg — context switches](https://www.brendangregg.com/blog/2014-12-31/the-hidden-costs-of-context-switches.html)
- Technical blog: [Red Hat Performance Blog](https://www.redhat.com/en/blog/channel/performance)
- Hands-on guide: [perf tools](https://www.brendangregg.com/perf.html)
