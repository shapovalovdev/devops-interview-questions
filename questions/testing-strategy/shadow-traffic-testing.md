---
title: Use shadow traffic safely
theme: testing-strategy
difficulty: staff
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://istio.io/latest/docs/tasks/traffic-management/mirroring/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://sre.google/sre-book/testing-reliability/
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

- [Istio — mirroring traffic to a second service](https://istio.io/latest/docs/tasks/traffic-management/mirroring/)
- [Google SRE Book — testing for reliability](https://sre.google/sre-book/testing-reliability/)
- Further reading (blog): [Martin Fowler — dark launching](https://martinfowler.com/bliki/DarkLaunching.html)

## What to learn next

- Official documentation: [Istio — traffic management concepts](https://istio.io/latest/docs/concepts/traffic-management/)
- Manual or specification: [Google SRE Book — testing for reliability](https://sre.google/sre-book/testing-reliability/)
- Maintainer or personal blog: [Martin Fowler — dark launching](https://martinfowler.com/bliki/DarkLaunching.html)
- Technical blog: [Honeycomb — testing in production, should you do it?](https://www.honeycomb.io/blog/testing-in-production)
- Hands-on guide: [Istio — mirroring traffic to a second service](https://istio.io/latest/docs/tasks/traffic-management/mirroring/)
