---
title: Build a CI/CD cost and capacity model
theme: ci-cd
difficulty: staff
type: scenario
tags: [ci-cd, cost-optimization, capacity-planning, monitoring, governance]
sources:
  - url: https://docs.github.com/en/billing/concepts/product-billing/github-actions
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build a CI/CD cost and capacity model

How would you manage CI/CD spend and queue time as engineering usage grows?

## Answer guide

- Measure demand by repository, workflow, runner class, duration, cache hit rate, and queue time; forecast peak concurrency rather than relying on average utilization.
- Reduce waste through deterministic caching, test selection backed by evidence, right-sized runners, and concurrency limits while preserving a complete release path.
- Allocate costs transparently and set service objectives for queue and critical-path duration. Over-optimizing runner minutes can increase developer wait time or weaken verification, while unconstrained parallelism can exhaust quotas.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [Further reading: GitHub Docs—concurrency](https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency)

## What to learn next

- Official documentation: [GitHub Actions billing](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Charity Majors](https://charity.wtf/)
- Technical blog: [Google Cloud DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Practical guide](https://docs.github.com/en/actions/tutorials/build-and-test-code)
