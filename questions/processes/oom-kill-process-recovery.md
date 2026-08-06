---
title: Recover safely after an OOM-killed process
theme: processes
difficulty: senior
type: troubleshooting
tags: [linux, processes, memory, oom, reliability, recovery]
sources:
  - url: https://www.kernel.org/doc/html/latest/mm/oom.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Recover safely after an OOM-killed process

A production process was killed for memory pressure. What do you verify before simply restarting it?

## Answer guide

- Confirm the event from kernel and supervisor evidence, including the killed process, cgroup or host scope, memory limit, pressure, and contemporaneous workload. An unexpected exit may have another cause, and the victim selected by the OOM killer is not necessarily the origin of pressure.
- Restore service deliberately: check replica capacity, data durability, in-flight job semantics, dependency health, and restart backoff. Restarting into the same exhausted cgroup can create a crash loop that amplifies load and erases useful evidence.
- Identify the control point—application retention, cache policy, concurrency, cgroup limit, node packing, or another workload—then make a bounded mitigation with monitoring. `oom_score_adj` influences selection but is not a substitute for correct capacity and memory limits.
- Preserve an incident record and add prevention signals: cgroup memory events, pressure stall information, allocation/growth metrics, and safe headroom. Test recovery and rollout behavior under constrained memory, not only on oversized development machines.

## References

- [Linux OOM handling documentation](https://www.kernel.org/doc/html/latest/mm/oom.html)
- [cgroup v2 memory controller](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- [proc_pid_oom_score_adj(5): OOM selection adjustment](https://man7.org/linux/man-pages/man5/proc_pid_oom_score_adj.5.html)
- Free book: [Linux kernel memory management documentation](https://www.kernel.org/doc/html/latest/mm/)
- Further reading (blog): [Brendan Gregg: Linux performance tools](https://www.brendangregg.com/blog/2015-12-03/linux-perf-tools-in-500-lines.html)

## What to learn next

- Official documentation: [Linux OOM documentation](https://www.kernel.org/doc/html/latest/mm/oom.html)
- Manual or specification: [man7 proc_pid_oom_score_adj(5)](https://man7.org/linux/man-pages/man5/proc_pid_oom_score_adj.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat — Linux performance](https://www.redhat.com/en/topics/linux/what-is-linux)
- Hands-on guide: [Linux kernel memory documentation](https://www.kernel.org/doc/html/latest/mm/)
