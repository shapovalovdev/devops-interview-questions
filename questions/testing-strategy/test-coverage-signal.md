---
title: Treat coverage as a testing signal
theme: testing-strategy
difficulty: junior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://martinfowler.com/articles/practical-test-pyramid.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Treat coverage as a testing signal

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

- Official documentation: [Coverage.py documentation](https://coverage.readthedocs.io/en/latest/)
- Manual or specification: [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Maintainer or personal blog: [Martin Fowler — test coverage](https://martinfowler.com/bliki/TestCoverage.html)
- Technical blog: [Google Testing Blog — code coverage best practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)
- Hands-on guide: [Coverage.py — branch coverage measurement](https://coverage.readthedocs.io/en/latest/branch.html)
