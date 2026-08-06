---
title: Lead evidence-preserving triage after a Linux kernel panic
theme: linux-troubleshooting
difficulty: senior
type: troubleshooting
tags: [linux, kernel, panic, incident-response]
sources:
  - url: https://docs.kernel.org/6.11/admin-guide/RAS/main.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Lead evidence-preserving triage after a Linux kernel panic

## Answer guide

- Preserve console, crash dump, kernel version, hardware/virtualization context, and the triggering workload before recycling nodes. Determine whether the event is a panic, watchdog reset, hardware error, or provider termination.
- Correlate recent kernel, driver, firmware, module, and infrastructure changes; reproduce only in an isolated environment. Configure crash capture and retention before the next event if policy and capacity permit.
- Mitigate by draining or replacing the node and using a known-good version with change control. Do not treat a single stack trace as proof of root cause or disable safety watchdogs without an approved recovery plan.

## References

- [Primary Linux documentation](https://docs.kernel.org/6.11/admin-guide/RAS/main.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)
