---
title: Define safe Terraform input variables
theme: infrastructure-as-code
difficulty: junior
type: theory
tags: [terraform, infrastructure-as-code, automation, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/values/variables
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://opentofu.org/docs/language/values/variables/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Define safe Terraform input variables

How should a reusable Terraform module expose and validate input variables?

## Answer guide

- Declare a type, useful description, and only a safe default for each input. Types make the module interface explicit and catch incompatible caller values early.
- Use validation blocks for constraints Terraform can evaluate, such as an allowed environment name or CIDR shape; validate provider-specific facts with provider APIs or policy checks where appropriate.
- Mark confidential inputs `sensitive`, but do not mistake redacted CLI output for secret removal: sensitive values can still be present in state.
- Avoid an untyped, catch-all variable map when a small explicit interface is possible; it makes upgrades and review less safe.
- Typed, validated inputs exist across tooling: OpenTofu keeps the same variable blocks with validation rules, while Bicep parameters and Pulumi inputs push the contract into a host language's type system — the interface-explicitness argument is the portable content.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: Input variables](https://developer.hashicorp.com/terraform/language/values/variables)
- [Terraform: Type constraints](https://developer.hashicorp.com/terraform/language/expressions/type-constraints)
- [OpenTofu — input variables](https://opentofu.org/docs/language/values/variables/)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
