---
title: Establish data-integrity controls across services
theme: distributed-systems
difficulty: staff
type: theory
tags: [databases, security, reliability]
sources:
  - url: https://sre.google/sre-book/data-integrity/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish data-integrity controls across services

How would you make data integrity an engineered, measurable property rather than an incident afterthought?

## Answer guide

- Define critical invariants, owners, authoritative records, and acceptable reconciliation delay for each business domain. Enforce invariants as close to durable state as possible with constraints, version checks, authorization, immutable audit events, and controlled migrations.
- Build detection and repair into the architecture: checksums or counts, reconciliation jobs, sampled end-to-end assertions, backup restore tests, and a documented correction workflow. Measure integrity signals separately from availability so a fast but wrong service is not considered healthy.
- Avoid treating replication as proof of correctness. A bad deployment, malicious write, schema bug, or duplicated event can replicate perfectly; destructive repair or a rollback without provenance can compound loss, so retain evidence and require bounded, reviewed remediation.

## References

- [Google SRE: data integrity](https://sre.google/sre-book/data-integrity/)
- Further reading (personal blog): [Brandur Leach: migrations](https://brandur.org/online-migrations)

## What to learn next

- Official documentation: [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
- Manual or specification: [Google SRE: data integrity](https://sre.google/sre-book/data-integrity/)
- Maintainer or personal blog: [Brandur Leach's writing](https://brandur.org/)
- Technical blog: [GitHub Engineering: database](https://github.blog/engineering/)
- Hands-on guide: [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html)
