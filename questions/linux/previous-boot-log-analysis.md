---
title: Investigate a failure that occurred only during the previous boot
theme: linux
difficulty: middle
type: troubleshooting
tags: [linux, debugging, troubleshooting]
sources:
  - url: https://www.freedesktop.org/software/systemd/man/latest/journalctl.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a failure that occurred only during the previous boot

A host is healthy now but failed to start a dependency during its prior boot. How do you collect evidence without confusing it with current state?

## Answer guide

- Select the previous boot explicitly when querying the journal, and inspect both kernel and affected-unit records around the first failure. Record the boot ID, image/kernel version, unit result, and timestamp so later analysis is reproducible.
- Compare the previous boot's configuration, mounts, network readiness, and dependency ordering with the successful boot. A current `systemctl status` describes current state and can hide a transient startup race or a unit that was manually restarted.
- Preserve relevant logs before retention removes them, then repair the dependency, ordering, retry, or environmental cause. Test a controlled reboot and monitor the startup path; do not mark the issue resolved solely because a later boot succeeded.

## References

- [journalctl: select records by boot](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html)
- Further reading: [systemd: manager and unit concepts](https://www.freedesktop.org/software/systemd/man/latest/systemd.html)
