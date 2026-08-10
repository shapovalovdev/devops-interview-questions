---
title: Design supervision for a multi-process application
theme: processes
difficulty: senior
type: scenario
tags: [linux, processes, systemd, pid1, reliability, must-know]
sources:
  - url: https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design supervision for a multi-process application

How should a platform supervise an application that creates web workers, schedulers, and short-lived helper processes?

## Answer guide

- Make ownership explicit: one supervisor owns the service lifecycle, each process role has a health and exit contract, and process groups/cgroups include all descendants. Avoid double supervision, where an application daemonizes while systemd or an orchestrator expects to track the foreground process.
- Define which exits should restart the whole service, one worker, or no component. Bound restart rates and surface a terminal failed state; otherwise a crash loop can consume resources and mask a persistent configuration or dependency error.
- Ensure the supervisor can stop and account for descendants. Systemd cgroups and configured kill behavior help, but applications that escape their cgroup or create detached work violate the contract and complicate rolling deployment.
- Test orphaned children, parent crashes, slow workers, SIGTERM, forced termination, reboot, and concurrent upgrade. Record process-tree and cgroup diagnostics in runbooks so responders do not kill an arbitrary wrapper.

## References

- [systemd.service: service process supervision](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- [systemd.kill: control process termination](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)
- [PR_SET_CHILD_SUBREAPER(2): child reaping](https://man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html)
- Free book: [systemd documentation](https://www.freedesktop.org/wiki/Software/systemd/)
- Further reading (blog): [Lennart Poettering: systemd process supervision](https://0pointer.net/blog/projects/systemd.html)

## What to learn next

- Official documentation: [systemd.service manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- Manual or specification: [systemd.kill manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)
- Maintainer or personal blog: [Lennart Poettering — systemd](https://0pointer.net/blog/projects/systemd.html)
- Technical blog: [systemd manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.html)
- Hands-on guide: [systemd project documentation](https://www.freedesktop.org/wiki/Software/systemd/)
