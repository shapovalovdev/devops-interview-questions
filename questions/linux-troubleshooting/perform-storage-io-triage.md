---
title: Perform first-pass storage I/O latency triage on Linux
theme: linux-troubleshooting
difficulty: senior
type: troubleshooting
tags: [linux, storage, io, latency, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/iostats.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Perform first-pass storage I/O latency triage on Linux

## Answer guide

- Define the latency symptom by device, operation, queue depth, filesystem, and workload. Combine application latency with block-device statistics, PSI, process state, and remote-storage telemetry to avoid blaming the nearest disk.
- Compare utilization, queueing, await-like latency, errors, flushes, and saturation against a healthy baseline. Account for caching and virtualization: low device counters do not exclude a network filesystem or cloud-volume control-plane issue.
- Reduce write amplification or concurrency, fail over where designed, and engage the storage owner with evidence. Do not run destructive filesystem repair or benchmark a saturated production volume during an incident.

## References

- [Primary Linux documentation](https://www.kernel.org/doc/html/latest/admin-guide/iostats.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

