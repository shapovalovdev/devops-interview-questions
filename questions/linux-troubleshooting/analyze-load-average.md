---
title: Analyze a host with a high load average but low CPU utilization
theme: linux-troubleshooting
difficulty: middle
type: troubleshooting
tags: [linux, load, cpu, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Analyze a host with a high load average but low CPU utilization

## Answer guide

- Treat load average as runnable plus uninterruptible tasks, not CPU utilization. Inspect runnable threads, D-state tasks, disk/network latency, PSI, and cgroup throttling before scaling CPU.
- Use process state and stack evidence to find the blocked resource, then compare with a healthy host and recent deployments. Check virtual-machine steal time and remote filesystem dependencies when relevant.
- Do not tune scheduler parameters or add cores until the bottleneck is known. Mitigate with bounded concurrency, traffic reduction, or failing over a dependency, then confirm both latency and queue depth recover.

## References

- [Primary Linux documentation](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)
