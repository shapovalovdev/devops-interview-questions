---
title: Choose Kafka retention or log compaction
theme: queue-messaging
difficulty: middle
type: scenario
tags: [kafka, message-queues, storage, reliability]
sources:
  - url: https://kafka.apache.org/documentation/#compaction
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose Kafka retention or log compaction

When should a Kafka topic use time/size retention, log compaction, or both?

## Answer guide

- Retention removes old log segments by age or size, making a replay window finite. Compaction retains at least the latest record for each key after cleaning, which fits reconstructing current keyed state.
- Compaction is asynchronous and does not mean every historical record disappears immediately; tombstones and delete-retention affect key deletion. Use a key consistently and validate consumers can handle duplicate historical updates.
- Combining policies can be useful but is not an archive guarantee. Set capacity and recovery requirements first; shortening retention to relieve disk pressure can destroy the only replay path.

## References

- [Apache Kafka log compaction](https://kafka.apache.org/documentation/#compaction)
- Further reading (blog): [Kafka log compaction](https://www.confluent.io/blog/log-compaction-in-apache-kafka-key-benefits-and-best-practices/)
