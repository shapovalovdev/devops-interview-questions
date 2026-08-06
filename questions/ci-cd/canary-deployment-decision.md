---
title: Decide whether to advance or stop a canary deployment
theme: ci-cd
difficulty: senior
type: scenario
tags: [ci-cd, deployment, monitoring, reliability]
sources:
  - url: https://sre.google/workbook/canarying-releases/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Decide whether to advance or stop a canary deployment

Which signals should control promotion of a small canary release?

## Answer guide

- Compare error rate, latency, saturation, and relevant business outcomes for the canary against a stable baseline and against the service’s SLO/error budget.
- Define the traffic slice, observation window, minimum sample size, promotion rule, and rollback threshold before release; stop or roll back automatically when a threshold breaches.
- Segment signals by region, version, and critical journey so a global average does not hide harm. A healthy canary cannot prove behavior under full load, and noisy or non-representative traffic requires a longer hold or a different experiment.

## References

- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
- [Further reading: Kubernetes—Deployment rolling updates](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
