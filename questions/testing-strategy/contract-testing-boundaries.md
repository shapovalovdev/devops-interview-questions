---
title: Use contract tests between services
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://spec.openapis.org/oas/latest.html
    source_type: standard
    verified_on: 2026-08-10
  - url: https://docs.pact.io/getting_started/how_pact_works
    source_type: official-docs
    verified_on: 2026-08-10
---

# Use contract tests between services

Every internal service publishes an OpenAPI document, and the end-to-end suite that is supposed to catch integration breakage fails constantly for unrelated reasons. Where does a contract test belong in that stack, and what does schema validation give you that a consumer-driven contract does not?

## Answer guide

- Put the boundary at the wire format between two independently deployable units. A contract test asserts that the request the consumer emits is one the provider accepts, and that the response satisfies the fields the consumer depends on. It asserts nothing about business outcomes, cross-service workflows, or database state, and anything that needs both services running at once has left contract-testing territory and become an integration test.
- Schema-first and consumer-driven checks answer different questions and most estates need both. An OpenAPI or JSON Schema check is provider-owned and complete — every endpoint and field, validated in both directions — and it is enforceable on every pull request with a linter plus a spec differ such as oasdiff or Spectral, catching a narrowed type or a newly required field before any consumer exists. A pact is consumer-owned and deliberately partial, but it tells you whether a change breaks a consumer that is actually deployed.
- Neither catches semantics. A field that keeps its type but changes meaning — cents to dollars, UTC to local time — an enum that gains a value the consumer's exhaustive switch does not handle, or pagination that silently stops being stable all pass a schema check cleanly. Push what you can into the contract explicitly: units in field names, a stated open-or-closed enum policy, additive-only change rules, and an explicit compatibility window. Accept that the rest needs a narrow integration test rather than pretending the contract covers it.
- Failure modes: generating the OpenAPI document from the implementation, so it can never disagree with the code and detects nothing; validating requests but not responses; contract suites that quietly acquire a real database and become slow integration tests; and treating green contracts as permission to ignore deployment order, when a backward-incompatible provider change shipped before its consumers is still an outage no test caught.

## References

- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Pact — how Pact works](https://docs.pact.io/getting_started/how_pact_works)
- Further reading (blog): [Martin Fowler — contract test](https://martinfowler.com/bliki/ContractTest.html)

## What to learn next

- Official documentation: [OpenAPI Initiative — learn OpenAPI](https://learn.openapis.org/)
- Manual or specification: [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- Maintainer or personal blog: [Martin Fowler — contract test](https://martinfowler.com/bliki/ContractTest.html)
- Technical blog: [Spotify Engineering — testing of microservices](https://engineering.atspotify.com/2018/01/testing-of-microservices/)
- Hands-on guide: [Pact — how Pact works](https://docs.pact.io/getting_started/how_pact_works)
