---
title: Control end-to-end test scope
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://playwright.dev/docs/best-practices
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch14.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Control end-to-end test scope

How should a team make this testing strategy decision?

## Answer guide

- Start from the production risk and choose a test boundary that proves the behavior without making feedback unnecessarily slow.
- Make dependencies, data ownership, and environment isolation explicit so results are reproducible and failures can be diagnosed.
- Treat test execution time and flake rate as product metrics; improve the signal before tightening a release gate.
- Review the strategy after escaped defects and architecture changes. More tests do not automatically improve confidence when the wrong boundary is exercised.

## References

- [Playwright — best practices](https://playwright.dev/docs/best-practices)
- [Software Engineering at Google — larger testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Further reading (blog): [Google Testing Blog — just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)

## What to learn next

- Official documentation: [Playwright — best practices](https://playwright.dev/docs/best-practices)
- Manual or specification: [Software Engineering at Google — larger testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Maintainer or personal blog: [Toby Clemson — testing strategies in a microservice architecture](https://martinfowler.com/articles/microservice-testing/)
- Technical blog: [Google Testing Blog — just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)
- Hands-on guide: [Playwright — writing tests](https://playwright.dev/docs/writing-tests)
