---
title: Triage PostgreSQL lock contention
theme: databases
difficulty: middle
type: troubleshooting
tags: [databases, postgresql, monitoring, troubleshooting, reliability]
sources:
  - url: https://www.postgresql.org/docs/current/explicit-locking.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage PostgreSQL lock contention

How do you investigate a request pile-up caused by PostgreSQL locks?

## Answer guide

- Identify blocked sessions, their wait events, the blocking session, lock modes, query text, transaction age, and application owner. PostgreSQL has several lock modes with differing conflict rules; the visible symptom is often many waiters, not the original blocker.
- Reduce impact by stopping or completing the safe blocker, pausing a conflicting deployment or batch job, and applying statement, lock, and idle-in-transaction timeouts where appropriate. Then fix transaction scope, access order, indexes, or migration method.
- Avoid a blanket kill of waiters: it can cause retry storms and hide the root cause. Some locks are expected, and DDL can request stronger locks than ordinary reads; rehearse migration locking behavior on representative data first.

## References

- [PostgreSQL documentation: explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
- Further reading (blog): [pganalyze: lock monitoring](https://pganalyze.com/blog/postgres-lock-monitoring)
