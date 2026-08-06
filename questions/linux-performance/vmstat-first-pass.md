---
title: Use vmstat for a first performance pass
theme: linux-performance
difficulty: junior
type: troubleshooting
tags: [linux, performance, cpu, memory, monitoring]
sources:
  - url: https://man7.org/linux/man-pages/man8/vmstat.8.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use vmstat for a first performance pass

What can `vmstat` tell you during an incident, and what must you verify next?

## Answer guide

- Sample `vmstat` over an interval, ignoring its since-boot first line, to inspect runnable and blocked tasks, swapping, block I/O, interrupts, context switches, and CPU time. It is a compact triage view, not a root-cause tool.
- Compare sustained changes with a known-good period and with the service timeline. High runnable work can justify per-CPU and per-process inspection; swap or I/O columns lead to memory or storage investigation.
- Counters are aggregated and may hide one device, cgroup, or process. Do not infer that a nonzero value is bad without rate, workload, and latency context, and avoid tuning from a single transient sample.

## References

- [vmstat(8): report virtual-memory statistics](https://man7.org/linux/man-pages/man8/vmstat.8.html)
- Further reading (blog): [Brendan Gregg — Linux Performance Tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux proc filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
- Manual or specification: [vmstat(8)](https://man7.org/linux/man-pages/man8/vmstat.8.html)
- Maintainer or personal blog: [Brendan Gregg — USE Method](https://www.brendangregg.com/usemethod.html)
- Technical blog: [Cloudflare Blog](https://blog.cloudflare.com/)
- Hands-on guide: [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)
