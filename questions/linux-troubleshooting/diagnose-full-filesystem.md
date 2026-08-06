---
title: Diagnose a Linux filesystem reported as full
theme: linux-troubleshooting
difficulty: junior
type: troubleshooting
tags: [linux, filesystem, disk, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man1/df.1.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose a Linux filesystem reported as full

## Answer guide

- Compare `df` with `du` on the affected mount, including inode consumption with `df -i`. A full block device, exhausted inodes, a hidden mount, and a quota problem need different remedies.
- Find unexpectedly large paths with one-filesystem boundaries and identify deleted-but-open files through `lsof +L1`. Truncating a live log without understanding its writer can cause data loss or repeated growth.
- Free or extend capacity using the service retention policy, then validate space, inode headroom, and application writes. Avoid deleting unknown files in system directories or assuming a container view is the host mount namespace.

## References

- [Primary Linux documentation](https://man7.org/linux/man-pages/man1/df.1.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

