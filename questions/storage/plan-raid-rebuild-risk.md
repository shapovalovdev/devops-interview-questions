---
title: Plan a degraded RAID rebuild without compounding risk
theme: storage
difficulty: senior
type: scenario
tags: [storage, hardware, reliability, incident-response]
sources:
  - url: https://www.kernel.org/doc/html/latest/admin-guide/md.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Plan a degraded RAID rebuild without compounding risk

An array is degraded after one member fails. How do you manage the rebuild safely?

## Answer guide

- Confirm the failed member and array state from controller and operating-system evidence, assess current redundancy and backups, and determine whether the workload can tolerate the increased risk and rebuild I/O.
- Replace with a compatible, verified device, follow the array's documented replacement procedure, and monitor sync progress, read errors, latency, and remaining members throughout rebuild.
- Rate-limit or schedule rebuild work when necessary to preserve service SLOs, but account for the longer degraded window; update capacity and replacement records.
- Replacing the wrong device, ignoring latent errors, or treating rebuild as a backup can cause multi-device loss. Do not force an uncertain member online merely to clear an alert.

## References

- [Linux MD RAID administration guide](https://www.kernel.org/doc/html/latest/admin-guide/md.html)
- Further reading (blog): [AWS Storage Blog: resilient storage operations](https://aws.amazon.com/blogs/storage/uncover-new-performance-insights-using-amazon-ebs-detailed-performance-statistics/)
## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
