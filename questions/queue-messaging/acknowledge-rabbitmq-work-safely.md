---
title: Acknowledge RabbitMQ work safely
theme: queue-messaging
difficulty: junior
type: scenario
tags: [rabbitmq, message-queues, reliability, troubleshooting]
sources:
  - url: https://www.rabbitmq.com/docs/confirms
    source_type: official-docs
    verified_on: 2026-08-06
---

# Acknowledge RabbitMQ work safely

Where should a worker acknowledge a RabbitMQ delivery that writes to a database?

## Answer guide

- Use manual acknowledgement and acknowledge only after the database operation has reached its durable success boundary. If the worker dies first, RabbitMQ can requeue/redeliver the unacknowledged message.
- Make the database operation idempotent with a stable message identifier or a uniqueness constraint. A crash after the database commit but before the acknowledgement produces a legitimate duplicate delivery.
- Bound concurrent unacknowledged work with prefetch and monitor redeliveries. Auto-ack is appropriate only when losing the work is acceptable; it is not a reliability optimization for durable writes.

## References

- [RabbitMQ consumer acknowledgements](https://www.rabbitmq.com/docs/confirms)
- Further reading (blog): [RabbitMQ reliability guide](https://www.rabbitmq.com/blog/2020/11/10/using-python-rabbitmq-client-libraries)
