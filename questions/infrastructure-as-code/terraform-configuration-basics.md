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
---

# Explain a Terraform root module and resource address

What is a Terraform root module, and why does a stable resource address matter?

## Answer guide

- The directory from which Terraform runs is the root module; it can call child modules. A resource address identifies a particular resource instance in configuration and state.
- Stable addresses let Terraform relate declared instances to already-managed remote objects. Changing an address without expressing a move can make Terraform plan a destroy/create operation.
- Keep a root module focused on one deployable boundary, expose a small input/output interface, and use reviewable refactoring procedures when reorganizing addresses.
- Modules are an abstraction, not a security boundary. Over-generalizing them can hide provider-specific behavior and make changes difficult to reason about.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: Modules](https://developer.hashicorp.com/terraform/language/modules)
- [Terraform: Resource syntax](https://developer.hashicorp.com/terraform/language/resources/syntax)
