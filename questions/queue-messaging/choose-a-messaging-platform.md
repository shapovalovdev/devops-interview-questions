---
title: Choose a messaging platform for an organization
theme: queue-messaging
difficulty: staff
type: scenario
tags: [kafka, rabbitmq, message-queues, platform-engineering, governance, must-know]
sources:
  - url: https://kafka.apache.org/documentation/#intro_concepts_and_terms
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rabbitmq.com/docs/queues
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose a messaging platform for an organization

How would you decide whether the platform should offer Kafka, RabbitMQ, both, or neither as a supported service?

## Answer guide

- Start with dominant workloads: replayable event streams, independent consumer groups, and high-throughput ordered partitions favor Kafka; routed work distribution and request/job patterns often favor RabbitMQ. A managed cloud service may be the right operational trade-off.
- Compare durability, ordering, latency, retention, tenant isolation, skills, compliance, cost, and 24/7 ownership. Publish approved use cases and an escalation path instead of letting every team invent a broker topology.
- Supporting both increases cognitive and operational cost; mandating one can force a poor model. Measure adoption and incident burden, set migration guidance, and avoid equating “event-driven” with a particular product.

## References

- [Apache Kafka concepts and terms](https://kafka.apache.org/documentation/#intro_concepts_and_terms)
- [RabbitMQ queues](https://www.rabbitmq.com/docs/queues)
- Further reading (blog): [Kafka versus RabbitMQ](https://www.confluent.io/blog/kafka-vs-rabbitmq/)

## What to learn next

- Official documentation: [AsyncAPI documentation](https://www.asyncapi.com/docs)
- Manual or specification: [AsyncAPI specification](https://www.asyncapi.com/docs/reference/specification/latest)
- Maintainer or personal blog: [Ben Stopford — distributed-systems articles](https://www.confluent.io/blog/author/ben-stopford/)
- Technical blog: [Redpanda engineering blog](https://www.redpanda.com/blog)
- Hands-on guide: [AsyncAPI tutorials](https://www.asyncapi.com/docs/tutorials)
