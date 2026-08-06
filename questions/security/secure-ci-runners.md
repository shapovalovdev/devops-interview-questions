---
title: Secure shared CI runners
theme: security
difficulty: middle
type: scenario
tags: [security, ci-cd, least-privilege, supply-chain]
sources:
  - url: https://docs.github.com/actions/security-for-github-actions/security-guides/security-hardening-your-deployments
    source_type: official-docs
    verified_on: 2026-08-06
---

# Secure shared CI runners

What controls should protect a CI runner that executes code from many repositories?

## Answer guide

- Assume build code is untrusted. Isolate jobs, use ephemeral runners where practical, restrict network and cloud access, and avoid mounting host sockets or persistent credentials by default.
- Give each workflow a minimal token and use short-lived federation for cloud access. Protect production environments with approvals and branch rules.
- Pin third-party actions or dependencies to reviewed immutable revisions, log runner activity, and patch runner images.
- Shared workspaces, reusable credentials, privileged Docker access, or secrets exposed to pull-request code let one project compromise another. Isolation controls need regular escape and cleanup testing.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [GitHub Actions: Security hardening](https://docs.github.com/actions/security-for-github-actions/security-guides/security-hardening-your-deployments)
- [OpenSSF: Secure Software Development](https://bestpractices.coreinfrastructure.org/)
