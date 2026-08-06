---
title: Choose for_each or count for repeated Terraform resources
theme: infrastructure-as-code
difficulty: middle
type: theory
tags: [terraform, infrastructure-as-code, automation, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/meta-arguments/for_each
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose for_each or count for repeated Terraform resources

When should you use `for_each` instead of `count` for repeated resources?

## Answer guide

- Use `for_each` when instances have stable, meaningful keys such as service names or account IDs. Terraform tracks instances by those keys.
- Use `count` for truly positional, interchangeable instances where a number is the natural identity.
- Removing an item from a count-based list can shift later indices and cause Terraform to change or replace the wrong logical instance. A `for_each` key avoids that index-shift problem.
- Keys must be known before Terraform performs remote operations and must not contain sensitive values, because they identify resource instances in output and state.

## References

- [Terraform: for_each meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/for_each)
- [Terraform: count meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/count)
