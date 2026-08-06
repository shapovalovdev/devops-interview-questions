---
title: Design a durable background job contract
theme: backend-architecture
difficulty: middle
type: scenario
tags: [message-queues, reliability, event-driven]
sources:
  - url: https://www.rabbitmq.com/docs/confirms
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a durable background job contract

What information and guarantees does a backend job queue need?

## Answer guide

- Define a durable job identifier, payload schema version, owner, schedule, retry policy, deadline, idempotency behavior, and final disposition. A worker acknowledges only after durable success, and its handler must tolerate redelivery.
- Bound concurrency by downstream capacity, preserve observability from request to job, and operate a dead-letter or repair route with access controls. Track queue age, attempts, execution duration, and poison-job counts.
- At-least-once delivery means duplicate execution is normal after a crash. Acknowledging before the effect persists loses work, while unlimited retries hide permanent defects; test worker termination at each boundary and intentionally malformed jobs.

## References

- [RabbitMQ: consumer acknowledgements](https://www.rabbitmq.com/docs/confirms)
- Further reading (personal blog): [Aphyr: RabbitMQ](https://aphyr.com/posts/351-jepsen-rabbitmq)

## What to learn next

- Official documentation: [RabbitMQ tutorials](https://www.rabbitmq.com/tutorials)
- Manual or specification: [AMQP concepts](https://www.rabbitmq.com/tutorials/amqp-concepts)
- Maintainer or personal blog: [Aphyr's blog](https://aphyr.com/)
- Technical blog: [RabbitMQ blog](https://www.rabbitmq.com/blog/)
- Hands-on guide: [RabbitMQ work queues tutorial](https://www.rabbitmq.com/tutorials/tutorial-two-python)
