---
title: Interpret a high Linux load average
theme: linux
difficulty: middle
type: troubleshooting
tags: [linux, monitoring, troubleshooting, lfcs]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Interpret a high Linux load average

Why can a high load average be normal on one host and an incident on another?

## Answer guide

- Load is a count-like signal over time, not CPU utilization. On Linux it includes runnable work and tasks in uninterruptible sleep, so a storage stall can raise load without consuming all CPU.
- Compare it with the host's CPU count, normal workload pattern, request latency, run-queue pressure, CPU utilization, I/O latency, and blocked-task evidence. A batch host with a known queue can tolerate a value that would be an outage for a latency-sensitive API.
- Separate CPU saturation from I/O or memory pressure using process state, disk and network latency, and cgroup metrics where workloads are constrained. Do not “fix” load by restarting processes until the bottleneck and affected service objective are known.
- Alert on sustained load together with user impact or resource saturation; a single load threshold is a weak fleet-wide incident rule.

## References

- Further reading (blog): [Complementary linux practice article](https://www.redhat.com/en/blog/what-is-linux)
- [Linux kernel: cgroup v2 CPU and I/O controllers](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Further reading: [Linux proc filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html)

## What to learn next

- Official documentation: [Linux kernel administration guide](https://docs.kernel.org/admin-guide/)
- Manual or specification: [proc(5) Linux manual](https://man7.org/linux/man-pages/man5/proc.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance analysis](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
