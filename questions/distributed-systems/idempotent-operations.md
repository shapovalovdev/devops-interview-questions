---
title: Make a retried write idempotent
theme: distributed-systems
difficulty: junior
type: scenario
tags: [reliability, event-driven, databases]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9110.html
    source_type: standard
    verified_on: 2026-08-06
---

# Make a retried write idempotent

How would you prevent a client timeout and retry from creating a second payment or job?

## Answer guide

- Give the logical operation a stable, client-generated idempotency key and persist the key, request fingerprint, outcome, and expiry atomically with the effect. On a retry, return the prior compatible result instead of executing the effect again.
- Treat HTTP method semantics as insufficient for business correctness: a POST can be safe with an idempotency design, while a nominally idempotent operation can still duplicate external side effects. Define key scope, retention, conflict response, and caller retry budget.
- A timeout means the caller lacks an answer, not that the server did nothing. Crashes between database commit and response, duplicate deliveries, and key reuse with changed parameters require reconciliation and an observable, deterministic conflict path.

## References

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
- Further reading (personal blog): [Brandur Leach: idempotency keys](https://brandur.org/fragments/idempotency-key-database)

## What to learn next

- Official documentation: [Stripe: idempotent requests](https://docs.stripe.com/api/idempotent_requests)
- Manual or specification: [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)
- Maintainer or personal blog: [Brandur Leach's writing](https://brandur.org/)
- Technical blog: [AWS Builders' Library: retries](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- Hands-on guide: [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
