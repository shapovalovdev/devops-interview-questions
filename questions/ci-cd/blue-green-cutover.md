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

- Official documentation: [Argo Rollouts blue-green strategy](https://argo-rollouts.readthedocs.io/en/stable/features/bluegreen/)
- Manual or specification: [Google SRE Book — reliable product launches](https://sre.google/sre-book/reliable-product-launches/)
- Maintainer or personal blog: [Martin Fowler — blue-green deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html)
- Technical blog: [Google Cloud — DevOps and SRE blog](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [GitHub Actions — manage deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments)
