---
title: Pin Terraform provider dependencies safely
theme: infrastructure-as-code
difficulty: junior
type: scenario
tags: [terraform, infrastructure-as-code, automation, reliability, security]
sources:
  - url: https://developer.hashicorp.com/terraform/language/providers/requirements
    source_type: official-docs
    verified_on: 2026-08-06
---

# Pin Terraform provider dependencies safely

How do provider constraints and the dependency lock file work together in a production repository?

## Answer guide

- Declare provider source addresses and version constraints in `required_providers`; constraints define the acceptable compatibility range.
- Commit `.terraform.lock.hcl` for root modules so repeated initialization selects the recorded provider versions and verifies recorded checksums.
- Upgrade intentionally in a branch, inspect the lock-file diff, run plans/tests, and verify provider release notes for changed resource semantics.
- A constraint alone can still allow a newer compatible version; deleting or casually regenerating the lock file makes CI and developer machines less reproducible.

## References

- [Terraform: Provider requirements](https://developer.hashicorp.com/terraform/language/providers/requirements)
- [Terraform: Dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock)
