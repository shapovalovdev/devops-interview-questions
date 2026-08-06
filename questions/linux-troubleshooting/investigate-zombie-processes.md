---
title: Investigate accumulating zombie processes on Linux
theme: linux-troubleshooting
difficulty: middle
type: troubleshooting
tags: [linux, processes, pid1, troubleshooting]
sources:
  - url: https://man7.org/linux/man-pages/man2/wait.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate accumulating zombie processes on Linux

## Answer guide

- Confirm the process state is `Z` and identify its parent. A zombie has exited and holds only an exit status; it consumes a PID, while an uninterruptible or runaway process has a different remediation path.
- Find the parent or supervising runtime that is failing to call `wait(2)`, including PID 1 behavior inside a container. Restart or repair the reaper only after considering its child processes and service impact.
- Fix child-reaping in the application or init wrapper and monitor PID growth. Killing a zombie itself is ineffective; only its parent can reap it, or init adopts and reaps it after the parent exits.

## References

- [Primary Linux documentation](https://man7.org/linux/man-pages/man2/wait.2.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

