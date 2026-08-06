---
title: Choose between cron and systemd timers
theme: linux
difficulty: middle
type: scenario
tags: [linux, automation, reliability, lfcs]
sources:
  - url: https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose between cron and systemd timers

When is a systemd timer preferable to cron for a host task, and what reliability behavior must be designed explicitly?

## Answer guide

- Both can schedule host work. A systemd timer integrates with a service unit, dependency ordering, resource controls, identity, logs, and explicit missed-run behavior; cron remains suitable for simple, portable schedules where those controls are provided elsewhere.
- Decide whether missed intervals should run after downtime, whether overlapping invocations are safe, which timezone/calendar semantics apply, and where output and failures are observed. A schedule alone is not a delivery guarantee.
- Make the task idempotent, bound its runtime and concurrency, and monitor completion freshness and exit status. Test reboot, clock change, and dependency-unavailable cases.

## References

- [systemd.timer: timer unit semantics](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)
- Further reading: [crontab(5): cron table format](https://man7.org/linux/man-pages/man5/crontab.5.html)
- Further reading (blog): [Julien Enselme — systemd timers](https://www.jujens.eu/posts/en/2025/Feb/01/systemd-timers/)

## What to learn next

- Official documentation: [systemd.timer unit semantics](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)
- Manual or specification: [crontab(5) cron table format](https://man7.org/linux/man-pages/man5/crontab.5.html)
- Maintainer or personal blog: [Julien Enselme — systemd timers](https://www.jujens.eu/posts/en/2025/Feb/01/systemd-timers/)
- Technical blog: [LinuxBlog.io — systemd timers as a cron alternative](https://linuxblog.io/systemd-timers-alternative-cron-linux/)
- Hands-on guide: [FOSS Linux — scheduling tasks with systemd timers](https://www.fosslinux.com/48317/scheduling-tasks-systemd-timers-linux.htm)
