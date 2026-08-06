---
title: Investigate a service that reports too many open files
theme: linux-troubleshooting
difficulty: middle
type: troubleshooting
tags: [linux, file-descriptors, limits, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man2/getrlimit.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a service that reports too many open files

## Answer guide

- Confirm whether the limit is per-process, per-user, or system-wide and inspect descriptor types: sockets, files, pipes, eventfds, and deleted files. Measure growth over time and request volume.
- Check the service manager's effective limit and application connection lifecycle. A higher limit only masks a descriptor leak or unbounded connection pool if the count grows without release.
- Fix ownership of descriptor lifecycle, apply a justified limit, and test under load. Avoid setting extreme global limits without capacity analysis because kernel memory and monitoring capacity also scale with descriptors.

## References

- [Primary Linux documentation](https://man7.org/linux/man-pages/man2/getrlimit.2.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

