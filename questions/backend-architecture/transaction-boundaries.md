---
title: Choose a transaction boundary
theme: backend-architecture
difficulty: middle
type: theory
tags: [databases, reliability, dependencies]
sources:
  - url: https://www.postgresql.org/docs/current/tutorial-transactions.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a transaction boundary

What belongs inside one database transaction in a backend request?

## Answer guide

- Put the atomic domain state changes that must succeed or fail together in the same transaction, with a consciously selected isolation level. Keep the transaction short: validate inputs first, then execute database work, commit, and only then trigger slow external effects.
- State the invariant being protected and identify competing writes, reads, and retries. Use constraints and locking or optimistic concurrency where they enforce the invariant, then monitor retries, deadlocks, and transaction duration.
- A transaction does not atomically include an email, HTTP call, or message broker publish. Holding locks during network calls reduces availability and can deadlock; use an outbox or compensating workflow and test process termination around commit.

## References

- [PostgreSQL: transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- Further reading (personal blog): [Brandur: transactionally staged jobs](https://brandur.org/job-drain)

## What to learn next

- Official documentation: [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- Manual or specification: [PostgreSQL concurrency control](https://www.postgresql.org/docs/current/mvcc.html)
- Maintainer or personal blog: [Brandur Leach's blog](https://brandur.org/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [PostgreSQL transactions tutorial](https://www.postgresql.org/docs/current/tutorial-transactions.html)
