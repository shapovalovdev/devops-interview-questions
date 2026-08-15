---
title: Design policy-as-code gates for Terraform delivery
theme: infrastructure-as-code
difficulty: senior
type: scenario
tags: [terraform, infrastructure-as-code, security, automation, governance, cgoa]
sources:
  - url: https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://www.openpolicyagent.org/docs/policy-language/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Design policy-as-code gates for Terraform delivery

How would you add policy-as-code without creating an unreviewable delivery bottleneck?

## Answer guide

- Evaluate policy against a machine-readable plan before apply and make the policy decision visible in code review and CI output.
- Start with high-impact invariants such as public exposure, encryption, required ownership, and disallowed regions; assign policy owners, tests, exceptions, and an expiry process.
- Separate advisory findings from mandatory blocks, and provide a documented emergency exception with audit evidence rather than encouraging bypasses.
- Policies cannot validate everything: provider APIs, runtime identity, and existing out-of-band resources may need complementary controls and monitoring.
- Policy evaluation does not require a vendor platform: Open Policy Agent with Rego evaluates a Terraform or OpenTofu plan's JSON representation in CI just as Sentinel does inside HCP Terraform, keeping the gate portable across forks and tools.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [HCP Terraform: Policy enforcement](https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement)
- [Terraform: JSON output format](https://developer.hashicorp.com/terraform/internals/json-format)
- [Open Policy Agent — policy language](https://www.openpolicyagent.org/docs/policy-language/)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
