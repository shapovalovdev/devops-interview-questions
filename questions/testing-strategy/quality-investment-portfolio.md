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

You are given four engineers for a quarter to improve quality across twelve services, and every team's request is "more test coverage". How do you decide where that capacity goes, and how will you know afterwards whether it worked?

## Answer guide

- Start from failure data, not from coverage. Pull the last two or three quarters of incidents, customer-reported defects, and rollbacks, and attribute each to the stage that should have caught it and the service it came from. The distribution is almost never uniform: a small number of services and a small number of failure classes — a config change with no validation, a schema migration, a third-party timeout — usually account for most of the pain, and that ranking is the portfolio, whereas per-team coverage requests are a proxy for how each team feels.
- Balance the portfolio across the four DORA outcomes rather than optimising one. Deployment frequency and lead time are throughput; change failure rate and failed-deployment recovery time are stability. Work that only adds gates buys stability by spending lead time, and work that only removes friction does the reverse; the research finding worth acting on is that the two move together when the investment is in the feedback loop itself — faster suites, better environments, safer rollback — rather than in more checks. Reserve part of the capacity for reducing test runtime, because it compounds across every future change.
- Make each bet falsifiable before it starts. Write the expected effect as a change in a measurable quantity — this class of defect stops reaching production, this suite drops below ten minutes, this service's change failure rate halves — with a baseline recorded now and a review date at the end of the quarter. Convert cost into the same currency: hours of engineer time per week lost to flaky reruns, or incident minutes, so a request competes on evidence rather than volume.
- Failure modes: funding a coverage percentage target, which reliably produces assertion-free tests and no defect reduction; spending the whole quarter on the loudest team rather than the riskiest service; treating quality investment as a one-off project so the improvement decays once the funded engineers leave; and measuring only the metric you moved, missing that lead time doubled because the new gates added forty minutes to every pipeline.

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
