---
title: Apply least privilege to a workflow token
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, github-actions, security, least-privilege]
sources:
  - url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#permissions
    source_type: official-docs
    verified_on: 2026-08-06
---

# Apply least privilege to a workflow token

How do you prevent a workflow from receiving more repository permission than it needs?

## Answer guide

- Declare explicit `GITHUB_TOKEN` permissions at workflow or job scope and grant only the scopes required by that job, such as `contents: read` for checkout.
- Split publishing or deployment into a separate job with the narrowly required write permission and protect it with trusted triggers and environments.
- Fork pull requests normally receive read-only access, but do not treat that as the only defense. Third-party actions and injected scripts can misuse any available token, so pin actions and review changes to workflow files.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: Workflow syntax—permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#permissions)
- [Further reading: GitHub Docs—security hardening for Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)

## What to learn next

- Official documentation: [GitHub Actions permissions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Troy Hunt](https://www.troyhunt.com/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [Security hardening your deployments](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments)
