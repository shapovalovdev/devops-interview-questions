---
title: Distinguish a program from a process
theme: processes
difficulty: junior
type: theory
tags: [linux, processes, pid1, debugging]
sources:
  - url: https://man7.org/linux/man-pages/man5/proc.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish a program from a process

What is the difference between a program and a process on Linux, and why does that distinction matter during operations?

## Answer guide

- A program is executable content stored on disk; a process is one running instance of a program with a PID, address space, credentials, open files, environment, scheduling state, and kernel-visible metadata. One executable can therefore have many independent processes, while a process can replace its program image with `execve` without acquiring a new PID.
- Inspect the running instance rather than infer behavior from its binary name. `/proc/<pid>/` exposes command-line arguments, status, file descriptors, maps, limits, and namespaces, but access can be restricted by permissions or `hidepid` mount options. Container process views can also differ because a PID namespace changes what is visible.
- Operationally, deploy tooling must target the intended process identity and lifetime. Restarting a service may create a new PID, while a stale PID file can name an unrelated later process after PID reuse; a process manager or pidfd is safer than treating a number as a permanent identity.
- Do not equate a shell command with a single process: shells, supervisors, worker pools, and wrappers may create a process tree. Record the executable, arguments, parent, cgroup, and start time before intervening so the evidence survives a restart.

## References

- [proc(5): Linux process information pseudo-filesystem](https://man7.org/linux/man-pages/man5/proc.5.html)
- [execve(2): execute a program](https://man7.org/linux/man-pages/man2/execve.2.html)
- [pidfd_open(2): obtain a process file descriptor](https://man7.org/linux/man-pages/man2/pidfd_open.2.html)
- Free book: [The Linux Documentation Project](https://tldp.org/)
- Further reading (blog): [Brendan Gregg: Linux performance tools](https://www.brendangregg.com/blog/2015-12-03/linux-perf-tools-in-500-lines.html)

## What to learn next

- Official documentation: [man7 proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- Manual or specification: [Linux pid_namespaces(7)](https://man7.org/linux/man-pages/man7/pid_namespaces.7.html)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Linux kernel proc filesystem documentation](https://docs.kernel.org/filesystems/proc.html)
- Hands-on guide: [Linux Journey — processes](https://linuxjourney.com/lesson/processes)
