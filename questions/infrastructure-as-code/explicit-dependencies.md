---
title: Model Terraform dependencies without overusing depends_on
theme: infrastructure-as-code
difficulty: middle
type: theory
tags: [terraform, infrastructure-as-code, automation, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on
    source_type: official-docs
    verified_on: 2026-08-06
---

# Model Terraform dependencies without overusing depends_on

When is `depends_on` appropriate, and why are expression references preferred?

## Answer guide

- Terraform infers an implicit dependency when one expression uses an attribute from another managed object. This is the preferred, precise way to express data flow.
- Use `depends_on` only for a hidden behavioral dependency that Terraform cannot infer from values, and point it at the smallest relevant object or module.
- Broad module-level `depends_on` can make plans more conservative, obscure why ordering exists, and cause more values to be unknown during planning.
- A dependency controls ordering, not readiness. If an API becomes usable after creation, model that provider behavior or add a separately reviewed readiness mechanism.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: depends_on meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on)
- [Terraform: Resource dependencies](https://developer.hashicorp.com/terraform/language/resources/behavior#resource-dependencies)
