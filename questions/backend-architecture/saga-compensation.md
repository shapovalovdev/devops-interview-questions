---
title: Coordinate a saga with compensations
theme: backend-architecture
difficulty: senior
type: theory
tags: [event-driven, reliability, databases]
sources:
  - url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/saga/saga
    source_type: official-docs
    verified_on: 2026-08-06
---

# Coordinate a saga with compensations

How should a cross-service business operation recover when one later step fails?

## Answer guide

- Represent the workflow as explicit durable steps with local transactions and define a business compensation for each reversible completed step. Record correlation identity, state, owner, retry policy, timeout, and the operator path for an indeterminate outcome.
- Prefer a choreography or orchestration model only after making ownership and observability clear. Design compensations as idempotent commands, protect external side effects, and reconcile with authoritative systems when outcomes are uncertain.
- A compensation is not a database rollback and may itself fail or be impossible, such as an already shipped item. Do not hide partial success; test duplicate events, reordered delivery, and a crash between a completed action and state recording.

## References

- [Microsoft: saga design pattern](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/saga/saga)
- Further reading (personal blog): [Chris Richardson: saga pattern](https://microservices.io/patterns/data/saga.html)

## What to learn next

- Official documentation: [Azure saga pattern](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/saga/saga)
- Manual or specification: [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- Maintainer or personal blog: [Chris Richardson's blog](https://microservices.io/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [Debezium outbox event router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html)
