---
title: Establish database change governance without blocking delivery
theme: databases
difficulty: staff
type: scenario
tags: [databases, postgresql, governance, deployment, reliability]
sources:
  - url: https://www.postgresql.org/docs/current/ddl-alter.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish database change governance without blocking delivery

How would you govern risky database changes while allowing teams to ship frequently?

## Answer guide

- Classify changes by observed lock, rewrite, data-loss, privilege, and reversibility risk, then provide automated preflight checks and documented safe patterns. Require evidence proportionate to risk: compatible application versions, rollout plan, runtime budget, monitoring, owner, and recovery procedure.
- Make low-risk changes self-service and make exceptions explicit, time-bounded, and reviewed after execution. Keep a shared migration history and use incident learning to improve templates, tooling, and platform defaults rather than adding blanket approvals.
- A CAB-style gate alone cannot predict runtime data size or long transactions, while unrestricted production DDL can create global outages. Governance must preserve emergency access but record it and reconcile drift afterward.
- Risk classification generalizes once you know each engine's change matrix: lock, rewrite, and duration behavior differ per statement family on PostgreSQL exactly as online-DDL capability differs per operation on MySQL or SQL Server, so governance should classify by observed effect, not by tool.

## References

- [PostgreSQL documentation: modifying tables](https://www.postgresql.org/docs/current/ddl-alter.html)
- Further reading (blog): [pganalyze: database migration locking topics](https://pganalyze.com/blog)

## What to learn next

- Official documentation: [PostgreSQL: modifying tables](https://www.postgresql.org/docs/current/ddl-alter.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL migrations and operations](https://pganalyze.com/blog)
- Hands-on guide: [PostgreSQL ALTER TABLE reference](https://www.postgresql.org/docs/current/sql-altertable.html)
