---
title: Define a flaky-test quarantine policy
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://docs.pytest.org/en/stable/how-to/skipping.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch11.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Define a flaky-test quarantine policy

How should a team approach this testing strategy decision?

## Answer guide

- Start with the failure mode and choose the smallest reliable test boundary that proves the important behavior.
- Make environment, ownership, and test-data assumptions explicit; shared mutable state and uncontrolled timing make confidence misleading.
- Use evidence from deterministic checks and targeted integration tests to decide whether a change may proceed.
- Revisit the strategy after incidents; excessive slow checks can delay delivery without covering the highest-risk boundary.

## References

- [pytest — how to skip tests and mark expected failures](https://docs.pytest.org/en/stable/how-to/skipping.html)
- [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Further reading (blog): [Google Testing Blog — test flakiness, one of the main challenges of automated testing](https://testing.googleblog.com/2020/12/test-flakiness-one-of-main-challenges.html)

## What to learn next

- Official documentation: [pytest documentation](https://docs.pytest.org/en/stable/)
- Manual or specification: [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Maintainer or personal blog: [Martin Fowler — eradicating non-determinism in tests](https://martinfowler.com/articles/nonDeterminism.html)
- Technical blog: [Google Testing Blog — test flakiness, one of the main challenges of automated testing](https://testing.googleblog.com/2020/12/test-flakiness-one-of-main-challenges.html)
- Hands-on guide: [pytest — how to skip tests and mark expected failures](https://docs.pytest.org/en/stable/how-to/skipping.html)
