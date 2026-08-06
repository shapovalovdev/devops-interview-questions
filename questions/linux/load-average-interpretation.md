---
title: Interpret a high Linux load average
theme: linux
difficulty: middle
type: troubleshooting
tags: [linux, monitoring, troubleshooting]
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

- [Linux kernel: cgroup v2 CPU and I/O controllers](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Further reading: [Linux proc filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
