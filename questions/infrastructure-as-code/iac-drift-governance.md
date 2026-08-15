---
title: Govern infrastructure drift at organization scale
theme: infrastructure-as-code
difficulty: staff
type: scenario
tags: [terraform, infrastructure-as-code, governance, monitoring, reliability, security, cgoa]
sources:
  - url: https://developer.hashicorp.com/terraform/cli/commands/plan
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern infrastructure drift at organization scale

What operating model detects and reduces IaC drift without blocking incident response?

## Answer guide

- Define ownership and an expected reconciliation time by resource criticality; schedule read-only plan/drift checks and route findings to the owning team with enough context to decide intent.
- Permit time-bounded emergency changes with an auditable record, then require configuration reconciliation or explicit retirement of the managed object.
- Track drift age, recurrence, coverage, and changes by identity to distinguish provider noise from access-control or process failures.
- Do not auto-apply every detected difference. Some differences represent an approved emergency fix, an unsafe provider interpretation, or a configuration bug; reconciliation needs an accountable decision.
- Organization-scale drift governance is tool-composable rather than Terraform-specific: scheduled read-only detection exists as OpenTofu plans, CloudFormation drift status, or Pulumi refresh, and the governance layer — ownership, expected reconciliation time, audited emergency changes — is identical over any of them.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: plan command](https://developer.hashicorp.com/terraform/cli/commands/plan)
- [Terraform: refresh-only mode tutorial](https://developer.hashicorp.com/terraform/tutorials/state/refresh)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
