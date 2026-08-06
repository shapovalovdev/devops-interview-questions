---
title: Use a transactional outbox for event publication
theme: backend-architecture
difficulty: middle
type: theory
tags: [databases, event-driven, reliability]
sources:
  - url: https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use a transactional outbox for event publication

How does a transactional outbox reduce the database-write and event-publish failure gap?

## Answer guide

- Write the domain change and a durable outbox row in one database transaction. A separate relay reads committed rows and publishes an event with a stable identifier, allowing recovery after a service crash without losing a committed business change.
- Make consumer processing idempotent because at-least-once relays may publish duplicates. Define ordering scope, retention, relay ownership, monitoring for age and backlog, and a replay and poison-event process.
- Do not claim exactly-once delivery merely because the outbox is transactional. A relay can crash after publishing but before marking progress, and an unbounded table can harm the primary database; test duplicate delivery and relay outage.

## References

- [Debezium outbox event router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html)
- Further reading (blog): [AWS: transactional outbox](https://aws.amazon.com/blogs/mt/achieving-transactional-integrity-with-saga-outbox-pattern/)

## What to learn next

- Official documentation: [Debezium documentation](https://debezium.io/documentation/reference/stable/)
- Manual or specification: [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- Maintainer or personal blog: [Chris Richardson's blog](https://microservices.io/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [Debezium outbox tutorial](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html)
