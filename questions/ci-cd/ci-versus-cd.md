---
title: Distinguish continuous integration, delivery, and deployment
theme: ci-cd
difficulty: junior
type: theory
tags: [ci-cd, automation, delivery, deployment, kcna]
sources:
  - url: https://docs.github.com/en/actions/concepts/workflows-and-actions
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish continuous integration, delivery, and deployment

What are continuous integration, continuous delivery, and continuous deployment, and where should a team keep a human decision?

## Answer guide

- Continuous integration merges small changes frequently and validates them with an automated build and test suite.
- Continuous delivery keeps every validated change in a deployable state; continuous deployment automatically releases eligible changes to production.
- Put a human or policy decision at a risk boundary such as production approval, regulated change review, or an exception to an automated rollback rule. Manual steps inside every build create queues and inconsistent evidence.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: Workflows and actions](https://docs.github.com/en/actions/concepts/workflows-and-actions)
- [Further reading: Google Cloud—continuous delivery overview](https://cloud.google.com/architecture/devops/devops-tech-continuous-delivery)

## What to learn next

- Official documentation: [GitHub Actions concepts](https://docs.github.com/en/actions/concepts/overview)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Charity Majors](https://charity.wtf/)
- Technical blog: [Google Cloud DevOps and SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Practical guide](https://docs.github.com/en/actions/tutorials/build-and-test-code)
