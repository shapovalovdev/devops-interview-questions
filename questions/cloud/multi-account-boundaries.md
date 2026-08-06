---
title: Define AWS multi-account boundaries
theme: cloud
difficulty: middle
type: scenario
tags: [aws, cloud, security, governance, least-privilege]
sources:
  - url: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define AWS multi-account boundaries

Why use multiple AWS accounts, and how should teams obtain access across them?

## Answer guide

- Accounts create strong billing, quota, and resource isolation boundaries. Use them to separate environments, teams, regulated workloads, or blast radii rather than putting every workload in one shared account.
- Organize accounts in AWS Organizations and apply service control policies as organization-level guardrails; they set maximum permissions and do not themselves grant permissions.
- Give humans and automation short-lived, auditable role access through federation and cross-account roles. Centralize logging and security visibility while retaining workload-account ownership.
- Do not make an account-per-team scheme so fragmented that shared networking, incident access, and controls become unmanaged exceptions. Define account-vending, baseline, ownership, and exit processes.

## References

- [AWS Organizations introduction](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- [Further reading: AWS IAM cross-account roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)
