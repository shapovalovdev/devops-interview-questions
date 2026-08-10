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

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [Kubernetes: Deployments and rollout history](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Further reading: Google SRE Workbook—canarying releases](https://sre.google/workbook/canarying-releases/)

## What to learn next

- Official documentation: [Helm rollback command reference](https://helm.sh/docs/helm/helm_rollback/)
- Manual or specification: [Google SRE Book — release engineering](https://sre.google/sre-book/release-engineering/)
- Maintainer or personal blog: [Pete Hodgson — feature toggles](https://martinfowler.com/articles/feature-toggles.html)
- Technical blog: [Google Cloud — DevOps and SRE blog](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Kubernetes — update and roll back an application](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)
