---
title: Triage packet loss from a Linux host to a critical dependency
theme: linux-troubleshooting
difficulty: middle
type: troubleshooting
tags: [linux, networking, tcp, packet-loss, troubleshooting]
sources:
  - url: https://www.kernel.org/doc/html/latest/networking/scaling.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage packet loss from a Linux host to a critical dependency

## Answer guide

- Measure the affected five-tuple, time window, loss/retransmits, interface counters, and route; distinguish DNS, connection establishment, congestion, MTU, NIC, and remote-service failures.
- Inspect `ip` route/address state, interface errors and drops, socket statistics, and an appropriately scoped packet capture. Compare an unaffected host or path to separate local from network-wide behavior.
- Avoid broad firewall flushes and unsafely large captures. Change one layer at a time, validate bidirectional traffic and application success, then retain counters long enough to catch intermittent recurrence.

## References

- [Primary Linux documentation](https://www.kernel.org/doc/html/latest/networking/scaling.html)
- [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Official documentation: [Linux kernel documentation](https://www.kernel.org/doc/html/latest/)
- Manual or specification: [Linux man-pages](https://man7.org/linux/man-pages/)
- Maintainer or personal blog: [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
- Hands-on guide: [Arch Linux Wiki — General troubleshooting](https://wiki.archlinux.org/title/General_troubleshooting)

