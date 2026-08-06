---
title: Preserve required ordering in asynchronous processing
theme: queue-messaging
difficulty: middle
type: scenario
tags: [kafka, rabbitmq, message-queues, event-driven, reliability]
sources:
  - url: https://kafka.apache.org/documentation/#intro_concepts_and_terms
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rabbitmq.com/docs/queues
    source_type: official-docs
    verified_on: 2026-08-06
---

# Preserve required ordering in asynchronous processing

An order service must process state changes for each order in sequence. How do you retain that property while scaling?

## Answer guide

- Define the ordering key and scope. In Kafka, key all events for one order to the same partition and process that partition serially for that key; order is not global across partitions. In RabbitMQ, multiple consumers and redelivery make end-to-end ordering fragile unless work is serialized deliberately.
- Put version or sequence information in the event and reject, buffer, or reconcile stale/out-of-order updates. Idempotent state transitions make replay and duplicate delivery safe.
- Parallelism competes with order: one hot key cannot scale indefinitely without changing the business design. Never infer order from wall-clock timestamps or publisher arrival across independent producers.

## References

- [Apache Kafka concepts and terms](https://kafka.apache.org/documentation/#intro_concepts_and_terms)
- [RabbitMQ queues](https://www.rabbitmq.com/docs/queues)
- Further reading (blog): [Kafka partitioning](https://www.confluent.io/blog/how-choose-number-topics-partitions-kafka-cluster/)
