---
title: Establish a platform-wide process lifecycle contract
theme: processes
difficulty: staff
type: scenario
tags: [linux, processes, platform-engineering, reliability, governance]
sources:
  - url: https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish a platform-wide process lifecycle contract

How would you set a platform-wide process lifecycle standard that improves reliability without forcing every team into one runtime?

## Answer guide

- Define outcome-oriented contracts: foreground ownership, identity, readiness, graceful termination, bounded shutdown, exit classification, log destination, resource limits, and child-process reaping. Publish runtime-specific adapters for systemd, containers, and batch workers rather than imposing one language or framework.
- Make adoption measurable through deployment checks and operational telemetry: shutdown completion, forced-kill rate, orphan/zombie count, restart-loop duration, limit failures, and fraction of services with a tested stop path. Allow time-bound exceptions with an accountable owner and compensating controls.
- Provide paved-road libraries and templates that correctly forward signals, expose health, manage workers, and avoid unsafe PID-file patterns. Teams should not have to rediscover subtle process semantics during an incident.
- Govern changes as reliability work: pilot representative workloads, test failure modes, document compatibility boundaries, and keep a rollback path. A standard that breaks legacy or regulated workloads without an escape hatch will be bypassed.

## References

- [systemd.service: service lifecycle model](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- [systemd.kill: shutdown controls](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)
- [signal(7): signal behavior](https://man7.org/linux/man-pages/man7/signal.7.html)
- Free book: [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/)
- Further reading (blog): [Lennart Poettering: systemd](https://0pointer.net/blog/projects/systemd.html)

## What to learn next

- Official documentation: [systemd.service manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- Manual or specification: [systemd.kill manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)
- Maintainer or personal blog: [Lennart Poettering — systemd](https://0pointer.net/blog/projects/systemd.html)
- Technical blog: [Google SRE — service management](https://sre.google/sre-book/table-of-contents/)
- Hands-on guide: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
