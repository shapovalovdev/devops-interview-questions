---
title: Model test execution cost
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Model test execution cost

How should a team decide which tests run at each delivery stage?

## Answer guide

- Classify checks by risk, duration, and diagnostic value, then keep fast deterministic tests in the ordinary change path.
- Run slower integration, performance, or environmental checks at an appropriate gate with clear ownership and service objectives.
- Track queue time, flake rate, and escaped defects so cost reductions do not quietly weaken confidence.
- Revisit the policy after architecture changes; a universal gate can waste capacity and still miss the system boundary that matters.

## References

- [Martin Fowler — practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Further reading (blog): [Google Testing Blog](https://testing.googleblog.com/)

## What to learn next

- Official documentation: [Google Testing Blog](https://testing.googleblog.com/)
- Manual or specification: [Software Engineering at Google — testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Maintainer or personal blog: [Martin Fowler](https://martinfowler.com/)
- Technical blog: [Netflix TechBlog](https://netflixtechblog.com/)
- Hands-on guide: [pytest documentation](https://docs.pytest.org/en/stable/)
