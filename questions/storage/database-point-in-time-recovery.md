---
title: Design database point-in-time recovery
theme: storage
difficulty: senior
type: scenario
tags: [storage, databases, reliability, incident-response]
sources:
  - url: https://www.postgresql.org/docs/current/continuous-archiving.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design database point-in-time recovery

How would you support recovery of a PostgreSQL service to just before an operator error?

## Answer guide

- Keep validated base backups and continuous WAL archiving for a retention window that satisfies the recovery-point objective; protect the archive independently from the primary database.
- Document the target-time or recovery-target procedure, required configuration and credentials, and an isolated restore environment. Exercise recovery and validate application-level correctness.
- Monitor backup completion, WAL archive continuity, restore duration, archive access, and the oldest recoverable point; alert before the RPO window is breached.
- A snapshot or logical dump alone may not support a precise time target. Gaps in WAL, incompatible versions, or a restore performed in place without isolation can turn an application error into a larger loss.

## References

- [PostgreSQL: continuous archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html)
- Further reading (blog): [Google Cloud Blog: backup and disaster recovery](https://cloud.google.com/blog/products/storage-data-transfer/introducing-google-cloud-backup-and-dr)
