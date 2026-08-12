---
title: Design a deployment rollback
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, deployment, reliability, incident-response, cgoa]
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

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [Kubernetes: Deployments and rollout history](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Further reading: Google SRE Workbook—canarying releases](https://sre.google/workbook/canarying-releases/)

## What to learn next

- Official documentation: [Kubernetes rolling back a Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [kubectl rollout reference](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/)
