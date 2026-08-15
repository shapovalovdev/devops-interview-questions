---
title: Migrate Terraform state to a remote backend
theme: infrastructure-as-code
difficulty: middle
type: scenario
tags: [terraform, infrastructure-as-code, automation, reliability, security]
sources:
  - url: https://developer.hashicorp.com/terraform/language/backend
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://opentofu.org/docs/language/state/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Migrate Terraform state to a remote backend

How would you migrate a team from local Terraform state to a remote backend safely?

## Answer guide

- Inventory each state file and ensure only one approved team owns each remote object set. Back up the existing state before altering backend configuration.
- Configure the remote backend with least-privilege access, encryption and a recovery policy; choose locking support if concurrent writers are possible.
- Run `terraform init` to validate and migrate state, then compare state and run a no-change plan using the new backend before allowing normal applies.
- Never put backend credentials in configuration or CI logs: Terraform can retain backend settings in `.terraform` and saved plans. A migration without access-control design merely centralizes a sensitive file.
- Remote-state migration is the same operation on OpenTofu, whose backends and state semantics follow the fork's lineage; on Pulumi the equivalent move switches the backend while preserving stack state — inventory, backup, and no-change-plan verification apply in each case.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: Backend configuration](https://developer.hashicorp.com/terraform/language/backend)
- [Terraform: State](https://developer.hashicorp.com/terraform/language/state)
- [OpenTofu — state](https://opentofu.org/docs/language/state/)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
