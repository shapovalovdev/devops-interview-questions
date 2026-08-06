---
title: Design a stable Terraform module interface
theme: infrastructure-as-code
difficulty: middle
type: scenario
tags: [terraform, infrastructure-as-code, automation, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/modules/develop
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a stable Terraform module interface

What makes a Terraform module safe to reuse across teams and environments?

## Answer guide

- Give the module one cohesive responsibility, explicitly typed inputs, documented outputs, and sensible validation; callers should not need to understand hidden implementation details.
- Pin module versions from a registry, VCS, or package source and upgrade them through review. Treat an input, output, or resource-address change as an API compatibility decision.
- Put provider configuration in the root module in most cases so the caller controls credentials, region, and provider aliases; pass aliases explicitly for multi-provider modules.
- Avoid a universal module with dozens of loosely related flags. It increases the test matrix and creates accidental coupling between teams.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: Developing modules](https://developer.hashicorp.com/terraform/language/modules/develop)
- [Terraform: Module composition](https://developer.hashicorp.com/terraform/language/modules/develop/composition)
