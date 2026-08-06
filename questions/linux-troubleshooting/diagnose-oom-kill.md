---
title: Diagnose an OOM-killed service in a cgroup-aware host
theme: linux-troubleshooting
difficulty: middle
type: troubleshooting
tags: [linux, cgroups, oom, memory, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose an OOM-killed service in a cgroup-aware host

## Answer guide

- Read the kernel OOM report to identify the victim, allocation context, and whether the event occurred in a memory cgroup or at host scope. Preserve the unit/container limit, peak, and pressure data.
- Compare application heap, native allocations, page cache, child processes, and configured cgroup memory limits. A container can be killed while the host has apparently free memory because its cgroup limit is the boundary.
- Set realistic requests/limits and workload backpressure, then test under representative concurrency. Do not raise limits blindly: that can move the kill to another workload or exhaust the node.

## References

- [Primary Linux documentation](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

