---
title: Plan a blue-green production cutover
theme: ci-cd
difficulty: senior
type: scenario
tags: [ci-cd, deployment, reliability, availability]
sources:
  - url: https://cloud.google.com/architecture/application-deployment-and-testing-strategies
    source_type: official-docs
    verified_on: 2026-08-06
---

# Plan a blue-green production cutover

What must be true before switching production traffic from blue to green?

## Answer guide

- Build green from the same immutable release process, validate it with production-like dependencies, and make health checks reflect ability to serve critical requests.
- Shift traffic with an explicit routing change, observe end-to-end and business signals, and retain blue long enough for a tested reversal.
- Ensure sessions, caches, schemas, queues, and background workers remain compatible across both versions. Blue-green requires duplicate capacity and does not make a bad shared database migration reversible.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [Google Cloud: Deployment and testing strategies](https://cloud.google.com/architecture/application-deployment-and-testing-strategies)
- [Further reading: Kubernetes—Deployment rolling updates](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

## What to learn next

- Official documentation: [Kubernetes Deployment strategies](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [John Allspaw](https://www.kitchensoap.com/)
- Technical blog: [Google Cloud DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [kubectl rollout reference](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/)
