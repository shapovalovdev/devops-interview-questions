---
title: Control file descriptor inheritance across exec
theme: processes
difficulty: middle
type: theory
tags: [linux, processes, file-descriptors, security]
sources:
  - url: https://man7.org/linux/man-pages/man2/open.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Control file descriptor inheritance across exec

Why can an inherited file descriptor cause an availability or security incident, and how do you prevent it?

## Answer guide

- A child normally inherits copies of its parent’s open file descriptors across `fork`; descriptors survive `execve` unless marked close-on-exec. An unintended inherited listening socket, pipe end, log file, or secret-bearing descriptor can keep a resource alive or expose a capability to a helper program.
- Create descriptors with `O_CLOEXEC` where available, or set `FD_CLOEXEC` immediately and safely. In multithreaded code, separate `fcntl` calls can race with a concurrent fork-and-exec, which is why atomic close-on-exec creation flags matter.
- Investigate leaks by comparing `/proc/<pid>/fd` and `/proc/<pid>/fdinfo` over time, counting descriptors by type and owner. Do not expose this data casually because targets and command lines can reveal credentials, sockets, or customer paths.
- Test process replacement and restart paths, not only normal requests. A descriptor leak can exhaust `RLIMIT_NOFILE`, delay TCP connection closure, or prevent a rolling restart from releasing a port.

## References

- [open(2): O_CLOEXEC and descriptor creation](https://man7.org/linux/man-pages/man2/open.2.html)
- [fcntl(2): FD_CLOEXEC](https://man7.org/linux/man-pages/man2/fcntl.2.html)
- [proc_pid_fd(5): open file descriptors](https://man7.org/linux/man-pages/man5/proc_pid_fd.5.html)
- Free book: [The Linux Programming Interface resources](https://man7.org/tlpi/)
- Further reading (blog): [Julia Evans: A few ways to learn about Linux file descriptors](https://jvns.ca/blog/2020/10/20/what-even-is-a-file-descriptor/)

## What to learn next

- Official documentation: [man7 open(2)](https://man7.org/linux/man-pages/man2/open.2.html)
- Manual or specification: [man7 fcntl(2)](https://man7.org/linux/man-pages/man2/fcntl.2.html)
- Maintainer or personal blog: [Julia Evans — file descriptors](https://jvns.ca/blog/2020/10/20/what-even-is-a-file-descriptor/)
- Technical blog: [Red Hat — Linux processes](https://www.redhat.com/en/topics/linux/what-is-a-linux-process)
- Hands-on guide: [The Linux Programming Interface resources](https://man7.org/tlpi/)
