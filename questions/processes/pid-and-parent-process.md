---
title: Explain PIDs and parent processes
theme: processes
difficulty: junior
type: theory
tags: [linux, processes, pid1, debugging]
sources:
  - url: https://man7.org/linux/man-pages/man2/getpid.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain PIDs and parent processes

What are PID and PPID, and what happens when a parent process exits before its child?

## Answer guide

- A PID identifies a process within its PID namespace and PPID identifies its current parent. The kernel exposes both in `/proc/<pid>/status`; process IDs are namespace-relative, so a container may call itself PID 1 while the host sees another PID.
- A child normally begins with its creator as parent. If that parent exits, Linux reparents the child to a suitable subreaper or the namespace init process, which must eventually collect terminated descendants. Reparenting does not itself terminate a child or transfer application-level ownership.
- Investigate a surprising PPID with `ps -o pid,ppid,stat,cmd`, `/proc/<pid>/status`, and the service/cgroup owner. A short-lived shell wrapper commonly explains children attached to systemd or an init process after the wrapper has exited.
- Avoid using a PID or PPID alone as an authorization or health signal. PID values are reused, and namespace translation can make host and container observations differ; combine identity with start time, executable, cgroup, and supervisor state.

## References

- [getpid(2): process identifiers](https://man7.org/linux/man-pages/man2/getpid.2.html)
- [pid_namespaces(7): PID isolation and namespace init](https://man7.org/linux/man-pages/man7/pid_namespaces.7.html)
- [PR_SET_CHILD_SUBREAPER(2): adopt orphaned descendants](https://man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html)
- Free book: [Linux kernel process management documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Lennart Poettering: The new world of Linux process supervision](https://0pointer.net/blog/projects/systemd.html)

## What to learn next

- Official documentation: [man7 getpid(2)](https://man7.org/linux/man-pages/man2/getpid.2.html)
- Manual or specification: [Linux pid_namespaces(7)](https://man7.org/linux/man-pages/man7/pid_namespaces.7.html)
- Maintainer or personal blog: [Lennart Poettering — systemd](https://0pointer.net/blog/projects/systemd.html)
- Technical blog: [Linux kernel proc filesystem documentation](https://docs.kernel.org/filesystems/proc.html)
- Hands-on guide: [Linux Journey — process details](https://linuxjourney.com/lesson/process-details)
