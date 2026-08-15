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
  - url: https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-troubleshooting/innodb-recovery-modes
    source_type: official-docs
    verified_on: 2026-08-16
---

# Respond to suspected PostgreSQL data corruption

What is your first response when PostgreSQL reports possible data corruption?

## Answer guide

- Preserve evidence and reduce further writes when the impact assessment warrants it; capture error logs, affected object and page information, storage and kernel evidence, recent changes, replication state, and backup/WAL status. Escalate to the database and storage owners with a declared incident lead.
- Determine scope on copies or an isolated restore, compare primary and replicas carefully, and select a recovery path that preserves the best known data: fail over, restore, or rebuild after expert review. Validate application-level invariants after recovery, not merely server startup.
- Do not run destructive repair commands, overwrite backups, or promote a replica solely because it is reachable. Hardware, filesystem, software, and operator causes need different treatment; recovery operations can permanently discard evidence or good data.
- Evidence-first corruption response is engine-agnostic: InnoDB force-recovery levels are the comparable last-resort lever that can mask or destroy evidence, and SQL Server emergency-mode repair carries the same warning — the stop, scope, and restore-from-copies sequence comes before any repair command.

## References

- [PostgreSQL documentation: backup and restore](https://www.postgresql.org/docs/current/backup.html)
- Further reading (blog): [pganalyze: Postgres operational practices](https://pganalyze.com/blog)
- [MariaDB — InnoDB recovery modes](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-troubleshooting/innodb-recovery-modes)

## What to learn next

- Official documentation: [PostgreSQL: backup and restore](https://www.postgresql.org/docs/current/backup.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL operations](https://pganalyze.com/blog)
- Hands-on guide: [PostgreSQL pg_verifybackup reference](https://www.postgresql.org/docs/current/app-pgverifybackup.html)
