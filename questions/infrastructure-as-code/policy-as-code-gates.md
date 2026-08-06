---
title: Design policy-as-code gates for Terraform delivery
theme: infrastructure-as-code
difficulty: senior
type: scenario
tags: [terraform, infrastructure-as-code, security, automation, governance]
sources:
  - url: https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design policy-as-code gates for Terraform delivery

How would you add policy-as-code without creating an unreviewable delivery bottleneck?

## Answer guide

- Evaluate policy against a machine-readable plan before apply and make the policy decision visible in code review and CI output.
- Start with high-impact invariants such as public exposure, encryption, required ownership, and disallowed regions; assign policy owners, tests, exceptions, and an expiry process.
- Separate advisory findings from mandatory blocks, and provide a documented emergency exception with audit evidence rather than encouraging bypasses.
- Policies cannot validate everything: provider APIs, runtime identity, and existing out-of-band resources may need complementary controls and monitoring.

## References

- [HCP Terraform: Policy enforcement](https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement)
- [Terraform: JSON output format](https://developer.hashicorp.com/terraform/internals/json-format)
