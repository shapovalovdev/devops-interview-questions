---
title: Name test cases for diagnosis
theme: testing-strategy
difficulty: junior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://docs.pytest.org/en/stable/explanation/goodpractices.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch12.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Name test cases for diagnosis

How should a team make this testing strategy decision?

## Answer guide

- Define the behavior and risk being controlled, then choose the smallest test boundary that provides reliable evidence.
- Keep data, dependencies, and environment assumptions explicit so results are reproducible and failures can be diagnosed.
- Balance execution cost against feedback speed and release confidence; use the check alongside review and operational signals.
- Reassess the strategy after incidents and architecture changes because an unowned test can become a source of false confidence.

## References

- [pytest — good integration practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [Software Engineering at Google — unit testing](https://abseil.io/resources/swe-book/html/ch12.html)
- Further reading (blog): [Google Testing Blog — writing descriptive test names](https://testing.googleblog.com/2014/10/testing-on-toilet-writing-descriptive.html)

## What to learn next

- Official documentation: [pytest documentation](https://docs.pytest.org/en/stable/)
- Manual or specification: [Software Engineering at Google — unit testing](https://abseil.io/resources/swe-book/html/ch12.html)
- Maintainer or personal blog: [Vladimir Khorikov — you are naming your tests wrong](https://enterprisecraftsmanship.com/posts/you-naming-tests-wrong/)
- Technical blog: [Google Testing Blog — writing descriptive test names](https://testing.googleblog.com/2014/10/testing-on-toilet-writing-descriptive.html)
- Hands-on guide: [pytest — good integration practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
