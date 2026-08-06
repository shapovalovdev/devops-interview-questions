---
title: Triage Kafka consumer lag
theme: queue-messaging
difficulty: middle
type: troubleshooting
tags: [kafka, message-queues, monitoring, troubleshooting]
sources:
  - url: https://kafka.apache.org/documentation/#basic_ops_monitoring
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage Kafka consumer lag

Consumer lag is growing. What do you investigate before scaling consumers?

## Answer guide

- Compare produced rate, consumed rate, lag by partition, processing latency, errors, rebalance activity, and broker health. Lag is the distance between a group's committed offset and the log end, not a diagnosis.
- Check for a hot partition or slow downstream dependency: adding consumers cannot exceed partition parallelism and does not help a single ordered hot key. Verify that consumers are assigned partitions and are committing progress.
- Scale only after locating the constraint, and protect dependencies with rate limits or backpressure. Retention can expire unprocessed records; alert on time-to-retention as well as raw lag.

## References

- [Apache Kafka monitoring](https://kafka.apache.org/documentation/#basic_ops_monitoring)
- Further reading (blog): [Kafka consumer lag monitoring](https://www.confluent.io/blog/kafka-lag-monitoring-and-metrics-at-appsflyer/)

## What to learn next

- Official documentation: [Apache Kafka monitoring](https://kafka.apache.org/documentation/#basic_ops_monitoring)
- Manual or specification: [Apache Kafka protocol](https://kafka.apache.org/protocol)
- Maintainer or personal blog: [Matthias J. Sax — Gently Down the Stream](https://www.gentlydownthe.stream/)
- Technical blog: [Confluent technical blog](https://www.confluent.io/blog/)
- Hands-on guide: [Confluent Kafka tutorials](https://developer.confluent.io/tutorials/)
