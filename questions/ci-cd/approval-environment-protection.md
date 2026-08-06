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

- [GitHub Docs: Control deployments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments)
- [Further reading: GitHub Docs—deployment environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)
