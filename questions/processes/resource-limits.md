---
title: Diagnose a per-process resource limit
theme: processes
difficulty: middle
type: troubleshooting
tags: [linux, processes, limits, file-descriptors, capacity-planning, lfcs]
sources:
  - url: https://man7.org/linux/man-pages/man2/getrlimit.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose a per-process resource limit

An application reports “too many open files.” How do you determine the effective limit and apply a safe fix?

## Answer guide

- Check the failing process’s effective soft and hard `RLIMIT_NOFILE` values in `/proc/<pid>/limits`, then count and classify its descriptors. Shell `ulimit` reflects only the shell; PAM, systemd, containers, and application startup can impose different limits.
- Distinguish a legitimate capacity shortfall from a leak. Compare descriptor growth with requests, connection pools, log rotation, error paths, and restarts. Raising a limit without fixing an unbounded leak can postpone failure while increasing memory use and blast radius.
- Apply a durable limit at the owning supervisor or workload specification, with a staged rollout and rollback plan. Ensure child processes inherit the intended value and confirm system-wide ceilings such as `fs.file-max` are sufficient for aggregate demand.
- Alert before exhaustion using utilization and growth-rate signals, and include a runbook that captures evidence without leaking sensitive descriptor targets. Test the application’s behavior when it receives `EMFILE`.

## References

- [getrlimit(2): resource limits](https://man7.org/linux/man-pages/man2/getrlimit.2.html)
- [proc_pid_limits(5): process limits](https://man7.org/linux/man-pages/man5/proc_pid_limits.5.html)
- [systemd.resource-control: service resource controls](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html)
- Free book: [The Linux Documentation Project](https://tldp.org/)
- Further reading (blog): [Julia Evans: File descriptors](https://jvns.ca/blog/2020/10/20/what-even-is-a-file-descriptor/)

## What to learn next

- Official documentation: [man7 getrlimit(2)](https://man7.org/linux/man-pages/man2/getrlimit.2.html)
- Manual or specification: [man7 proc_pid_limits(5)](https://man7.org/linux/man-pages/man5/proc_pid_limits.5.html)
- Maintainer or personal blog: [Julia Evans — file descriptors](https://jvns.ca/blog/2020/10/20/what-even-is-a-file-descriptor/)
- Technical blog: [Red Hat — Linux processes](https://www.redhat.com/en/topics/linux/what-is-a-linux-process)
- Hands-on guide: [The Linux Documentation Project](https://tldp.org/)
