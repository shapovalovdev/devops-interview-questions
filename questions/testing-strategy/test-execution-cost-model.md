---
title: Model test execution cost
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://docs.github.com/en/actions
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch14.html
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

- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Software Engineering at Google — larger testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Further reading (blog): [Google Testing Blog — test sizes](https://testing.googleblog.com/2010/12/test-sizes.html)

## What to learn next

- Official documentation: [GitHub Actions documentation](https://docs.github.com/en/actions)
- Manual or specification: [Software Engineering at Google — larger testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Maintainer or personal blog: [Alex Kladov — how to test](https://matklad.github.io/2021/05/31/how-to-test.html)
- Technical blog: [Google Testing Blog — test sizes](https://testing.googleblog.com/2010/12/test-sizes.html)
- Hands-on guide: [pytest-xdist — distributed test execution](https://pytest-xdist.readthedocs.io/en/stable/)
