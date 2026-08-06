---
title: Manage event schema evolution
theme: queue-messaging
difficulty: senior
type: scenario
tags: [kafka, rabbitmq, message-queues, event-driven, governance]
sources:
  - url: https://kafka.apache.org/documentation/#intro_concepts_and_terms
    source_type: official-docs
    verified_on: 2026-08-06
---

# Manage event schema evolution

How do you evolve a published event without breaking old consumers or replay?

## Answer guide

- Treat an event schema as a versioned public contract. Prefer additive, optional fields with documented defaults; keep event type, schema version, producer, and correlation identifiers explicit.
- Validate compatibility in CI against registered or representative consumer contracts, deploy consumers that tolerate the new form before producers emit it, and retain decoders needed for the replay window.
- Renaming a field or changing its meaning is a compatibility break even if serialization succeeds. Version the event or provide a migration stream; do not overwrite historical facts to hide a contract error.

## References

- [Apache Kafka concepts and terms](https://kafka.apache.org/documentation/#intro_concepts_and_terms)
- Further reading (blog): [Schema evolution with Kafka](https://www.confluent.io/blog/stream-data-quality-why-it-matters/)
