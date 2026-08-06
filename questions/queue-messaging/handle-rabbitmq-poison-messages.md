---
title: Handle RabbitMQ poison messages
theme: queue-messaging
difficulty: middle
type: troubleshooting
tags: [rabbitmq, message-queues, troubleshooting, reliability]
sources:
  - url: https://www.rabbitmq.com/docs/nack
    source_type: official-docs
    verified_on: 2026-08-06
---

# Handle RabbitMQ poison messages

A message keeps failing and being redelivered. What should the consumer do?

## Answer guide

- Identify whether the failure is permanent (invalid schema or missing required data) or transient (dependency outage). Reject or negatively acknowledge with a deliberate requeue decision; do not retry permanently bad data forever.
- Use a bounded retry policy and dead-letter route, record the message identity and failure reason, and make processing idempotent. Quorum queues can enforce a delivery limit, but the application still needs a remediation path.
- A blind `requeue=true` loop consumes broker and worker capacity, amplifies logs, and prevents newer work from progressing. Alert on redelivery count, dead-letter volume, and age.

## References

- [RabbitMQ negative acknowledgements](https://www.rabbitmq.com/docs/nack)
- Further reading (blog): [Poison messages and RabbitMQ](https://www.rabbitmq.com/blog/2010/08/03/well-ill-let-you-off-this-time)
