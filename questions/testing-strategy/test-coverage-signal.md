---
title: Treat coverage as a testing signal
theme: testing-strategy
difficulty: junior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://coverage.readthedocs.io/en/latest/branch.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch11.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Treat coverage as a testing signal

A manager proposes an 85% line-coverage gate on every repository. What will that number actually tell you, what will it miss, and what would you propose instead?

## Answer guide

- Coverage measures execution, not verification. A line counts as covered the moment any test causes it to run, whether or not anything asserted on the outcome, so a suite that calls every function and asserts nothing can reach 85% and detect no defect at all. Line coverage is also the weakest of the available measures: `if a and b:` on one line is fully covered by a single case, whereas branch coverage — Coverage.py's `--branch` — requires every arc out of every decision point, which is what actually catches the unhandled `else` and the exception path.
- Read it as a subtractive signal. High coverage proves very little, but a specific block at zero is a concrete, actionable fact: this error handler, this migration path, this retry branch has never been executed by a test. That makes the coverage report most valuable as a diff view — which lines the change added and which of those the change's tests never touch — rather than as an aggregate. Google's own guidance is to use coverage to find gaps and to distrust a single repository-wide threshold as an objective.
- So propose a gate on the change rather than on the codebase: new and modified lines must be covered, with an explicit, reviewed exemption path, plus a rule that the total may not fall. That measures the behaviour you want — people writing tests with their change — without demanding a retrospective campaign against legacy code whose payoff is worst where the code is least likely to change. Exclude generated code and expose branch rather than line percentages so the number is harder to inflate.
- Failure modes: teams meeting a percentage by testing trivial accessors and generated code while the payment path stays untested; assertion-free tests written specifically to raise the number; coverage collected only from unit tests so integration-covered code appears uncovered and gets duplicate tests; and the reverse error, treating 100% as proof, when coverage says nothing about missing requirements — code that was never written cannot be uncovered.

## References

- [Coverage.py — branch coverage measurement](https://coverage.readthedocs.io/en/latest/branch.html)
- [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Further reading (blog): [Google Testing Blog — code coverage best practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)

## What to learn next

- Official documentation: [Coverage.py documentation](https://coverage.readthedocs.io/en/latest/)
- Manual or specification: [Software Engineering at Google — testing overview](https://abseil.io/resources/swe-book/html/ch11.html)
- Maintainer or personal blog: [Martin Fowler — test coverage](https://martinfowler.com/bliki/TestCoverage.html)
- Technical blog: [Google Testing Blog — code coverage best practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)
- Hands-on guide: [Coverage.py — branch coverage measurement](https://coverage.readthedocs.io/en/latest/branch.html)
