---
title: Explain RabbitMQ exchanges, bindings, and queues
theme: queue-messaging
difficulty: junior
type: theory
tags: [rabbitmq, message-queues, event-driven, reliability]
sources:
  - url: https://www.rabbitmq.com/docs/exchanges
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain RabbitMQ exchanges, bindings, and queues

How does a RabbitMQ publisher route a message to the right consumer?

## Answer guide

- Publishers send to an exchange, not directly to a consumer. Exchange type and bindings decide which queue or queues receive a message: direct matches keys, topic matches patterns, fanout broadcasts, and headers uses headers.
- Consumers receive from queues and acknowledge only after durable processing. Separate queues let independent workloads scale and fail independently, while a fanout can deliberately copy one publication to several queues.
- An unmatched mandatory publication, an accidental broad topic binding, or a missing queue policy can silently lose intended work or create an unbounded backlog. Declare and test routing topology as code.

## References

- [RabbitMQ exchanges and bindings](https://www.rabbitmq.com/docs/exchanges)
- Further reading (blog): [RabbitMQ topic exchanges](https://www.rabbitmq.com/blog/2010/09/14/very-fast-and-scalable-topic-routing-part-1)
