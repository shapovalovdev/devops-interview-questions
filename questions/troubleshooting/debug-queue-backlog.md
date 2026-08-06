---
title: Triage a growing asynchronous work backlog
theme: troubleshooting
difficulty: middle
type: troubleshooting
tags: [troubleshooting, message-queues, capacity-planning, monitoring, reliability]
sources:
  - url: https://sre.google/sre-book/handling-overload/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Triage a growing asynchronous work backlog
## Answer guide
- Measure arrival rate, successful completion rate, age of oldest work, retry rate, consumer health, and downstream latency. A rising depth is a symptom; determine whether production exceeds consumption or messages are blocked by one poison input.
- Inspect consumer concurrency, partition ownership, acknowledgements, resource limits, and dependency errors. Scale only after verifying the downstream can accept more work and message handling is idempotent.
- Apply backpressure, rate limits, dead-letter handling, or a bounded replay plan and monitor end-to-end correctness. Purging a queue or blindly retrying can permanently lose work or multiply side effects.
## References
- [Google SRE Book — Handling Overload](https://sre.google/sre-book/handling-overload/)
- [Apache Kafka documentation](https://kafka.apache.org/documentation/)
- Further reading (blog): [Chris Richardson — messaging](https://microservices.io/)
## What to learn next
- Free book: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official guide: [RabbitMQ documentation](https://www.rabbitmq.com/docs)
- Official guide: [Kafka documentation](https://kafka.apache.org/documentation/)
- Personal technical blog: [Chris Richardson](https://microservices.io/)
- Technical blog: [Confluent blog](https://www.confluent.io/blog/)
