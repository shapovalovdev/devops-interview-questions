---
title: Choose reusable workflow boundaries
theme: ci-cd
difficulty: middle
type: theory
tags: [ci-cd, github-actions, automation, governance]
sources:
  - url: https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose reusable workflow boundaries

When should a team extract a reusable workflow, and what inputs should it expose?

## Answer guide

- Extract stable, repeated policy such as build, test, signing, or deployment setup when consumers need the same behavior and evidence.
- Expose small typed inputs, explicit outputs, and the minimum secrets and permissions; version the reusable workflow like an interface.
- Keep product-specific branching in the caller. Reusable workflows cannot elevate caller token permissions, and excessive nesting or hidden defaults makes failures and changes difficult to audit.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: Reusing workflow configurations](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations)
- [Further reading: GitHub Docs—workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)

## What to learn next

- Official documentation: [GitHub reusable workflows](https://docs.github.com/en/actions/how-tos/sharing-automations/reusing-workflows)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [Practical guide](https://docs.github.com/en/actions/tutorials/create-actions)
