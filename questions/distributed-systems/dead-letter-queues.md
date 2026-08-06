---
title: Operate a dead-letter queue
theme: distributed-systems
difficulty: senior
type: troubleshooting
tags: [message-queues, event-driven, recovery]
sources:
  - url: https://www.rabbitmq.com/docs/dlx
    source_type: official-docs
    verified_on: 2026-08-06
---

# Operate a dead-letter queue

What should happen to an event that repeatedly cannot be processed?

## Answer guide

- Move the failed delivery to a durable, access-controlled dead-letter path with original payload, headers, attempt count, error classification, consumer version, and correlation identifier. Alert on growth and classify whether the error is transient, malformed, incompatible, or a business rejection.
- Preserve the source event and define a replay process that is idempotent, rate-limited, and run only after the consumer or data defect is corrected. Set retention, ownership, privacy handling, and a documented final disposition rather than leaving messages indefinitely.
- A dead-letter queue is not a silent success path. Blind replay can repeat side effects, TTL or routing mistakes can loop a message, and inaccessible payloads can become data loss; test failure injection and ensure operators can inspect and repair safely.

## References

- [RabbitMQ: dead letter exchanges](https://www.rabbitmq.com/docs/dlx)
- Further reading (personal blog): [Aphyr: queues](https://aphyr.com/posts/351-jepsen-rabbitmq)

## What to learn next

- Official documentation: [RabbitMQ consumer acknowledgements](https://www.rabbitmq.com/docs/confirms)
- Manual or specification: [AMQP 0-9-1 model](https://www.rabbitmq.com/tutorials/amqp-concepts)
- Maintainer or personal blog: [Aphyr's blog](https://aphyr.com/)
- Technical blog: [RabbitMQ: dead lettering](https://www.rabbitmq.com/blog/)
- Hands-on guide: [RabbitMQ tutorials](https://www.rabbitmq.com/tutorials)
