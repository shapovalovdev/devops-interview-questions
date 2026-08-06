---
title: Govern infrastructure drift at organization scale
theme: infrastructure-as-code
difficulty: staff
type: scenario
tags: [terraform, infrastructure-as-code, governance, monitoring, reliability, security]
sources:
  - url: https://developer.hashicorp.com/terraform/cli/commands/plan
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern infrastructure drift at organization scale

What operating model detects and reduces IaC drift without blocking incident response?

## Answer guide

- Define ownership and an expected reconciliation time by resource criticality; schedule read-only plan/drift checks and route findings to the owning team with enough context to decide intent.
- Permit time-bounded emergency changes with an auditable record, then require configuration reconciliation or explicit retirement of the managed object.
- Track drift age, recurrence, coverage, and changes by identity to distinguish provider noise from access-control or process failures.
- Do not auto-apply every detected difference. Some differences represent an approved emergency fix, an unsafe provider interpretation, or a configuration bug; reconciliation needs an accountable decision.

## References

- [Terraform: plan command](https://developer.hashicorp.com/terraform/cli/commands/plan)
- [Terraform: refresh-only mode tutorial](https://developer.hashicorp.com/terraform/tutorials/state/refresh)
