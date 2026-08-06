---
title: Design guardrails for automated process remediation
theme: processes
difficulty: staff
type: scenario
tags: [linux, processes, automation, incident-response, reliability]
sources:
  - url: https://man7.org/linux/man-pages/man2/pidfd_send_signal.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design guardrails for automated process remediation

How would you automate remediation for unhealthy processes while minimizing the chance that automation worsens an incident?

## Answer guide

- Automate only a narrowly defined, observable failure with a proven safe recovery—such as replacing an unhealthy replica behind capacity—rather than “restart anything that looks slow.” Verify unit, cgroup, workload identity, dependency health, and recent remediation history before acting.
- Build layered guardrails: rate limits, concurrency limits, canaries, blast-radius boundaries, maintenance windows where required, audit trails, and automatic halt conditions. A retry loop that restarts a process faster than its dependency recovers can cause a fleet-wide self-inflicted outage.
- Prefer supervisor-native actions and stable identity mechanisms over shell PID scraping. After every action, confirm the intended process group changed, readiness recovered, error rate improved, and no durable work was duplicated or abandoned.
- Review automation against real incidents and inject failure tests: PID reuse, stuck shutdown, OOM loop, partial network partition, bad deployment, and overloaded dependencies. Maintain a human override and clear escalation path.

## References

- [pidfd_send_signal(2): signal using a pidfd](https://man7.org/linux/man-pages/man2/pidfd_send_signal.2.html)
- [systemctl: service management operations](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
- [systemd.service: restart behavior](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- Free book: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
- Further reading (blog): [Charity Majors: Observability and incident response](https://charity.wtf/)

## What to learn next

- Official documentation: [man7 pidfd_send_signal(2)](https://man7.org/linux/man-pages/man2/pidfd_send_signal.2.html)
- Manual or specification: [systemd.service manual](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- Maintainer or personal blog: [Charity Majors — observability writing](https://charity.wtf/)
- Technical blog: [Google SRE — emergency response](https://sre.google/sre-book/managing-incidents/)
- Hands-on guide: [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
