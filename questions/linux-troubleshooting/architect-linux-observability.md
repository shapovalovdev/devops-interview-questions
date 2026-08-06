---
title: Architect Linux fleet observability for rapid fault isolation
theme: linux-troubleshooting
difficulty: staff
type: troubleshooting
tags: [linux, observability, metrics, logging, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/accounting/psi.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Architect Linux fleet observability for rapid fault isolation

## Answer guide

- Define a small, durable host signal set: CPU modes and pressure, memory pressure/OOMs, disk errors/latency, network drops/retransmits, filesystem headroom, process/service state, and change metadata. Preserve high-cardinality detail behind controlled drill-down paths.
- Correlate host telemetry with application SLOs, deployments, topology, and ownership, and set retention/access controls for sensitive logs. Validate agents under resource pressure so observability does not amplify a host incident.
- Avoid alerting on every host metric or collecting unbounded process labels. Review signal usefulness after incidents and use representative fault injection to prove that responders can isolate causes.

## References

- [Primary Linux documentation](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)
