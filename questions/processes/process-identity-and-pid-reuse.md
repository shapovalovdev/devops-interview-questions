---
title: Avoid PID-reuse errors in automation
theme: processes
difficulty: senior
type: scenario
tags: [linux, processes, automation, security, debugging]
sources:
  - url: https://man7.org/linux/man-pages/man2/pidfd_open.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Avoid PID-reuse errors in automation

Why is `kill $(cat pidfile)` unsafe by itself, and how would you make process-control automation safer?

## Answer guide

- PIDs are finite identifiers that can be reused after a process exits. A stale PID file can therefore identify an unrelated process, especially on busy hosts or after a failed restart; sending a signal based only on that number can create an outage or security incident.
- Prefer the owning service manager’s unit identity and cgroup-aware operations. When application code needs a stable kernel reference, use pidfds where the supported kernel and runtime permit them, and verify the executable, start time, credentials, namespace, and command contract before acting.
- Treat PID files as advisory compatibility artifacts. Create them atomically with correct ownership, remove them on clean shutdown, validate their contents, and never trust a writable path supplied by an unprivileged user.
- Design automation with dry-run evidence, least privilege, audit logging, confirmation of post-action state, and rollback or escalation criteria. A safe script must handle races, restarts, containers, and a process that exits between inspection and action.

## References

- [pidfd_open(2): process file descriptors](https://man7.org/linux/man-pages/man2/pidfd_open.2.html)
- [pidfd_send_signal(2): signal by pidfd](https://man7.org/linux/man-pages/man2/pidfd_send_signal.2.html)
- [systemctl: manage units](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
- Free book: [Secure Programming HOWTO](https://tldp.org/HOWTO/Secure-Programs-HOWTO/)
- Further reading (blog): [Lennart Poettering: systemd](https://0pointer.net/blog/projects/systemd.html)

## What to learn next

- Official documentation: [man7 pidfd_open(2)](https://man7.org/linux/man-pages/man2/pidfd_open.2.html)
- Manual or specification: [man7 pidfd_send_signal(2)](https://man7.org/linux/man-pages/man2/pidfd_send_signal.2.html)
- Maintainer or personal blog: [Lennart Poettering — systemd](https://0pointer.net/blog/projects/systemd.html)
- Technical blog: [Red Hat — Linux processes](https://www.redhat.com/en/topics/linux/what-is-a-linux-process)
- Hands-on guide: [Secure Programming HOWTO](https://tldp.org/HOWTO/Secure-Programs-HOWTO/)
