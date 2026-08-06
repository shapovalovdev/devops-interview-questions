---
title: Consume an at-least-once event stream safely
theme: distributed-systems
difficulty: middle
type: scenario
tags: [event-driven, kafka, reliability]
sources:
  - url: https://kafka.apache.org/documentation/#semantics
    source_type: official-docs
    verified_on: 2026-08-06
---

# Consume an at-least-once event stream safely

How should a consumer process duplicates while preserving a correct business outcome?

## Answer guide

- Assume a record can be delivered again after a consumer crash, rebalance, or uncertain acknowledgement. Give each business effect a durable deduplication key or use an idempotent state transition, then commit the consumer position only after the effect is safely recorded.
- Decide the atomic boundary between consumed offset and application state. A single transactional store can record both; otherwise use an outbox, inbox, or reconciliation process and document the period in which an effect may be pending.
- Do not promise exactly-once end-to-end merely because a broker supports transactions. External APIs, emails, and side effects outside the transaction can duplicate; rebalances, poison messages, and retention expiry need observability and an operator recovery path.

## References

- [Apache Kafka: message delivery semantics](https://kafka.apache.org/documentation/#semantics)
- Further reading (personal blog): [Chris Richardson: idempotent consumer](https://microservices.io/post/microservices/patterns/2020/10/16/idempotent-consumer.html)

## What to learn next

- Official documentation: [Kafka consumer configuration](https://kafka.apache.org/documentation/#consumerconfigs)
- Manual or specification: [Kafka design](https://kafka.apache.org/documentation/#design)
- Maintainer or personal blog: [Chris Richardson's microservices blog](https://microservices.io/)
- Technical blog: [Confluent: exactly-once semantics](https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/)
- Hands-on guide: [Kafka consumer tutorial](https://kafka.apache.org/quickstart)
