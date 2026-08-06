---
title: Investigate a Linux hung-task warning or D-state process
theme: linux-troubleshooting
difficulty: senior
type: troubleshooting
tags: [linux, kernel, processes, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a Linux hung-task warning or D-state process

## Answer guide

- Capture the task state, kernel stack, blocked resource, and related storage/network signals. D-state often indicates uninterruptible waits, so a normal signal may not terminate the process until the kernel operation returns.
- Compare affected hosts and recent dependency changes, then identify the underlying device, filesystem, NFS, or driver path. Use bounded kernel diagnostics with operational approval because some collection has overhead or sensitive data.
- Restore or isolate the dependency and replace the node if it cannot recover safely. Do not force-reboot before preserving evidence unless user impact and the incident commander explicitly require it.

## References

- [Primary Linux documentation](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

