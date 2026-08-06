---
title: Explain RAID redundancy and its limits
theme: storage
difficulty: junior
type: theory
tags: [storage, hardware, reliability, availability]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/md.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain RAID redundancy and its limits

What problem does RAID solve, and why is it not a backup strategy?

## Answer guide

- RAID combines devices to trade capacity and performance for tolerance of some device failures. Mirroring duplicates data; parity layouts reconstruct data after a tolerated member failure, subject to the selected level and array state.
- It improves availability for a device failure, but it does not preserve an earlier correct version of data.
- Monitor member health, rebuild progress, error rates, spare capacity, and the array's degraded state. Test replacement procedures before an incident.
- RAID cannot protect against accidental deletion, application corruption, ransomware, controller faults, or a site loss; retain independent, restore-tested backups.

## References

- [Linux MD RAID administration guide](https://www.kernel.org/doc/html/latest/admin-guide/md.html)
- Further reading (blog): [AWS Storage Blog: resilient storage architecture](https://aws.amazon.com/blogs/storage/)
