---
title: Measure platform impact with DORA metrics without gaming teams
theme: sre
difficulty: staff
type: scenario
tags: [platform-engineering, reliability, monitoring, ci-cd, governance, cnpa]
sources:
  - url: https://dora.dev/guides/dora-metrics/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://dora.dev/capabilities/platform-engineering/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Measure platform impact with DORA metrics without gaming teams

How would you show whether a new internal developer platform improves delivery
without turning DORA metrics into individual or team performance targets?

## Answer guide

- Establish a baseline for comparable services and instrument the delivery path consistently: change lead time, deployment frequency, failed-deployment recovery time, change-failure percentage, and deployment rework rate. Define event boundaries, exclusions, owners, and data quality checks before comparing periods; a metric whose deployments or incidents are counted differently is not evidence of platform impact.
- Pair delivery measures with platform adoption, task-success time, support demand, reliability objectives, and developer-feedback signals. Segment results by service class and rollout cohort instead of averaging unlike teams, because a platform can reduce self-service friction while a migration or a higher-risk product temporarily changes delivery outcomes.
- Use the scorecard to find bottlenecks and test reversible improvements, then publish the interpretation and uncertainty. Do not set a universal deployment-frequency quota or rank individuals: teams can split changes, relabel failures, or avoid necessary work when a proxy becomes a target.
- Review unintended effects such as worsened availability, queueing at a platform gate, exclusion of hard-to-migrate services, and survey fatigue. A positive metric trend is insufficient if it was purchased by suppressing incident reporting, weakening controls, or moving toil to another team.

## References

- [DORA: software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- [DORA: platform engineering capability](https://dora.dev/capabilities/platform-engineering/)
- Further reading (blog): [Google Cloud Blog: improve developer experience with platform engineering](https://cloud.google.com/blog/products/application-development/how-platform-engineers-can-improve-their-developers-experience)
