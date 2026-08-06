---
title: Respond to suspected PostgreSQL data corruption
theme: databases
difficulty: senior
type: troubleshooting
tags: [databases, postgresql, incident-response, reliability, storage]
sources:
  - url: https://www.postgresql.org/docs/current/backup.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to suspected PostgreSQL data corruption

What is your first response when PostgreSQL reports possible data corruption?

## Answer guide

- Preserve evidence and reduce further writes when the impact assessment warrants it; capture error logs, affected object and page information, storage and kernel evidence, recent changes, replication state, and backup/WAL status. Escalate to the database and storage owners with a declared incident lead.
- Determine scope on copies or an isolated restore, compare primary and replicas carefully, and select a recovery path that preserves the best known data: fail over, restore, or rebuild after expert review. Validate application-level invariants after recovery, not merely server startup.
- Do not run destructive repair commands, overwrite backups, or promote a replica solely because it is reachable. Hardware, filesystem, software, and operator causes need different treatment; recovery operations can permanently discard evidence or good data.

## References

- [PostgreSQL documentation: backup and restore](https://www.postgresql.org/docs/current/backup.html)
- Further reading (blog): [pganalyze: Postgres operational practices](https://pganalyze.com/blog)
