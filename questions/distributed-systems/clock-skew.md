---
title: Handle clock skew in a distributed service
theme: distributed-systems
difficulty: junior
type: troubleshooting
tags: [time, reliability, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc5905.html
    source_type: standard
    verified_on: 2026-08-06
---

# Handle clock skew in a distributed service

Why is wall-clock time unsafe as a universal ordering mechanism, and what should you do instead?

## Answer guide

- Wall clocks can drift, step backward, and disagree across hosts, so they cannot alone establish causality or a safe lease decision. Synchronize clocks with a monitored time service, record clock health, and use a logical sequence, database transaction order, or consensus log when total order matters.
- Distinguish elapsed-time measurement from civil timestamps. Use monotonic timers for local deadlines, make lease and certificate expiry assumptions explicit, and define the maximum tolerated uncertainty before a node stops serving a time-sensitive role.
- A hidden time jump can invalidate tokens early, make logs appear out of order, or allow two lease holders. Treat NTP loss, virtual-machine suspend, leap handling, and an unsynchronized recovering node as operational failures with alarms and safe rejoin rules.

## References

- [RFC 5905: Network Time Protocol Version 4](https://www.rfc-editor.org/rfc/rfc5905.html)
- Further reading (personal blog): [Cockroach Labs: living without atomic clocks](https://www.cockroachlabs.com/blog/living-without-atomic-clocks/)

## What to learn next

- Official documentation: [chrony documentation](https://chrony-project.org/documentation.html)
- Manual or specification: [RFC 5905](https://www.rfc-editor.org/rfc/rfc5905.html)
- Maintainer or personal blog: [Martin Kleppmann: clocks](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)
- Technical blog: [Google SRE: distributed periodic scheduling](https://sre.google/sre-book/distributed-periodic-scheduling/)
- Hands-on guide: [Chrony FAQ](https://chrony-project.org/faq.html)
