---
title: Design a Kafka exactly-once processing flow
theme: queue-messaging
difficulty: senior
type: scenario
tags: [kafka, message-queues, event-driven, reliability]
sources:
  - url: https://kafka.apache.org/documentation/#semantics
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a Kafka exactly-once processing flow

How can a Kafka application safely read records, transform them, and publish derived Kafka records exactly once?

## Answer guide

- Use Kafka's documented transactional producer and consumer integration for the supported consume-transform-produce boundary: output records and consumed offsets are committed atomically to Kafka, and downstream consumers use the appropriate isolation level.
- Scope the claim narrowly to Kafka records and a configured transactional topology. Any call to an external system needs its own idempotency, outbox/inbox pattern, or compensating action.
- Transactions add coordination, timeouts, fencing, and operational constraints. Monitor aborted transactions and producer errors; do not treat retries or `acks=all` alone as an exactly-once design.

## References

- [Apache Kafka message delivery semantics](https://kafka.apache.org/documentation/#semantics)
- Further reading (blog): [Exactly-once semantics in Kafka](https://www.confluent.io/blog/enabling-exactly-once-kafka-streams/)

## What to learn next

- Official documentation: [Apache Kafka message delivery semantics](https://kafka.apache.org/documentation/#semantics)
- Manual or specification: [Apache Kafka protocol](https://kafka.apache.org/protocol)
- Maintainer or personal blog: [Matthias J. Sax — Gently Down the Stream](https://www.gentlydownthe.stream/)
- Technical blog: [Confluent technical blog](https://www.confluent.io/blog/)
- Hands-on guide: [Confluent Kafka tutorials](https://developer.confluent.io/tutorials/)
