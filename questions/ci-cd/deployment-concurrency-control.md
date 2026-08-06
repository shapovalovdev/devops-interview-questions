---
title: Prevent conflicting production deployments
theme: ci-cd
difficulty: senior
type: scenario
tags: [ci-cd, deployment, reliability, automation]
sources:
  - url: https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency
    source_type: official-docs
    verified_on: 2026-08-06
---

# Prevent conflicting production deployments

How should a delivery system stop two releases from mutating the same production target at once?

## Answer guide

- Put deployments that share a target in an explicit concurrency group and choose whether newer runs cancel obsolete work or queue behind it based on safety and release semantics.
- Recheck the artifact, desired revision, and environment state when a queued job begins; a previously approved deployment can be stale.
- Scope locks narrowly enough to preserve throughput but broadly enough to cover shared migrations, traffic controls, and configuration. Concurrency control prevents overlapping automation, not out-of-band changes or an unsafe deployment design.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: Concurrency](https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency)
- [Further reading: GitHub Docs—control deployments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments)
