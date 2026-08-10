---
title: Refactor Terraform resource addresses safely
theme: infrastructure-as-code
difficulty: senior
type: scenario
tags: [terraform, infrastructure-as-code, deployment, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/modules/develop/refactoring
    source_type: official-docs
    verified_on: 2026-08-06
---

# Refactor Terraform resource addresses safely

How do you move a resource into a module or rename it without recreating production infrastructure?

## Answer guide

- Identify the current and destination addresses and use a `moved` block to declare the state-address migration in configuration.
- Run a plan and confirm Terraform reports the move rather than a destroy/create sequence; apply through the normal locked, reviewed workflow.
- Keep moved blocks long enough for all supported callers and workspaces to upgrade, then remove them only as a documented breaking change.
- Do not rely on manual state moves as the normal migration mechanism. They are harder to review, repeat, and distribute across independent workspaces.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: Refactoring](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring)
- [Terraform: moved block reference](https://developer.hashicorp.com/terraform/language/block/moved)
## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
