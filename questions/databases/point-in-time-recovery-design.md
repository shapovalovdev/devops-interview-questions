---
title: Design PostgreSQL point-in-time recovery
theme: databases
difficulty: senior
type: scenario
tags: [databases, postgresql, storage, reliability, incident-response]
sources:
  - url: https://www.postgresql.org/docs/current/continuous-archiving.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design PostgreSQL point-in-time recovery

How would you recover a PostgreSQL service to immediately before an accidental deletion?

## Answer guide

- Maintain verified base backups plus continuous write-ahead-log (WAL) archiving, with a retention window that meets the recovery-point objective. Restore into an isolated environment, select and document the target time or transaction boundary, and validate the recovered application state.
- Monitor base backup completion, archive continuity, replay progress, archive permissions, restore duration, and the oldest recoverable point. Protect backup and WAL storage independently from the primary and rehearse the full procedure with service owners.
- A logical dump or storage snapshot alone cannot promise a precise time target. Missing WAL, a wrong recovery target, version incompatibility, or restoring in place can make a recoverable operator mistake a larger outage.

## References

- [PostgreSQL documentation: continuous archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html)
- Further reading (blog): [pganalyze: Postgres backup topics](https://pganalyze.com/blog)
