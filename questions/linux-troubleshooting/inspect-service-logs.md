---
title: Inspect a Linux service that is failing after a restart
theme: linux-troubleshooting
difficulty: junior
type: troubleshooting
tags: [systemd, journald, logs, troubleshooting]
sources:
  - url: https://www.freedesktop.org/software/systemd/man/latest/journalctl.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Inspect a Linux service that is failing after a restart

## Answer guide

- Use `systemctl status` and a bounded `journalctl -u` time window to identify the unit, exit status, and first relevant error. Correlate the failure with configuration, package, permission, and dependency changes rather than treating the last log line as the cause.
- Inspect the effective unit with `systemctl cat` and `systemctl show`; check environment files, overrides, working directory, user, and dependent units. Reproduce safely with the service's normal account where possible.
- Do not repeatedly restart a flapping service or erase volatile evidence. Preserve logs and resource state, make one reversible change, then confirm recovery with a functional check as well as an active unit state.

## References

- [Primary Linux documentation](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)
