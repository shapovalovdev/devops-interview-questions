---
title: Set test-suite execution policy
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Set test-suite execution policy

How should a team make this testing strategy decision?

## Answer guide

- Define the behavior and risk being controlled, then choose the smallest test boundary that provides reliable evidence.
- Keep data, dependencies, and environment assumptions explicit so results are reproducible and failures can be diagnosed.
- Balance execution cost against feedback speed and release confidence; use the check alongside review and operational signals.
- Reassess the strategy after incidents and architecture changes because an unowned test can become a source of false confidence.

## References

- [Martin Fowler — practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Further reading (blog): [Google Testing Blog](https://testing.googleblog.com/)

## What to learn next

- Official documentation: [GitHub Actions documentation](https://docs.github.com/en/actions)
- Manual or specification: [Software Engineering at Google — larger testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Maintainer or personal blog: [Martin Fowler — on the diverse and fantastical shapes of testing](https://martinfowler.com/articles/2021-test-shapes.html)
- Technical blog: [Slack Engineering — handling flaky tests at scale](https://slack.engineering/handling-flaky-tests-at-scale-auto-detection-suppression/)
- Hands-on guide: [pytest — how to mark test functions with attributes](https://docs.pytest.org/en/stable/how-to/mark.html)
