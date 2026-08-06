---
title: Design multi-tenant isolation
theme: backend-architecture
difficulty: senior
type: scenario
tags: [security, databases, iam]
sources:
  - url: https://www.postgresql.org/docs/current/ddl-rowsecurity.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design multi-tenant isolation

How should a shared backend prevent one tenant from reading or changing another tenant’s data?

## Answer guide

- Establish tenant identity from authenticated context, not a caller-controlled request field, and carry it through every query, cache key, event, and authorization check. Choose row, schema, database, or account isolation based on risk, scale, and operational needs.
- Enforce the boundary in more than one layer where appropriate, such as application policy plus database row-level security, and test with a least-privileged runtime identity. Audit access decisions and measure cross-tenant denial attempts.
- Filtering in one repository method is not isolation because a future query, analytics job, cache, or admin endpoint can bypass it. Missing tenant keys in caches leak data; perform adversarial tests and a response plan for boundary violations.

## References

- [PostgreSQL row security policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
- Further reading (blog): [AWS SaaS tenant isolation](https://aws.amazon.com/blogs/apn/saas-tenant-isolation-strategies/)

## What to learn next

- Official documentation: [PostgreSQL row security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
- Manual or specification: [OWASP authorization cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- Maintainer or personal blog: [Troy Hunt's blog](https://www.troyhunt.com/)
- Technical blog: [AWS SaaS Factory](https://aws.amazon.com/blogs/apn/)
- Hands-on guide: [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
