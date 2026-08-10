---
title: Choose integration test boundaries
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://testcontainers.com/guides/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch13.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Choose integration test boundaries

How should a team make this testing strategy decision?

## Answer guide

- Start from the production risk and choose a test boundary that proves the behavior without making feedback unnecessarily slow.
- Make dependencies, data ownership, and environment isolation explicit so results are reproducible and failures can be diagnosed.
- Treat test execution time and flake rate as product metrics; improve the signal before tightening a release gate.
- Review the strategy after escaped defects and architecture changes. More tests do not automatically improve confidence when the wrong boundary is exercised.

## References

- [Testcontainers — guides](https://testcontainers.com/guides/)
- [Software Engineering at Google — test doubles](https://abseil.io/resources/swe-book/html/ch13.html)
- Further reading (blog): [Spotify Engineering — testing of microservices](https://engineering.atspotify.com/2018/01/testing-of-microservices/)

## What to learn next

- Official documentation: [Testcontainers — guides](https://testcontainers.com/guides/)
- Manual or specification: [Software Engineering at Google — test doubles](https://abseil.io/resources/swe-book/html/ch13.html)
- Maintainer or personal blog: [Martin Fowler — integration test](https://martinfowler.com/bliki/IntegrationTest.html)
- Technical blog: [Spotify Engineering — testing of microservices](https://engineering.atspotify.com/2018/01/testing-of-microservices/)
- Hands-on guide: [Testcontainers — getting started](https://testcontainers.com/getting-started/)
