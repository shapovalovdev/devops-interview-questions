---
title: Commit Kafka offsets after processing effects
theme: queue-messaging
difficulty: middle
type: scenario
tags: [kafka, message-queues, reliability, databases]
sources:
  - url: https://kafka.apache.org/documentation/#consumerconfigs
    source_type: official-docs
    verified_on: 2026-08-06
---

# Commit Kafka offsets after processing effects

What offset-commit order should a Kafka consumer use when it writes a record to an external database?

## Answer guide

- Commit after the database effect succeeds; committing first can skip work permanently if the process crashes. Committing after processing permits replay if the commit is lost.
- A replay can repeat a completed write, so use an idempotency key, upsert, or an inbox/outbox-style transaction. Offset commits are consumer progress markers, not a distributed transaction with an external database.
- Commit only offsets for completed contiguous records in each partition and handle rebalance revocation carefully. Long processing without polling can trigger group loss and duplicate concurrent work.

## References

- [Apache Kafka consumer configuration](https://kafka.apache.org/documentation/#consumerconfigs)
- Further reading (blog): [Kafka consumer design](https://docs.confluent.io/kafka/design/consumer-design.html)
