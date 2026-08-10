---
title: Choose a signal for a running process
theme: processes
difficulty: junior
type: theory
tags: [linux, processes, signals, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man7/signal.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a signal for a running process

When would you use SIGTERM, SIGKILL, and SIGHUP, and what risks do they carry?

## Answer guide

- SIGTERM requests termination and can be caught so an application drains work, closes resources, and exits. SIGKILL cannot be caught, blocked, or ignored; it stops a task without cleanup. Use SIGKILL only after the intended identity and a bounded graceful-shutdown attempt have been verified.
- SIGHUP has a historical terminal meaning; applications may choose to treat it as reload, terminate, or ignore it. Never assume a reload semantic from the signal name: consult the service documentation and confirm whether it atomically validates and applies its configuration.
- Send a signal through the service manager when it owns the process, because it understands the service cgroup and configured stop behavior. A raw `kill PID` can affect only a wrapper, miss workers, or target a reused PID.
- Record why and when a forceful signal was sent. SIGKILL can interrupt writes, leave partial external work, and conceal deadlock or I/O causes; follow it with recovery validation and root-cause investigation.

## References

- [signal(7): dispositions and delivery](https://man7.org/linux/man-pages/man7/signal.7.html)
- [kill(2): send a signal](https://man7.org/linux/man-pages/man2/kill.2.html)
- [systemctl kill: signal service processes](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
- Free book: [Advanced Bash-Scripting Guide: signals](https://www.gnu.org/software/bash/manual/html_node/Signals.html)
- Further reading (blog): [Lennart Poettering: systemd for administrators](https://0pointer.net/blog/projects/systemd.html)

## What to learn next

- Official documentation: [man7 signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html)
- Manual or specification: [man7 kill(2)](https://man7.org/linux/man-pages/man2/kill.2.html)
- Maintainer or personal blog: [Lennart Poettering — systemd](https://0pointer.net/blog/projects/systemd.html)
- Technical blog: [Red Hat — Linux signals](https://www.redhat.com/en/blog/linux-signals)
- Hands-on guide: [Advanced Bash-Scripting Guide — signals](https://www.gnu.org/software/bash/manual/html_node/Signals.html)
