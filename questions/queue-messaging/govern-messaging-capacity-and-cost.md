---
title: Govern messaging capacity and cost
theme: queue-messaging
difficulty: staff
type: scenario
tags: [kafka, rabbitmq, message-queues, capacity-planning, cost-optimization, governance]
sources:
  - url: https://kafka.apache.org/documentation/#basic_ops
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.rabbitmq.com/docs/memory
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern messaging capacity and cost

How should a platform team govern messaging capacity without surprising product teams during an incident?

## Answer guide

- Charge or report on retained bytes, replication, partitions/queues, ingress-egress, connections, and recovery reserve. Forecast from growth, retention, peak replay, and failure catch-up—not average traffic alone.
- Set explicit quotas, retention defaults, backlog and disk headroom policies, then provide safe exceptions for critical workloads. Communicate approaching limits early and make ownership of idle topics/queues visible.
- Emergency deletion or retention reduction can destroy replay and forensic value. Prefer throttling, producer backpressure, and planned archival, with a documented business decision for any data-loss action.

## References

- [Apache Kafka operations](https://kafka.apache.org/documentation/#basic_ops)
- [RabbitMQ memory alarms](https://www.rabbitmq.com/docs/memory)
- Further reading (blog): [Kafka capacity planning](https://www.confluent.io/blog/how-to-choose-the-right-number-of-kafka-partitions/)

## What to learn next

- Official documentation: [Apache Kafka operations](https://kafka.apache.org/documentation/#basic_ops)
- Manual or specification: [AsyncAPI specification](https://www.asyncapi.com/docs/reference/specification/latest)
- Maintainer or personal blog: [Ben Stopford — distributed-systems articles](https://www.confluent.io/blog/author/ben-stopford/)
- Technical blog: [Redpanda engineering blog](https://www.redpanda.com/blog)
- Hands-on guide: [AsyncAPI tutorials](https://www.asyncapi.com/docs/tutorials)
