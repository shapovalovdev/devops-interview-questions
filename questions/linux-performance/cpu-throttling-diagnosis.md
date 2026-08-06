---
title: Diagnose cgroup CPU throttling
theme: linux-performance
difficulty: senior
type: troubleshooting
tags: [linux, performance, cpu, cgroups, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose cgroup CPU throttling

How can a service have low host CPU use but high latency from CPU limits?

## Answer guide

- Cgroup CPU bandwidth controls can throttle a group's runnable tasks after it consumes its configured quota in a period, even while other host CPUs are idle. Examine the effective cgroup settings, throttling statistics, per-thread CPU demand, and latency during the same interval.
- Confirm the runtime's conversion of requested CPU limits to cgroup values, then right-size demand from load tests and business objectives. Consider concurrency, burst behavior, CPU affinity, and noisy-neighbor protection when changing limits.
- Raising limits indiscriminately can break fair sharing and move saturation to the host. Aggregate CPU percent hides quota waiting, so do not dismiss a latency regression until cgroup accounting and scheduling delay have been checked.

## References

- [Linux kernel: cgroup v2 CPU controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [cgroup v2 CPU controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Manual or specification: [sched(7)](https://man7.org/linux/man-pages/man7/sched.7.html)
- Maintainer or personal blog: [Brendan Gregg — perf examples](https://www.brendangregg.com/perf.html)
- Technical blog: [Kubernetes Blog](https://kubernetes.io/blog/)
- Hands-on guide: [systemd resource control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html)
