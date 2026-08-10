---
title: Use contract tests between services
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Use contract tests between services

How should an engineering team make this testing decision?

## Answer guide

- Start from the production risk and choose the smallest test boundary that can prove the behavior with realistic dependencies. Keep feedback fast enough for ordinary change flow.
- Make ownership, test data, and environment assumptions explicit. A test that relies on shared mutable state or timing is a reliability risk, not merely a slow check.
- Combine deterministic automated checks with targeted integration evidence. Measure failures and maintain the suite as a product; do not use coverage alone as proof of confidence.
- Revisit the mix after incidents and architecture changes. Over-investing in expensive end-to-end checks can slow delivery while still missing boundary failures.

## References

- [Martin Fowler — practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Further reading (blog): [Google Testing Blog](https://testing.googleblog.com/)

## What to learn next

- Official documentation: [OpenAPI Initiative — learn OpenAPI](https://learn.openapis.org/)
- Manual or specification: [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- Maintainer or personal blog: [Martin Fowler — contract test](https://martinfowler.com/bliki/ContractTest.html)
- Technical blog: [Spotify Engineering — testing of microservices](https://engineering.atspotify.com/2018/01/testing-of-microservices/)
- Hands-on guide: [Pact — how Pact works](https://docs.pact.io/getting_started/how_pact_works)
