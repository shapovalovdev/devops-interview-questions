---
title: Design Terraform outputs without exposing secrets
theme: infrastructure-as-code
difficulty: junior
type: scenario
tags: [terraform, infrastructure-as-code, security, automation]
sources:
  - url: https://developer.hashicorp.com/terraform/language/values/outputs
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://opentofu.org/docs/language/values/outputs/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Design Terraform outputs without exposing secrets

What should a module output, and how do you avoid turning outputs into a secret-distribution channel?

## Answer guide

- Output stable values that a caller genuinely needs, such as an ID, endpoint, or structured connection metadata; outputs form part of a module's public contract.
- Mark secret-derived outputs `sensitive` so Terraform redacts them in normal CLI output, and restrict state access because state still records values Terraform needs.
- Prefer an identity reference or secret-manager path over outputting a credential. Give consumers permission to retrieve the secret rather than broadening state access.
- Changing output names or shapes can break downstream automation, including remote-state consumers, so version and test that interface deliberately.
- Output hygiene has equivalents: OpenTofu keeps the same sensitive-value redaction in CLI output, and Bicep's @secure() decorator and Pulumi's secret outputs play the same protect-at-boundary role — with the same caveat that state still holds the underlying value.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: Output values](https://developer.hashicorp.com/terraform/language/values/outputs)
- [Terraform: Manage sensitive data](https://developer.hashicorp.com/terraform/language/manage-sensitive-data)
- [OpenTofu — output values](https://opentofu.org/docs/language/values/outputs/)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
