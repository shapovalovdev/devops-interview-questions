---
title: Handle flaky tests without masking regressions
theme: ci-cd
difficulty: middle
type: troubleshooting
tags: [ci-cd, debugging, reliability, troubleshooting]
sources:
  - url: https://martinfowler.com/articles/nonDeterminism.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Handle flaky tests without masking regressions

What should happen when a test fails intermittently in CI?

## Answer guide

- Preserve the failure evidence, classify it as product defect, test defect, or environmental instability, and assign an owner and deadline rather than silently accepting retries.
- Reproduce with the recorded seed, timing, environment, and dependency versions; remove uncontrolled time, concurrency, network, and shared-state assumptions.
- A bounded retry may reduce transient infrastructure noise, but report both the first attempt and final result. Retrying deterministic failures can turn a release gate into a false signal and hide a real regression.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [Martin Fowler: Eradicating non-determinism in tests](https://martinfowler.com/articles/nonDeterminism.html)
- [Further reading: GitHub Docs—workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs)
