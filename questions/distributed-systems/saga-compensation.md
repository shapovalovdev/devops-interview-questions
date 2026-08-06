---
title: Coordinate a multi-service saga
theme: distributed-systems
difficulty: middle
type: scenario
tags: [event-driven, reliability, recovery]
sources:
  - url: https://microservices.io/patterns/data/saga.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Coordinate a multi-service saga

When should a workflow use compensating actions instead of a distributed transaction?

## Answer guide

- Use a saga when independent services own their data and one global atomic transaction is unavailable or inappropriate. Model each durable step, its successful outcome, timeout, retry policy, and semantic compensation; compensation is a new business action, not a database rollback.
- Choose orchestration when one workflow owner needs visibility and ordering, or choreography when events remain simple and observable. Persist correlation identifiers and state so a failover can resume rather than infer progress from ephemeral messages.
- Some effects cannot be fully undone, such as a shipment or an external notification. Duplicates, late replies, compensation failure, and concurrent edits require idempotent commands, manual resolution, and clear user-facing status instead of a false promise of atomicity.

## References

- [Microservices.io: Saga pattern](https://microservices.io/patterns/data/saga.html)
- Further reading (personal blog): [Chris Richardson: saga pattern](https://microservices.io/patterns/data/saga.html)

## What to learn next

- Official documentation: [Temporal: saga pattern](https://docs.temporal.io/develop/java/saga)
- Manual or specification: [BPMN 2.0 specification](https://www.omg.org/spec/BPMN/2.0/PDF)
- Maintainer or personal blog: [Chris Richardson's microservices blog](https://microservices.io/)
- Technical blog: [AWS: saga orchestration](https://aws.amazon.com/blogs/architecture/implementing-the-saga-pattern-with-aws-lambda-and-amazon-step-functions/)
- Hands-on guide: [Temporal tutorials](https://learn.temporal.io/)
