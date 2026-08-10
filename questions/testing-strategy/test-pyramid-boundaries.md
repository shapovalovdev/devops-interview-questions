---
title: Define test-pyramid boundaries
theme: testing-strategy
difficulty: junior
type: theory
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://abseil.io/resources/swe-book/html/ch11.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Define test-pyramid boundaries

How should an engineering team make this testing decision?

## Answer guide

- Start from the production risk and choose the smallest test boundary that can prove the behavior with realistic dependencies. Keep feedback fast enough for ordinary change flow.
- Make ownership, test data, and environment assumptions explicit. A test that relies on shared mutable state or timing is a reliability risk, not merely a slow check.
- Combine deterministic automated checks with targeted integration evidence. Measure failures and maintain the suite as a product; do not use coverage alone as proof of confidence.
- Revisit the mix after incidents and architecture changes. Over-investing in expensive end-to-end checks can slow delivery while still missing boundary failures.

## References

- [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- [Ham Vocke — the practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Further reading (blog): [Google Testing Blog — just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)

## What to learn next

- Official documentation: [pytest documentation](https://docs.pytest.org/en/stable/)
- Manual or specification: [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Maintainer or personal blog: [Ham Vocke — the practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Technical blog: [Google Testing Blog — just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)
- Hands-on guide: [pytest — how-to guides](https://docs.pytest.org/en/stable/how-to/index.html)
