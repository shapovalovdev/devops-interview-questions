---
title: Make test failures observable
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Make test failures observable

How should a team make this testing strategy decision?

## Answer guide

- Start from the production risk and choose a test boundary that proves the behavior without making feedback unnecessarily slow.
- Make dependencies, data ownership, and environment isolation explicit so results are reproducible and failures can be diagnosed.
- Treat test execution time and flake rate as product metrics; improve the signal before tightening a release gate.
- Review the strategy after escaped defects and architecture changes. More tests do not automatically improve confidence when the wrong boundary is exercised.

## References

- [Martin Fowler — practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- Further reading (blog): [Google Testing Blog](https://testing.googleblog.com/)

## What to learn next

- Official documentation: [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- Manual or specification: [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/)
- Maintainer or personal blog: [Pete Hodgson — domain-oriented observability](https://martinfowler.com/articles/domain-oriented-observability.html)
- Technical blog: [Honeycomb — what observability-driven development is not](https://www.honeycomb.io/blog/observability-driven-development)
- Hands-on guide: [OpenTelemetry — Python getting started](https://opentelemetry.io/docs/languages/python/getting-started/)
