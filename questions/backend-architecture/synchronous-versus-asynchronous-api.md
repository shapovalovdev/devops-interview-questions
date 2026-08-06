---
title: Choose synchronous versus asynchronous API processing
theme: backend-architecture
difficulty: junior
type: scenario
tags: [http, event-driven, message-queues]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9110
    source_type: standard
    verified_on: 2026-08-06
---

# Choose synchronous versus asynchronous API processing

When should an API return a final result immediately versus accept work for later completion?

## Answer guide

- Use synchronous handling when the bounded work and dependencies can reliably meet the caller’s latency expectation. Use an accepted asynchronous operation when work is long-running, bursty, or needs durable retry and the client can observe a status resource or callback.
- Define the operation identifier, durable state transitions, timeout, retry, authorization, and completion contract. A 202 response only communicates acceptance; it does not prove the work succeeded, so expose a reliable way to learn the outcome.
- Avoid hiding slow work behind a synchronous endpoint until a load spike causes timeouts and duplicate submissions. An asynchronous design also fails without idempotency and dead-letter handling; test crashes between acceptance, dispatch, and result publication.

## References

- [HTTP Semantics: 202 Accepted](https://www.rfc-editor.org/rfc/rfc9110)
- Further reading (blog): [Stripe: usage-based billing](https://stripe.com/blog/how-we-built-it-usage-based-billing)

## What to learn next

- Official documentation: [AWS SQS developer guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- Manual or specification: [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Aphyr's blog](https://aphyr.com/)
- Technical blog: [Stripe engineering](https://stripe.com/blog/engineering)
- Hands-on guide: [RabbitMQ tutorials](https://www.rabbitmq.com/tutorials)
