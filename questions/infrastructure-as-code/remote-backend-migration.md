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
---

# Migrate Terraform state to a remote backend

How would you migrate a team from local Terraform state to a remote backend safely?

## Answer guide

- Inventory each state file and ensure only one approved team owns each remote object set. Back up the existing state before altering backend configuration.
- Configure the remote backend with least-privilege access, encryption and a recovery policy; choose locking support if concurrent writers are possible.
- Run `terraform init` to validate and migrate state, then compare state and run a no-change plan using the new backend before allowing normal applies.
- Never put backend credentials in configuration or CI logs: Terraform can retain backend settings in `.terraform` and saved plans. A migration without access-control design merely centralizes a sensitive file.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: Backend configuration](https://developer.hashicorp.com/terraform/language/backend)
- [Terraform: State](https://developer.hashicorp.com/terraform/language/state)
