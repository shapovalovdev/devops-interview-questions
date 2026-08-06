---
title: Diagnose file-descriptor exhaustion
theme: linux-performance
difficulty: middle
type: troubleshooting
tags: [linux, performance, filesystem, troubleshooting, reliability]
sources:
  - url: https://man7.org/linux/man-pages/man2/getrlimit.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose file-descriptor exhaustion

How do you investigate “too many open files” in a Linux service?

## Answer guide

- Capture the failing process, error rate, effective soft and hard `RLIMIT_NOFILE`, system limits, and descriptor types. Inspect open files and sockets by process to distinguish a normal high-concurrency workload from a leak, stuck connections, or inherited descriptors.
- Mitigate safely by reducing unnecessary concurrency or draining a faulty instance, then repair lifecycle handling and set a capacity-backed limit. Add metrics for descriptor count, connection states, error responses, and restart behavior.
- Raising a limit can defer failure while consuming kernel memory or hiding leaks. A host-wide limit and a process limit differ, and containers or service managers may impose another layer, so validate the effective setting after deployment.

## References

- [getrlimit(2): resource limits including open files](https://man7.org/linux/man-pages/man2/getrlimit.2.html)
- Further reading (blog): [Brendan Gregg — Linux performance tools](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux proc filesystem](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
- Manual or specification: [getrlimit(2)](https://man7.org/linux/man-pages/man2/getrlimit.2.html)
- Maintainer or personal blog: [Brendan Gregg — performance tools](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [GitLab Handbook — infrastructure](https://handbook.gitlab.com/handbook/engineering/infrastructure/)
- Hands-on guide: [lsof manual](https://man7.org/linux/man-pages/man8/lsof.8.html)
