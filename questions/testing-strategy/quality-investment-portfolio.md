---
title: Prioritize quality investment portfolio
theme: testing-strategy
difficulty: staff
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://dora.dev/guides/dora-metrics/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch11.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Prioritize quality investment portfolio

How should a team make this testing strategy decision?

## Answer guide

- Define the user-facing risk and choose a test boundary that produces useful evidence without delaying every change.
- Make dependencies, data, and environment ownership explicit so results are reproducible and failures can be diagnosed.
- Balance test cost against feedback speed and release confidence; use the result together with review and operational signals.
- Reassess after incidents and architecture changes, because an uncontrolled or unowned check becomes a source of false confidence.

## References

- [DORA — software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Further reading (blog): [Martin Fowler — is high quality software worth the cost?](https://martinfowler.com/articles/is-quality-worth-cost.html)

## What to learn next

- Official documentation: [DORA — software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- Manual or specification: [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Maintainer or personal blog: [Martin Fowler — is high quality software worth the cost?](https://martinfowler.com/articles/is-quality-worth-cost.html)
- Technical blog: [AWS Builders' Library — going faster with continuous delivery](https://aws.amazon.com/builders-library/going-faster-with-continuous-delivery/)
- Hands-on guide: [DORA — quick check](https://dora.dev/quickcheck/)
