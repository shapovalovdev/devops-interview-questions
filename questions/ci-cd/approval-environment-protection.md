---
title: Configure production environment protection
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, deployment, security, governance]
sources:
  - url: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments
    source_type: official-docs
    verified_on: 2026-08-06
---

# Configure production environment protection

How should a pipeline use an environment approval without turning every release into a manual ceremony?

## Answer guide

- Bind the production deployment job to an environment with reviewers, branch/tag restrictions, and narrowly scoped secrets; keep validation and artifact creation automated.
- Require an approval only after the immutable artifact and release evidence are ready, and record who approved which revision and deployment intent.
- Use policy-based automatic promotion for low-risk changes when justified by evidence. Approval is not a substitute for tests, observability, rollback, or separation of duties; stale approvals must not authorize a different artifact.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: Control deployments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments)
- [Further reading: GitHub Docs—deployment environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)

## What to learn next

- Official documentation: [GitHub Actions deployments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Charity Majors](https://charity.wtf/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [GitHub Actions deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments)
