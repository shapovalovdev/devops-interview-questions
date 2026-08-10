---
title: Design a focused unit test
theme: testing-strategy
difficulty: junior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://abseil.io/resources/swe-book/html/ch12.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://docs.pytest.org/en/stable/how-to/fixtures.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design a focused unit test

How should a team make this testing strategy decision?

## Answer guide

- Define the behavior and risk being controlled, then choose the smallest test boundary that provides reliable evidence.
- Keep data, dependencies, and environment assumptions explicit so results are reproducible and failures can be diagnosed.
- Balance execution cost against feedback speed and release confidence; use the check alongside review and operational signals.
- Reassess the strategy after incidents and architecture changes because an unowned test can become a source of false confidence.

## References

- [Software Engineering at Google — unit testing](https://abseil.io/resources/swe-book/html/ch12.html)
- [pytest — how to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- Further reading (blog): [Google Testing Blog — tests too DRY? make them DAMP!](https://testing.googleblog.com/2019/12/testing-on-toilet-tests-too-dry-make.html)

## What to learn next

- Official documentation: [pytest documentation](https://docs.pytest.org/en/stable/)
- Manual or specification: [Software Engineering at Google — unit testing](https://abseil.io/resources/swe-book/html/ch12.html)
- Maintainer or personal blog: [Martin Fowler — unit test](https://martinfowler.com/bliki/UnitTest.html)
- Technical blog: [Google Testing Blog — tests too DRY? make them DAMP!](https://testing.googleblog.com/2019/12/testing-on-toilet-tests-too-dry-make.html)
- Hands-on guide: [pytest — how to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
