---
title: Define integration test data contracts
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://json-schema.org/specification
    source_type: standard
    verified_on: 2026-08-10
  - url: https://docs.confluent.io/platform/current/schema-registry/index.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Define integration test data contracts

Two teams exchange events through a Kafka topic, and a producer change that added a required field broke every consumer overnight. What compatibility rules and tests should have caught that before it shipped?

## Answer guide

- Make the schema the contract and register it. With Schema Registry the producer's serialiser registers a schema per subject and the registry rejects a version that violates the configured compatibility rule, so the check happens at the write path rather than in a review. The rule that matters here is BACKWARD, meaning a consumer on the new schema can read data written with the previous one: adding a field with a default is allowed, adding a required field with no default is not, and that single setting would have blocked the change.
- Pick the compatibility mode from the deployment order you actually use. BACKWARD lets consumers upgrade first; FORWARD lets producers upgrade first; FULL permits either but forbids most changes; and the TRANSITIVE variants check against every historical version rather than only the previous one, which is what you want for a topic with long retention where a replay reads year-old records. Removing a field is backward-compatible and forward-breaking — the asymmetry is the point, and choosing the wrong mode makes the gate agree with a change that breaks the side you did not think about.
- Test the rule, do not trust it. Keep golden sample payloads from each supported version in the repository and assert current consumer code parses all of them, so a consumer that starts requiring a newly added field is caught even though the registry approved it. Validate against JSON Schema or Avro in CI rather than at runtime only, run a compatibility check as a pull-request gate against the registry, and version the topic itself when you need a genuinely breaking change, running both for the retention window.
- Failure modes: a consumer that deserialises leniently but then dereferences a field it assumed present, turning a compatible schema change into a null-pointer outage; `auto.register.schemas` left enabled in production so the first producer to start defines the contract; compatibility set on the wrong subject naming strategy so the check runs against a schema nobody uses; and semantic changes — a currency switching units, an enum gaining a member — that every structural rule permits.

## References

- [JSON Schema specification](https://json-schema.org/specification)
- [Confluent — Schema Registry documentation](https://docs.confluent.io/platform/current/schema-registry/index.html)
- Further reading (blog): [AWS Builders' Library — ensuring rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/)

## What to learn next

- Official documentation: [Confluent — Schema Registry documentation](https://docs.confluent.io/platform/current/schema-registry/index.html)
- Manual or specification: [JSON Schema specification](https://json-schema.org/specification)
- Maintainer or personal blog: [Martin Fowler — tolerant reader](https://martinfowler.com/bliki/TolerantReader.html)
- Technical blog: [AWS Builders' Library — ensuring rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/)
- Hands-on guide: [JSON Schema — creating your first schema](https://json-schema.org/learn/getting-started-step-by-step)
