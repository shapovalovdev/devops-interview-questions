---
title: Evolve an event schema safely
theme: distributed-systems
difficulty: middle
type: scenario
tags: [event-driven, kafka, delivery]
sources:
  - url: https://kafka.apache.org/documentation/#design
    source_type: official-docs
    verified_on: 2026-08-06
---

# Evolve an event schema safely

How do you add fields or change meaning in an event consumed by independently deployed services?

## Answer guide

- Treat an event schema and its semantics as a published compatibility contract. Add optional fields with defaults where the serialization and consumers support it, version the event intentionally, and preserve old interpretation until all retained events and consumers no longer require it.
- Validate producer and consumer compatibility in CI using representative old and new payloads. Include event type, schema version, producer version, correlation identifier, and a clear migration or deprecation window in the contract.
- Renaming a field can be backward-compatible syntactically while changing meaning operationally. Consumers can lag for months, replays can read old records, and an unannounced incompatible change can poison a partition or silently compute the wrong business result.

## References

- [Apache Kafka: design](https://kafka.apache.org/documentation/#design)
- Further reading (personal blog): [Martin Kleppmann: turning the database inside out](https://martin.kleppmann.com/2015/03/27/repeatable-read-transactions-in-postgresql.html)

## What to learn next

- Official documentation: [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html)
- Manual or specification: [Apache Avro specification](https://avro.apache.org/docs/1.12.0/specification/)
- Maintainer or personal blog: [Martin Kleppmann's blog](https://martin.kleppmann.com/)
- Technical blog: [Confluent: schema evolution](https://developer.confluent.io/)
- Hands-on guide: [Kafka quickstart](https://kafka.apache.org/quickstart)
