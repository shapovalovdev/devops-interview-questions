---
title: Triage a hung process without destroying evidence
theme: processes
difficulty: middle
type: troubleshooting
tags: [linux, processes, debugging, incident-response, logs]
sources:
  - url: https://man7.org/linux/man-pages/man1/strace.1.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a hung process without destroying evidence

A process accepts no work but remains alive. What is your safe investigation sequence?

## Answer guide

- Establish impact and ownership first: determine whether the process is the service, a worker, or a supervisor; check health endpoints, queue depth, and redundant capacity. Do not restart a broadly shared component before deciding whether traffic can be drained or isolated.
- Capture low-risk evidence in increasing order of intrusion: service status and logs, process state and wait channel, resource and pressure metrics, open descriptors and sockets, then a short bounded syscall trace or stack capture if policy permits. Multiple samples distinguish a stable wait from a transient one.
- Interpret the observed wait with its dependency. A blocked `read`, DNS lookup, lock, filesystem call, or full pipe points to a different owner and remediation. A tracer changes timing and can be prohibited for sensitive workloads, so use a change record and stop condition.
- Recover with the least disruptive method—restore a dependency, drain and restart one instance, or roll back a change—then verify requests, background work, and data consistency. Preserve artifacts for the post-incident review.

## References

- [strace(1): trace system calls and signals](https://man7.org/linux/man-pages/man1/strace.1.html)
- [proc(5): process information](https://man7.org/linux/man-pages/man5/proc.5.html)
- [Linux PSI documentation](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- Free book: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg: Linux performance tools](https://www.brendangregg.com/blog/2015-12-03/linux-perf-tools-in-500-lines.html)

## What to learn next

- Official documentation: [man7 strace(1)](https://man7.org/linux/man-pages/man1/strace.1.html)
- Manual or specification: [man7 proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat — Linux performance](https://www.redhat.com/en/topics/linux/what-is-linux)
- Hands-on guide: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
