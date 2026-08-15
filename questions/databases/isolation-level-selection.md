---
title: Select a PostgreSQL transaction isolation level
theme: databases
difficulty: middle
type: scenario
tags: [databases, postgresql, reliability, troubleshooting]
sources:
  - url: https://www.postgresql.org/docs/current/transaction-iso.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/sql/t-sql/statements/set-transaction-isolation-level-transact-sql
    source_type: official-docs
    verified_on: 2026-08-16
---

# Select a PostgreSQL transaction isolation level

How would you choose an isolation level for a workflow that must not oversell inventory?

## Answer guide

- Start from the invariant and concurrent operations, not a preferred isolation label. PostgreSQL's default Read Committed gives each command a snapshot; use explicit locking, an atomic conditional update, or Serializable transactions when the workflow needs stronger coordination.
- At Serializable isolation, design the transaction to be short and retry the documented serialization failures as a whole transaction. Add a unique constraint or other database-enforced invariant where it directly represents the business rule.
- Higher isolation is not free and does not repair external side effects. Long transactions and high conflict increase retries or blocking; retries must be idempotent, bounded, observable, and never silently convert a rejected sale into an inconsistent state.
- Isolation labels hide engine differences worth naming: MySQL InnoDB's REPEATABLE READ gives every transaction a consistent snapshot while SQL Server offers Read Committed Snapshot Isolation as an opt-in, and both differ from PostgreSQL's snapshot-based REPEATABLE READ — check the engine's actual semantics before promising an invariant.

## References

- [PostgreSQL documentation: transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- Further reading (blog): [pganalyze: Postgres transaction and concurrency topics](https://pganalyze.com/blog)
- [SQL Server — SET TRANSACTION ISOLATION LEVEL](https://learn.microsoft.com/sql/t-sql/statements/set-transaction-isolation-level-transact-sql)

## What to learn next

- Official documentation: [PostgreSQL: transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL concurrency articles](https://pganalyze.com/blog)
- Hands-on guide: [PostgreSQL transaction tutorial](https://www.postgresql.org/docs/current/tutorial-transactions.html)
