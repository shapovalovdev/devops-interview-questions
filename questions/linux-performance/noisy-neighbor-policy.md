---
title: Design a noisy-neighbor performance policy
theme: linux-performance
difficulty: staff
type: scenario
tags: [linux, performance, cgroups, capacity-planning, governance]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a noisy-neighbor performance policy

How would you prevent one Linux workload from degrading shared-host tenants?

## Answer guide

- Define tenant classes, measurable fairness objectives, and the resource boundaries that enforce them: CPU, memory, I/O, PID, network, and placement controls. Cgroup v2 provides resource-control interfaces, but platform policy must specify defaults, exceptions, and who owns capacity.
- Instrument both host and cgroup pressure, throttling, OOM events, queueing, and user-facing outcomes. Rehearse isolation and eviction behavior, give tenants actionable limits and dashboards, and use exceptions with expiry and capacity review.
- Limits alone do not eliminate shared bottlenecks such as kernel work, NIC queues, storage devices, or cache. Overly tight controls can cause self-inflicted latency and retries, so validate fairness under mixed workloads and failure scenarios.

## References

- [Linux kernel: cgroup v2 resource control](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [cgroup v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Manual or specification: [cgroups(7)](https://man7.org/linux/man-pages/man7/cgroups.7.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Kubernetes Blog](https://kubernetes.io/blog/)
- Hands-on guide: [systemd resource control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html)
