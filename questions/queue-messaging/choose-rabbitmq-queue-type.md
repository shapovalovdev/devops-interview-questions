---
title: Choose a RabbitMQ queue type
theme: queue-messaging
difficulty: middle
type: scenario
tags: [rabbitmq, message-queues, reliability, performance]
sources:
  - url: https://www.rabbitmq.com/docs/quorum-queues
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a RabbitMQ queue type

When would you choose a RabbitMQ quorum queue rather than a classic queue?

## Answer guide

- Quorum queues are replicated, consensus-based queues intended for stronger data safety and predictable recovery; classic queues have different replication and performance characteristics. Choose based on the workload's durability, availability, feature, and latency needs.
- Test the current RabbitMQ version and topology: queue type is a declaration-time decision with operational consequences, and quorum queue sizing needs a healthy odd-sized replica group across failure domains.
- Do not assume replication removes the need for publisher confirms, consumer idempotency, or capacity planning. A poorly sized cluster can become unavailable rather than safely accept under-replicated work.

## References

- [RabbitMQ quorum queues](https://www.rabbitmq.com/docs/quorum-queues)
- Further reading (blog): [RabbitMQ quorum queues](https://www.rabbitmq.com/blog/2019/08/28/quorum-queues-local-delivery)

## What to learn next

- Official documentation: [RabbitMQ quorum queues](https://www.rabbitmq.com/docs/quorum-queues)
- Manual or specification: [AMQP 0-9-1 specification](https://www.rabbitmq.com/resources/specs/amqp0-9-1.pdf)
- Maintainer or personal blog: [RabbitMQ team — RabbitMQ engineering blog](https://www.rabbitmq.com/blog/)
- Technical blog: [CloudAMQP technical blog](https://www.cloudamqp.com/blog/)
- Hands-on guide: [RabbitMQ tutorials](https://www.rabbitmq.com/tutorials)
