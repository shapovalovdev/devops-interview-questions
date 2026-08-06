---
title: How do you investigate an OOM-killer incident without treating the kill as the root cause?
theme: systems-performance
difficulty: middle
type: troubleshooting
tags: [linux, memory, incident-response, performance]
sources:
  - url: https://www.kernel.org/doc/html/latest/mm/oom.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# How do you investigate an OOM-killer incident without treating the kill as the root cause?

## Answer guide

- Preserve kernel logs, cgroup events, memory limits, process maps, and workload history. Determine whether the global kernel OOM killer or a cgroup limit event selected the process; their scope and remediation differ.
- Identify the allocation class and growth pattern: anonymous heap, page cache, tmpfs, kernel memory, or a leak. Examine concurrency and restart loops because repeated recovery can hide continued demand.
- Restore service with safe limits or load shedding, then test a specific root-cause hypothesis. Disabling OOM handling or simply raising limits risks host-wide failure; priority adjustments influence selection but do not create memory.

## References

- [Linux kernel: out of memory handling](https://www.kernel.org/doc/html/latest/mm/oom.html)
- [Linux kernel: cgroup v2 memory controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Further reading (personal blog): [Brendan Gregg — Analyzing a High Rate of Paging](https://www.brendangregg.com/blog/2021-08-30/high-rate-of-paging.html)

## What to learn next

- Official documentation: [Linux OOM handling](https://www.kernel.org/doc/html/latest/mm/oom.html)
- Manual or specification: [systemd-oomd manual](https://www.freedesktop.org/software/systemd/man/latest/systemd-oomd.service.html)
- Maintainer or personal blog: [Brendan Gregg — memory-pressure investigation](https://www.brendangregg.com/blog/2021-08-30/high-rate-of-paging.html)
- Technical blog: [Elastic Blog](https://www.elastic.co/blog/)
- Hands-on guide: [Kubernetes resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
