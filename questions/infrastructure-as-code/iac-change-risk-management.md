---
title: Create a risk-based IaC change-management model
theme: infrastructure-as-code
difficulty: staff
type: scenario
tags: [terraform, infrastructure-as-code, governance, deployment, reliability, security]
sources:
  - url: https://developer.hashicorp.com/terraform/cli/commands/plan
    source_type: official-docs
    verified_on: 2026-08-06
---

# Create a risk-based IaC change-management model

How would you scale IaC approvals without applying the same process to every change?

## Answer guide

- Classify plans by impact signals such as destructive actions, privilege changes, public network exposure, production scope, data movement, and replacement of stateful services.
- Require the evidence proportionate to the risk: reviewed plan, owner approval, maintenance/cutover plan, rollback evidence, and policy result. Low-risk repeatable changes should flow automatically through protected CI.
- Preserve the reviewed configuration, plan metadata, policy decision, actor identity, and apply result for audit and incident investigation.
- A plan becomes stale when inputs or remote infrastructure change. Risk classification reduces review noise; it does not make a speculative plan safe to apply later without revalidation.
- Impact classification generalizes across tools because every plan contract exposes the same signals: CloudFormation change sets classify actions as add, modify, remove, or import, and OpenTofu plan JSON carries the same destructive-action flags a risk classifier consumes.

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
