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

- Official documentation: [Google Testing Blog](https://testing.googleblog.com/)
- Manual or specification: [The Google Testing Blog book](https://abseil.io/resources/swe-book/html/ch14.html)
- Maintainer or personal blog: [Martin Fowler](https://martinfowler.com/)
- Technical blog: [Netflix TechBlog](https://netflixtechblog.com/)
- Hands-on guide: [pytest documentation](https://docs.pytest.org/en/stable/)
