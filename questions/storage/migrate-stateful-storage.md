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
- Further reading (blog): [AWS Storage Blog: storage migration patterns](https://aws.amazon.com/blogs/storage/)
