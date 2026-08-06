---
title: Explain RAID redundancy and its limits
theme: hardware
difficulty: junior
type: theory
tags: [hardware, raid, storage, reliability]
sources:
  - url: https://docs.kernel.org/admin-guide/md.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain RAID redundancy and its limits

What problem does RAID solve, and why is it not a backup?

## Answer guide

- RAID combines drives to provide capacity, performance, and/or tolerance of specified drive failures. The RAID level determines the usable capacity, parity or mirroring behavior, and number of failures it can tolerate.
- It does not create an independent historical copy. Deletion, corruption, ransomware, controller mistakes, and many site-level failures can affect every replica in the array.
- During rebuilds, performance and fault tolerance can be reduced; monitor rebuild progress and latency, keep tested backups, and replace failed hardware according to the array’s supported procedure.

## References

- [Linux kernel: Multiple Devices (MD)](https://docs.kernel.org/admin-guide/md.html)
- Further reading (blog): [Backblaze: managing for hard-drive failure and data corruption](https://www.backblaze.com/blog/?p=91405)
