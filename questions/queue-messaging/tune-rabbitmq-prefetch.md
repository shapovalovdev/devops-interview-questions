---
title: Tune RabbitMQ consumer prefetch
theme: queue-messaging
difficulty: middle
type: scenario
tags: [rabbitmq, message-queues, performance, reliability]
sources:
  - url: https://www.rabbitmq.com/docs/consumer-prefetch
    source_type: official-docs
    verified_on: 2026-08-06
---

# Tune RabbitMQ consumer prefetch

What does RabbitMQ prefetch control and how do you set it safely?

## Answer guide

- Prefetch limits outstanding unacknowledged deliveries for a consumer or channel, providing application-level backpressure. A small value improves fairness and crash recovery; a larger one can improve throughput when work is uniform and memory is sufficient.
- Start from processing latency, concurrency, memory, and downstream capacity, then load-test. Keep acknowledgement after the durable effect so an in-flight buffer is recoverable.
- An excessive prefetch can concentrate thousands of messages on a slow consumer, inflate memory, and delay redelivery after failure. A value of one can underutilize a high-latency worker; observe unacked counts and end-to-end latency.

## References

- [RabbitMQ consumer prefetch](https://www.rabbitmq.com/docs/consumer-prefetch)
- Further reading (blog): [RabbitMQ prefetch explained](https://www.rabbitmq.com/blog/2012/04/25/rabbitmq-performance-measurements-part-2)

## What to learn next

- Official documentation: [RabbitMQ consumer prefetch](https://www.rabbitmq.com/docs/consumer-prefetch)
- Manual or specification: [AMQP 0-9-1 specification](https://www.rabbitmq.com/resources/specs/amqp0-9-1.pdf)
- Maintainer or personal blog: [RabbitMQ team — RabbitMQ engineering blog](https://www.rabbitmq.com/blog/)
- Technical blog: [CloudAMQP technical blog](https://www.cloudamqp.com/blog/)
- Hands-on guide: [RabbitMQ consumer guide](https://www.rabbitmq.com/docs/consumers)
