---
title: Isolate Terraform environments and blast radius
theme: infrastructure-as-code
difficulty: senior
type: scenario
tags: [terraform, infrastructure-as-code, security, reliability, governance]
sources:
  - url: https://developer.hashicorp.com/terraform/language/state/workspaces
    source_type: official-docs
    verified_on: 2026-08-06
---

# Isolate Terraform environments and blast radius

How should an organization separate development, staging, and production Terraform operations?

## Answer guide

- Separate state, credentials, approvals, and operational ownership at least by environment and meaningful blast-radius boundary. A workspace is a distinct state instance, but it is not automatically a complete security boundary.
- Use explicit environment inputs and provider configuration; do not infer production from a local shell default or a mutable branch name.
- Grant CI identities only the scope required for that environment, require stronger review for production, and make target workspace/environment visible in plans.
- Splitting every resource into its own state creates dependency and coordination overhead; grouping everything into one state makes locks and failures too broad. Choose boundaries around lifecycle and ownership.

## References

- [Terraform: Workspaces](https://developer.hashicorp.com/terraform/language/state/workspaces)
- [Terraform: State](https://developer.hashicorp.com/terraform/language/state)
