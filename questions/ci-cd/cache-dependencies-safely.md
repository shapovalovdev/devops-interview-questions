---
title: Cache CI dependencies without using stale outputs
theme: ci-cd
difficulty: junior
type: scenario
tags: [ci-cd, automation, reliability, security]
sources:
  - url: https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows
    source_type: official-docs
    verified_on: 2026-08-06
---

# Cache CI dependencies without using stale outputs

How should a CI job cache dependencies while preserving correctness and isolation?

## Answer guide

- Key a dependency cache from the operating system, runtime/tool version, architecture, and lockfile hash; restore only compatible fallback keys.
- Cache downloaded dependencies or compiler caches, not unverified release artifacts. Rebuild outputs when source or build inputs change.
- Caches are an optimization, so the job must work on a cache miss. Do not place credentials in cache paths, and account for cache poisoning or cross-branch access when using shared runners.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: Caching dependencies](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)
- [Further reading: GitHub Docs—dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching)
