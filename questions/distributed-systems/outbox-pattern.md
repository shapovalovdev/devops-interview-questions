---
title: Apply the transactional outbox pattern
theme: distributed-systems
difficulty: middle
type: scenario
tags: [event-driven, databases, reliability]
sources:
  - url: https://www.postgresql.org/docs/current/transaction-iso.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Apply the transactional outbox pattern

How do you publish an event after a database change without losing one side of the update?

## Answer guide

- In the same database transaction as the business update, insert an immutable outbox row containing a stable event identifier and payload. A separate publisher reads committed rows, publishes with retry, and marks progress only after a recoverable acknowledgement.
- Preserve ordering where it matters with an aggregate key or partition, and retain rows long enough for replay and audit. Consumers still need deduplication because the relay can publish an event twice after a crash between broker acknowledgement and checkpoint.
- Avoid a dual-write that commits the database then sends to a broker without recovery metadata. Failed publication, an unavailable broker, malformed payloads, and schema evolution need a dead-letter or repair workflow rather than silently dropping business state.

## References

- [PostgreSQL: transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- Further reading (personal blog): [Chris Richardson: transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html)

## What to learn next

- Official documentation: [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- Manual or specification: [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- Maintainer or personal blog: [Chris Richardson's microservices blog](https://microservices.io/)
- Technical blog: [Debezium: outbox pattern](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html)
- Hands-on guide: [PostgreSQL logical decoding](https://www.postgresql.org/docs/current/logicaldecoding.html)
