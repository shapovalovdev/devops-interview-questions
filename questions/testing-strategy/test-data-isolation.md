---
title: Design isolated test data
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design isolated test data

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

- Official documentation: [Testcontainers — guides](https://testcontainers.com/guides/)
- Manual or specification: [Software Engineering at Google — test doubles](https://abseil.io/resources/swe-book/html/ch13.html)
- Maintainer or personal blog: [Martin Fowler — object mother](https://martinfowler.com/bliki/ObjectMother.html)
- Technical blog: [Google Testing Blog — keep tests focused](https://testing.googleblog.com/2018/06/testing-on-toilet-keep-tests-focused.html)
- Hands-on guide: [pytest — how to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
