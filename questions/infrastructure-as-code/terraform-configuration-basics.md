---
title: Explain a Terraform root module and resource address
theme: infrastructure-as-code
difficulty: junior
type: theory
tags: [terraform, infrastructure-as-code, automation]
sources:
  - url: https://developer.hashicorp.com/terraform/language/modules
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://opentofu.org/docs/language/modules/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Explain a Terraform root module and resource address

What is a Terraform root module, and why does a stable resource address matter?

## Answer guide

- The directory from which Terraform runs is the root module; it can call child modules. A resource address identifies a particular resource instance in configuration and state.
- Stable addresses let Terraform relate declared instances to already-managed remote objects. Changing an address without expressing a move can make Terraform plan a destroy/create operation.
- Keep a root module focused on one deployable boundary, expose a small input/output interface, and use reviewable refactoring procedures when reorganizing addresses.
- Modules are an abstraction, not a security boundary. Over-generalizing them can hide provider-specific behavior and make changes difficult to reason about.
- OpenTofu, the Linux Foundation fork, keeps the same root-module and resource-address model, so this reasoning transfers verbatim; CloudFormation stacks with nested stacks and Pulumi projects with resource URNs are the equivalent unit-and-identity pairs on other toolchains.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: Modules](https://developer.hashicorp.com/terraform/language/modules)
- [Terraform: Resource syntax](https://developer.hashicorp.com/terraform/language/resources/syntax)
- [OpenTofu — modules](https://opentofu.org/docs/language/modules/)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
