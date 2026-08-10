---
title: Place performance tests in CI
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://sre.google/sre-book/testing-reliability/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Place performance tests in CI

How should a team make this testing strategy decision?

## Answer guide

- Define the behavior and risk being controlled, then select evidence that is representative enough to influence a release decision.
- Keep dependencies, test data, and timing controlled so a passing result is reproducible and a failure is diagnosable.
- Make the cost, feedback time, and ownership explicit; use the result with code review and operational signals rather than as an isolated score.
- Review false positives and escaped defects after releases. A broad but untrusted test signal can slow delivery while masking meaningful gaps.

## References

- [Grafana k6 — automated performance testing](https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/)
- [Google SRE Book — testing for reliability](https://sre.google/sre-book/testing-reliability/)
- Further reading (blog): [Slack Engineering — continuous load testing](https://slack.engineering/continuous-load-testing/)

## What to learn next

- Official documentation: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
- Manual or specification: [Google SRE Book — testing for reliability](https://sre.google/sre-book/testing-reliability/)
- Maintainer or personal blog: [Brendan Gregg — active benchmarking](https://www.brendangregg.com/activebenchmarking.html)
- Technical blog: [Slack Engineering — continuous load testing](https://slack.engineering/continuous-load-testing/)
- Hands-on guide: [Grafana k6 — automated performance testing](https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/)
