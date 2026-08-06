---
title: Design a deployment rollback
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, deployment, reliability, incident-response]
sources:
  - url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a deployment rollback

What makes a rollback fast and safe when a newly deployed service is harmful?

## Answer guide

- Define measurable rollback triggers, the responsible operator, and the known-good immutable artifact before deployment. Automate the common rollback path where the blast radius warrants it.
- Roll back application code and compatible configuration together, then verify customer-facing signals and dependency behavior rather than only job completion.
- Database migrations and irreversible external effects can make version rollback unsafe. Use backward-compatible expand/contract changes, feature flags, backups, and an incident plan for data correction.

## References

- [Kubernetes: Deployments and rollout history](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Further reading: Google SRE Workbook—canarying releases](https://sre.google/workbook/canarying-releases/)
