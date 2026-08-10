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

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: plan command](https://developer.hashicorp.com/terraform/cli/commands/plan)
- [Terraform: apply command](https://developer.hashicorp.com/terraform/cli/commands/apply)
## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
