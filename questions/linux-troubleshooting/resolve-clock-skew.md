---
title: Resolve clock skew that is breaking Linux service authentication
theme: linux-troubleshooting
difficulty: middle
type: troubleshooting
tags: [linux, time, ntp, tls, troubleshooting]
sources:
  - url: https://www.freedesktop.org/software/systemd/man/latest/systemd-timesyncd.service.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Resolve clock skew that is breaking Linux service authentication

## Answer guide

- Confirm wall-clock offset, monotonic time behavior, timezone assumptions, and the authentication failure window. Certificates, tokens, distributed leases, and logs can fail differently when time moves backward or forward.
- Inspect the active time synchronization service, upstream reachability, virtualization time source, and any competing clock managers. Correct large offsets cautiously because a sudden step can disturb timers and ordered logs.
- Restore a single supported synchronization design, monitor offset and stratum/peer health, and revalidate authentication. Do not paper over skew by weakening certificate validation or widening token lifetime indefinitely.

## References

- [Primary Linux documentation](https://www.freedesktop.org/software/systemd/man/latest/systemd-timesyncd.service.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)
