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
---

# Design Terraform outputs without exposing secrets

What should a module output, and how do you avoid turning outputs into a secret-distribution channel?

## Answer guide

- Output stable values that a caller genuinely needs, such as an ID, endpoint, or structured connection metadata; outputs form part of a module's public contract.
- Mark secret-derived outputs `sensitive` so Terraform redacts them in normal CLI output, and restrict state access because state still records values Terraform needs.
- Prefer an identity reference or secret-manager path over outputting a credential. Give consumers permission to retrieve the secret rather than broadening state access.
- Changing output names or shapes can break downstream automation, including remote-state consumers, so version and test that interface deliberately.

## References

- [Terraform: Output values](https://developer.hashicorp.com/terraform/language/values/outputs)
- [Terraform: Manage sensitive data](https://developer.hashicorp.com/terraform/language/manage-sensitive-data)
