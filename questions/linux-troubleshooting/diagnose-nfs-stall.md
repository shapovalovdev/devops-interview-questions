---
title: Diagnose an application stalled on an NFS mount
theme: linux-troubleshooting
difficulty: senior
type: troubleshooting
tags: [linux, nfs, storage, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man5/nfs.5.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose an application stalled on an NFS mount

## Answer guide

- Confirm the path is NFS and collect mount options, server/export health, RPC reachability, client retransmissions, and tasks blocked in filesystem calls. An application timeout may be downstream of an NFS retry policy.
- Compare another client and a direct server-side check, then assess network path, DNS, identity mapping, and server capacity. Mount options such as `hard`, timeouts, and protocol version carry data-integrity and availability trade-offs.
- Use a designed failover or maintenance procedure and communicate that I/O may block. Do not change a data workload from hard to soft semantics casually; soft failures can surface as application-level I/O errors and corruption risk.

## References

- [Primary Linux documentation](https://man7.org/linux/man-pages/man5/nfs.5.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

