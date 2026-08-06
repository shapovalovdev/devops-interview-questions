---
title: Define an Argo Rollouts AnalysisTemplate safely
theme: ci-cd
difficulty: senior
type: scenario
tags: [ci-cd, kubernetes, argo, argo-rollouts, capa, observability, reliability]
sources:
  - url: https://argo-rollouts.readthedocs.io/en/stable/features/analysis/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define an Argo Rollouts AnalysisTemplate safely

What makes an AnalysisTemplate suitable for automatically promoting or aborting a rollout?

## Answer guide

- Define metrics that represent user-visible correctness and provide explicit success and failure conditions, sampling interval, failure limit, and measurement window. AnalysisRuns evaluate those metrics during a rollout according to the template.
- Use a low-cardinality, version-aware query and test it against known-good and known-bad releases. Prefer a small set of reliable signals over a complex query no one can operate during an incident.
- Account for delayed telemetry, sparse traffic, and dependencies outside the candidate. A noisy or missing metric can stall safe delivery or promote a regression, so retain manual pause and rollback procedures.

## References

- [Argo Rollouts: analysis](https://argo-rollouts.readthedocs.io/en/stable/features/analysis/)
- Further reading (blog): [Google Cloud Blog: practical SLOs for releases](https://cloud.google.com/blog/products/devops-sre/introducing-slos-service-level-objectives)
