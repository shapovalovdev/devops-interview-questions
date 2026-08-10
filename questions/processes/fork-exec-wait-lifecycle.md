---
title: Explain the fork exec wait lifecycle
theme: processes
difficulty: middle
type: theory
tags: [linux, processes, debugging, systemd]
sources:
  - url: https://man7.org/linux/man-pages/man2/fork.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain the fork exec wait lifecycle

Explain how a Unix service commonly creates a child process and later observes its result.

## Answer guide

- `fork()` creates a child process with a new PID and copies of the parent’s process attributes; Linux uses copy-on-write so memory is not eagerly duplicated. The child often calls `execve()` to replace its program image, while the parent retains responsibility for supervision and reaping.
- `execve()` preserves some state but resets important attributes, including caught signal dispositions. It also replaces the address space, so code must set up arguments, environment, file descriptors, credentials, and any required signal policy deliberately before or after the boundary.
- The parent obtains termination or stop information through a `wait*` call. If it never waits, exited children can remain zombies; if it waits synchronously in the wrong place, it can stall service responsiveness. Supervisors should use a defined ownership and restart policy.
- Diagnose unexpected behavior by tracing the process tree and verifying which component forks, which execs, and which reaps. Framework behavior may differ from a simple shell example, especially for worker pools and systemd-managed services.

## References

- [fork(2): create a child process](https://man7.org/linux/man-pages/man2/fork.2.html)
- [execve(2): replace a process image](https://man7.org/linux/man-pages/man2/execve.2.html)
- [wait(2): collect child status](https://man7.org/linux/man-pages/man2/wait.2.html)
- Free book: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Lennart Poettering: systemd process supervision](https://0pointer.net/blog/projects/systemd.html)

## What to learn next

- Official documentation: [man7 fork(2)](https://man7.org/linux/man-pages/man2/fork.2.html)
- Manual or specification: [man7 execve(2)](https://man7.org/linux/man-pages/man2/execve.2.html)
- Maintainer or personal blog: [Lennart Poettering — systemd](https://0pointer.net/blog/projects/systemd.html)
- Technical blog: [Linux kernel proc filesystem documentation](https://docs.kernel.org/filesystems/proc.html)
- Hands-on guide: [Linux Journey — processes](https://linuxjourney.com/lesson/processes)
