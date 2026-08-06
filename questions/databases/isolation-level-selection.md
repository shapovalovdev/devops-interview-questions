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
---

# Select a PostgreSQL transaction isolation level

How would you choose an isolation level for a workflow that must not oversell inventory?

## Answer guide

- Start from the invariant and concurrent operations, not a preferred isolation label. PostgreSQL's default Read Committed gives each command a snapshot; use explicit locking, an atomic conditional update, or Serializable transactions when the workflow needs stronger coordination.
- At Serializable isolation, design the transaction to be short and retry the documented serialization failures as a whole transaction. Add a unique constraint or other database-enforced invariant where it directly represents the business rule.
- Higher isolation is not free and does not repair external side effects. Long transactions and high conflict increase retries or blocking; retries must be idempotent, bounded, observable, and never silently convert a rejected sale into an inconsistent state.

## References

- [PostgreSQL documentation: transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- Further reading (blog): [pganalyze: Postgres transaction and concurrency topics](https://pganalyze.com/blog)
