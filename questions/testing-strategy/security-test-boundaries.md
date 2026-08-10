---
title: Set security testing boundaries
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Set security testing boundaries

How should a team make this testing strategy decision?

## Answer guide

- Define the user-facing risk and choose a test boundary that produces useful evidence without delaying every change.
- Make dependencies, data, and environment ownership explicit so results are reproducible and failures can be diagnosed.
- Balance test cost against feedback speed and release confidence; use the result together with review and operational signals.
- Reassess after incidents and architecture changes, because an uncontrolled or unowned check becomes a source of false confidence.

## References

- [Martin Fowler — practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Further reading (blog): [Google Testing Blog](https://testing.googleblog.com/)

## What to learn next

- Official documentation: [Google Testing Blog](https://testing.googleblog.com/)
- Manual or specification: [Software Engineering at Google — testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Maintainer or personal blog: [Martin Fowler](https://martinfowler.com/)
- Technical blog: [Netflix TechBlog](https://netflixtechblog.com/)
- Hands-on guide: [pytest documentation](https://docs.pytest.org/en/stable/)
