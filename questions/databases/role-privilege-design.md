---
title: Design least-privilege PostgreSQL roles
theme: databases
difficulty: middle
type: scenario
tags: [databases, postgresql, security, least-privilege, governance]
sources:
  - url: https://www.postgresql.org/docs/current/user-manag.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design least-privilege PostgreSQL roles

How would you separate application, migration, reporting, and administrator access in PostgreSQL?

## Answer guide

- Create distinct login and group roles with narrowly scoped privileges: applications perform only required data operations, migration automation receives time-bounded DDL authority, reporting receives read access, and administration is separately controlled. Set ownership and default privileges deliberately.
- Use managed secrets, strong authentication, TLS, audit identity changes, and periodically review role memberships and grants. Test a role in a staging environment and use `SET ROLE` or a dedicated account to prove it cannot perform prohibited actions.
- A role that owns an object has powers beyond ordinary grants, and membership inheritance or broad schema privileges can defeat the intended boundary. Never run routine services as a superuser; emergency access needs logging, expiration, and review.

## References

- [PostgreSQL documentation: database roles](https://www.postgresql.org/docs/current/user-manag.html)
- Further reading (blog): [pganalyze: PostgreSQL security](https://pganalyze.com/postgresql-security)
