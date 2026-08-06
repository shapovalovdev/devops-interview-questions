---
title: Triage cgroup memory-limit failures
theme: linux-performance
difficulty: senior
type: troubleshooting
tags: [linux, performance, memory, cgroups, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage cgroup memory-limit failures

Why can a container be OOM-killed while the host still has memory available?

## Answer guide

- A cgroup memory boundary can constrain the workload independently of host-wide free or available RAM. Inspect the cgroup's configured `memory.max`, current usage, events, swap policy, process set, and the orchestrator's effective request and limit.
- Verify whether memory is anonymous, file cache, kernel-accounted, or a leak, then choose a measured change: reduce concurrency, fix allocation behavior, adjust a justified limit, or move workload placement. Test the limit under realistic burst and recovery conditions.
- A larger container limit can cause host pressure or evict other tenants, and an unlimited cgroup removes isolation. Do not rely on host dashboards alone; collection paths and cgroup version semantics must match the runtime.

## References

- [Linux kernel: cgroup v2 memory controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [cgroup v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Manual or specification: [proc_meminfo(5)](https://man7.org/linux/man-pages/man5/proc_meminfo.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Kubernetes Blog](https://kubernetes.io/blog/)
- Hands-on guide: [systemd resource control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html)
