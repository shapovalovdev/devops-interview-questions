---
title: Plan Kafka partition capacity
theme: queue-messaging
difficulty: senior
type: scenario
tags: [kafka, message-queues, capacity-planning, performance, reliability]
sources:
  - url: https://kafka.apache.org/documentation/#design
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://kafka.apache.org/documentation/#basic_ops
    source_type: official-docs
    verified_on: 2026-08-06
---

# Plan Kafka partition capacity

How do you choose partition count for a new high-volume Kafka topic?

## Answer guide

- Model peak ingress, record size, retention, replication, consumer throughput, key distribution, recovery time, and broker resources. Partitions create parallelism but also consume metadata, file handles, replication, and recovery capacity.
- Start with measured producer/consumer throughput and growth headroom, then load-test failure and catch-up cases. Size consumers no higher than useful partition concurrency and watch for hot partitions.
- Adding partitions later is possible but can change key mapping and ordering assumptions. A large count chosen only for “future scale” can make controller operations and recovery slower; document the rationale and revisit it with data.

## References

- [Apache Kafka design](https://kafka.apache.org/documentation/#design)
- [Apache Kafka operations](https://kafka.apache.org/documentation/#basic_ops)
- Further reading (blog): [Choosing Kafka partitions](https://www.confluent.io/blog/how-choose-number-topics-partitions-kafka-cluster/)
