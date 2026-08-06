---
title: Explain relational tables, keys, and constraints
theme: databases
difficulty: junior
type: theory
tags: [databases, postgresql, reliability]
sources:
  - url: https://www.postgresql.org/docs/current/ddl-constraints.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain relational tables, keys, and constraints

What problem do primary keys, foreign keys, and constraints solve in a relational database?

## Answer guide

- A table stores rows of one relation; a primary key identifies each row, while a foreign key requires a referenced value to exist in another table. `NOT NULL`, `UNIQUE`, `CHECK`, and exclusion constraints make invalid states harder or impossible to commit.
- Put invariants that must hold for every writer in the database, then add indexes that support the constraint and actual query patterns. Name constraints and model deletion or update behavior deliberately, because foreign-key actions are part of the application contract.
- Constraints do not replace authorization, input validation, or a migration plan. A bulk import, deferred constraint, or cascading action can still create load or unexpected effects, so test realistic writes and monitor constraint failures.

## References

- [PostgreSQL documentation: constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
- Further reading (blog): [pganalyze: Postgres constraints and data integrity](https://pganalyze.com/blog)

## What to learn next

- Official documentation: [PostgreSQL: constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL data integrity articles](https://pganalyze.com/blog)
- Hands-on guide: [PostgreSQL data definition tutorial](https://www.postgresql.org/docs/current/ddl.html)
