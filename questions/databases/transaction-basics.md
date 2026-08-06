---
title: Explain database transaction boundaries
theme: databases
difficulty: junior
type: theory
tags: [databases, postgresql, reliability]
sources:
  - url: https://www.postgresql.org/docs/current/tutorial-transactions.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain database transaction boundaries

Why should related database changes be made in one transaction?

## Answer guide

- A transaction groups statements so they either commit together or roll back together, preserving an application invariant such as recording both an order and its payment state. PostgreSQL exposes this through `BEGIN`, `COMMIT`, and `ROLLBACK`.
- Keep transactions small, make the boundary match one business operation, and handle expected retryable errors in the application. Acquire external input before opening the transaction and publish irreversible side effects only with an explicit idempotency or outbox design.
- A transaction is not a distributed transaction across arbitrary services. Long or idle transactions retain snapshots and locks, can block maintenance, and increase contention, so observe duration and terminate or fix abandoned work carefully.

## References

- [PostgreSQL documentation: transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- Further reading (blog): [pganalyze: connection tracing and idle transactions](https://pganalyze.com/blog/postgres-connection-tracing-wait-event-analysis-and-vacuum-monitoring)

## What to learn next

- Official documentation: [PostgreSQL: transactions tutorial](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — connection tracing and idle transactions](https://pganalyze.com/blog/postgres-connection-tracing-wait-event-analysis-and-vacuum-monitoring)
- Hands-on guide: [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
