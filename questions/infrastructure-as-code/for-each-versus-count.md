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
  - url: https://opentofu.org/docs/language/meta-arguments/for_each/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Choose for_each or count for repeated Terraform resources

When should you use `for_each` instead of `count` for repeated resources?

## Answer guide

- Use `for_each` when instances have stable, meaningful keys such as service names or account IDs. Terraform tracks instances by those keys.
- Use `count` for truly positional, interchangeable instances where a number is the natural identity.
- Removing an item from a count-based list can shift later indices and cause Terraform to change or replace the wrong logical instance. A `for_each` key avoids that index-shift problem.
- Keys must be known before Terraform performs remote operations and must not contain sensitive values, because they identify resource instances in output and state.
- OpenTofu implements the identical for_each and count meta-arguments, so the key-versus-index rule transfers verbatim; the index-shift hazard it avoids is generic, afflicting any tool where repeated resources are enumerated positionally rather than keyed.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: for_each meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/for_each)
- [Terraform: count meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/count)
- [OpenTofu — for_each meta-argument](https://opentofu.org/docs/language/meta-arguments/for_each/)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
