---
title: Explain Kafka topics and partitions
theme: queue-messaging
difficulty: junior
type: theory
tags: [kafka, message-queues, event-driven, performance]
sources:
  - url: https://kafka.apache.org/documentation/#intro_concepts_and_terms
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Kafka topics and partitions

What is a Kafka topic partition, and what ordering guarantee does it provide?

## Answer guide

- A topic is divided into partitions, each an append-only ordered log. Kafka assigns records offsets within a partition; the order guarantee is per partition, not across the whole topic.
- A producer key commonly selects a partition so all events for an entity retain order. Adding partitions increases potential parallelism but changes key-to-partition mapping and cannot create a global ordering guarantee.
- Hot keys can make one partition the bottleneck, while more consumers than partitions leave consumers idle. Design key choice, partition count, retention, and consumer concurrency together; changing them during an incident can make replay and ordering harder to reason about.

## References

- [Apache Kafka concepts and terms](https://kafka.apache.org/documentation/#intro_concepts_and_terms)
- Further reading (blog): [Multi-threaded Kafka consumption](https://www.confluent.io/blog/kafka-consumer-multi-threaded-messaging/)
