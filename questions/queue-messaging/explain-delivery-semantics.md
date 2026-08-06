---
title: Explain at-most-once, at-least-once, and exactly-once claims
theme: queue-messaging
difficulty: junior
type: theory
tags: [kafka, rabbitmq, message-queues, reliability]
sources:
  - url: https://kafka.apache.org/documentation/#semantics
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rabbitmq.com/docs/confirms
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain at-most-once, at-least-once, and exactly-once claims

What do delivery semantics mean, and why is “exactly once” usually incomplete by itself?

## Answer guide

- At-most-once accepts loss rather than retrying. At-least-once retries when acknowledgement is uncertain, so a consumer can see a duplicate. These are end-to-end properties involving producer, broker, consumer, and the side effect.
- Kafka provides idempotent and transactional mechanisms for supported read-process-write flows, but an external database, email, or payment call needs its own idempotency key or transactional boundary. RabbitMQ confirms and consumer acknowledgements also do not make an arbitrary external side effect exactly once.
- State the scope whenever claiming exactly once. Acknowledging before processing loses work; acknowledging after a non-idempotent effect can duplicate it after a crash. Design compensation, deduplication, and observability for either case.

## References

- [Apache Kafka message delivery semantics](https://kafka.apache.org/documentation/#semantics)
- [RabbitMQ publisher confirms and consumer acknowledgements](https://www.rabbitmq.com/docs/confirms)
- Further reading (blog): [Kafka data access semantics](https://www.confluent.io/blog/apache-kafka-data-access-semantics-consumers-and-membership/)
