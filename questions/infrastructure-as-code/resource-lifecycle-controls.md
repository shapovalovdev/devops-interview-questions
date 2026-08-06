---
title: Use Terraform lifecycle rules without masking risk
theme: infrastructure-as-code
difficulty: middle
type: scenario
tags: [terraform, infrastructure-as-code, deployment, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use Terraform lifecycle rules without masking risk

How should a team use Terraform lifecycle meta-arguments for a critical resource?

## Answer guide

- Use `prevent_destroy` to make destructive replacement or removal require an explicit configuration change, and use `create_before_destroy` only when the provider and service design can tolerate duplicate overlap.
- Use `replace_triggered_by` to model a deliberate replacement relationship rather than relying on incidental change ordering.
- Treat `ignore_changes` as a narrow, documented exception for an externally managed attribute; it deliberately tells Terraform not to reconcile that drift.
- Lifecycle rules cannot create provider capabilities. `create_before_destroy` can fail on globally unique names, quotas, or services that cannot run two copies; test the actual replacement path.

## References

- [Terraform: lifecycle meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle)
- [Terraform: Resource syntax](https://developer.hashicorp.com/terraform/language/resources/syntax)
