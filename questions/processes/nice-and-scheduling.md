---
title: Use nice values without promising performance
theme: processes
difficulty: middle
type: theory
tags: [linux, processes, cpu, performance, limits]
sources:
  - url: https://man7.org/linux/man-pages/man7/sched.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use nice values without promising performance

What does a nice value change, and when is it the wrong tool for protecting a production service?

## Answer guide

- Nice is a scheduling priority input for normal scheduling policies; lower nice generally gives a task more favorable CPU scheduling treatment. It is not a CPU limit, reservation, latency guarantee, or I/O control, and effects depend on the scheduler, contention, cgroups, and privileges.
- Use it for cooperative batch work where reduced CPU preference is acceptable. Do not claim it protects a latency-sensitive service from a runaway peer: the peer can still consume memory, file descriptors, I/O bandwidth, network queues, or CPU when no alternative work is runnable.
- Prefer cgroup resource controls, quotas, weights, admission limits, and workload isolation for enforceable multi-tenant policy. Configure them through the service manager or orchestrator so restarts and descendants remain in scope.
- Validate with workload-specific latency and throughput tests. Changing priority can hide a capacity problem, starve background maintenance, or create confusing behavior across distributions and container runtimes.

## References

- [sched(7): Linux scheduling policies](https://man7.org/linux/man-pages/man7/sched.7.html)
- [nice(2): change process priority](https://man7.org/linux/man-pages/man2/nice.2.html)
- [cgroup v2 CPU controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Free book: [Linux kernel scheduler documentation](https://www.kernel.org/doc/html/latest/scheduler/)
- Further reading (blog): [Brendan Gregg: CPU utilization is wrong](https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html)

## What to learn next

- Official documentation: [man7 sched(7)](https://man7.org/linux/man-pages/man7/sched.7.html)
- Manual or specification: [Linux cgroup v2 CPU controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Brendan Gregg — CPU utilization](https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html)
- Technical blog: [Red Hat — Linux performance](https://www.redhat.com/en/topics/linux/what-is-linux)
- Hands-on guide: [Linux kernel scheduler docs](https://www.kernel.org/doc/html/latest/scheduler/)
