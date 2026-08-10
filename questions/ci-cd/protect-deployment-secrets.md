---
title: Protect deployment secrets in CI/CD
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, security, least-privilege, deployment]
sources:
  - url: https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions
    source_type: official-docs
    verified_on: 2026-08-06
---

# Protect deployment secrets in CI/CD

How should a production deployment obtain credentials without exposing them to ordinary CI jobs?

## Answer guide

- Scope secrets to a protected environment and expose them only to the deployment job after its approval and policy checks; use separate identities for build and deploy.
- Prefer short-lived, federated credentials over long-lived static tokens, with least-privilege permissions and an auditable subject binding.
- Masking reduces accidental log disclosure but does not make untrusted code safe. Never run pull-request code with production secrets; rotate credentials and investigate any possible exposure.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [Further reading: GitHub Docs—OpenID Connect](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)

## What to learn next

- Official documentation: [GitHub Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Troy Hunt](https://www.troyhunt.com/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [Security hardening your deployments](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments)
