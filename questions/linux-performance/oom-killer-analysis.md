---
title: Analyze a Linux OOM kill
theme: linux-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, memory, troubleshooting, incident-response]
sources:
  - url: https://www.kernel.org/doc/html/latest/mm/oom.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Analyze a Linux OOM kill

How do you investigate an out-of-memory termination on Linux?

## Answer guide

- Preserve kernel messages and the workload timeline, then identify whether the event was global or cgroup-scoped, which allocation failed, memory limits, swap policy, and the selected victim. The kernel OOM documentation describes its badness-based selection and relevant controls.
- Correlate memory growth, faults, reclaim, PSI, cgroup events, and recent deploys. Repair the leak, limit, concurrency, or capacity assumption; add actionable alerts and reproduce under a bounded representative load where possible.
- Do not assume the killed process caused the pressure or that `oom_score_adj` is a fix. Protecting a process can shift termination elsewhere, and restarting without addressing demand can create a crash loop and destroy incident evidence.

## References

- [Linux kernel: out-of-memory handling](https://www.kernel.org/doc/html/latest/mm/oom.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux OOM handling](https://www.kernel.org/doc/html/latest/mm/oom.html)
- Manual or specification: [proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux memory analysis](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Meta Engineering](https://engineering.fb.com/)
- Hands-on guide: [cgroup v2 memory controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
