---
title: Migrate stateful storage with controlled downtime
theme: storage
difficulty: senior
type: scenario
tags: [storage, deployment, reliability, databases]
sources:
  - url: https://www.postgresql.org/docs/current/backup.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Migrate stateful storage with controlled downtime

What plan would you use to move a production stateful service to new storage?

## Answer guide

- Define the data-consistency model, acceptable downtime, rollback point, validation criteria, and owner approvals before selecting replication, export/import, dual-write, or a maintenance-window approach.
- Rehearse at representative data size, measure transfer and catch-up time, secure the migration channel, and monitor source and target capacity and error rates.
- At cutover, fence or drain writes as required, verify the target's integrity and application behavior, retain the old source read-only for the agreed rollback window, then decommission deliberately.
- Copying blocks while an application writes can create an inconsistent target. A migration without an explicit rollback, schema/version compatibility test, or capacity headroom risks extended outage and data loss.

## References

- [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html)
- Further reading (blog): [AWS Storage Blog: storage migration patterns](https://aws.amazon.com/blogs/storage/uncover-new-performance-insights-using-amazon-ebs-detailed-performance-statistics/)
## What to learn next

- Official documentation: [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- Manual or specification: [mount(8) Linux manual](https://man7.org/linux/man-pages/man8/mount.8.html)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/blog/index.html)
- Technical blog: [Red Hat engineering blog](https://www.redhat.com/en/blog)
- Hands-on guide: [Fedora Quick Docs](https://docs.fedoraproject.org/en-US/quick-docs/)
