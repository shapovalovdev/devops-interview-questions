---
title: Use shadow traffic safely
theme: testing-strategy
difficulty: staff
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Use shadow traffic safely

How should a team make this testing strategy decision?

## Answer guide

- Define the behavior and risk being controlled, then select evidence that is representative enough to influence a release decision.
- Keep dependencies, test data, and timing controlled so a passing result is reproducible and a failure is diagnosable.
- Make the cost, feedback time, and ownership explicit; use the result with code review and operational signals rather than as an isolated score.
- Review false positives and escaped defects after releases. A broad but untrusted test signal can slow delivery while masking meaningful gaps.

## References

- [Martin Fowler — practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Further reading (blog): [Google Testing Blog](https://testing.googleblog.com/)

## What to learn next

- Official documentation: [Google Testing Blog](https://testing.googleblog.com/)
- Manual or specification: [Software Engineering at Google — testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Maintainer or personal blog: [Martin Fowler](https://martinfowler.com/)
- Technical blog: [Netflix TechBlog](https://netflixtechblog.com/)
- Hands-on guide: [pytest documentation](https://docs.pytest.org/en/stable/)
