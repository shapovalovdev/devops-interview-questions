---
title: Choose a work queue or an event log
theme: queue-messaging
difficulty: junior
type: theory
tags: [message-queues, kafka, rabbitmq, event-driven, reliability]
sources:
  - url: https://kafka.apache.org/documentation/#intro_concepts_and_terms
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rabbitmq.com/docs/queues
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a work queue or an event log

When is RabbitMQ-style queueing a better fit than Kafka-style durable event logs, and when is it not?

## Answer guide

- A work queue routes a message to a consumer and normally removes it after acknowledgement; it fits bounded asynchronous jobs, per-message routing, and short-lived task hand-off. Kafka stores ordered records in retained topic partitions and independently tracked consumer offsets, so several applications can replay the same event stream.
- Choose from delivery and recovery requirements, not protocol popularity: use a queue for work ownership and a log for replayable facts, analytics, fan-out, or rebuilding downstream state. Either can support multiple consumers, but their retention and consumption models differ.
- Do not treat either as a transactional business workflow. Consumers must remain idempotent because redelivery, retries, and duplicate effects can occur; set retention, DLQ/retry, and capacity limits explicitly.

## References

- [Apache Kafka concepts and terms](https://kafka.apache.org/documentation/#intro_concepts_and_terms)
- [RabbitMQ queues](https://www.rabbitmq.com/docs/queues)
- Further reading (blog): [Kafka consumer groups](https://www.confluent.io/blog/dynamic-vs-static-kafka-consumer-rebalancing/)
