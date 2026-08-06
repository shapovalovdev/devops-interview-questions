---
title: Review a Terraform plan before production apply
theme: infrastructure-as-code
difficulty: middle
type: scenario
tags: [terraform, infrastructure-as-code, automation, deployment, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/cli/commands/plan
    source_type: official-docs
    verified_on: 2026-08-06
---

# Review a Terraform plan before production apply

What must a production plan-review workflow establish before it applies infrastructure changes?

## Answer guide

- Run initialization and a plan using the same reviewed configuration, variables, provider versions, and target workspace intended for production.
- Inspect every create, update, replace, and destroy action; confirm scope, identities, regions, dependencies, and whether replacement causes downtime or data loss.
- In automation, save a reviewed plan and apply that exact plan promptly. Re-plan if the configuration, inputs, credentials, or relevant remote state may have changed.
- A speculative plan is evidence, not a reservation: other changes can make a later apply differ. Avoid `-auto-approve` unless a protected automation workflow provides equivalent controls.

## References

- [Terraform: plan command](https://developer.hashicorp.com/terraform/cli/commands/plan)
- [Terraform: apply command](https://developer.hashicorp.com/terraform/cli/commands/apply)
