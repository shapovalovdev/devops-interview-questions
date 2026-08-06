---
title: Configure Kafka producer durability
theme: queue-messaging
difficulty: middle
type: scenario
tags: [kafka, message-queues, reliability, performance]
sources:
  - url: https://kafka.apache.org/documentation/#producerconfigs
    source_type: official-docs
    verified_on: 2026-08-06
---

# Configure Kafka producer durability

How would you configure a Kafka producer for durable business events, and what latency trade-off follows?

## Answer guide

- Use an appropriate replication factor and producer acknowledgement policy; `acks=all` waits for the leader's in-sync replica set, while acks less than all accepts more loss exposure. Enable idempotence for retry-safe producer semantics and use a retry policy compatible with it.
- Broker `min.insync.replicas` and the producer's acknowledgement setting work together: a producer cannot manufacture durability that an under-replicated cluster lacks. Monitor under-replicated partitions and rejected produces.
- Waiting for replicas adds latency and can reduce availability during replica loss. Do not “fix” an outage by weakening acknowledgements without explicitly accepting the data-loss consequence.

## References

- [Apache Kafka producer configuration](https://kafka.apache.org/documentation/#producerconfigs)
- Further reading (blog): [Apache Kafka producer internals](https://www.confluent.io/blog/kafka-producer-internals-preparing-event-data/)

## What to learn next

- Official documentation: [Apache Kafka producer configuration](https://kafka.apache.org/documentation/#producerconfigs)
- Manual or specification: [Apache Kafka protocol](https://kafka.apache.org/protocol)
- Maintainer or personal blog: [Matthias J. Sax — Gently Down the Stream](https://www.gentlydownthe.stream/)
- Technical blog: [Confluent technical blog](https://www.confluent.io/blog/)
- Hands-on guide: [Confluent Kafka tutorials](https://developer.confluent.io/tutorials/)
