---
title: Distinguish Terraform local values from data sources
theme: infrastructure-as-code
difficulty: junior
type: theory
tags: [terraform, infrastructure-as-code, automation]
sources:
  - url: https://developer.hashicorp.com/terraform/language/values/locals
    source_type: official-docs
    verified_on: 2026-08-06
---

# Distinguish Terraform local values from data sources

When should you use a local value versus a data source in Terraform?

## Answer guide

- A local value names an expression calculated from configuration; it does not query an external system. Use it to avoid repeating a meaningful expression.
- A data source reads information exposed by a provider, such as an existing network or image. Its result can change outside the configuration and can affect a plan.
- Keep data-source selection explicit and constrained—for example, specify an immutable image identifier rather than selecting an ambiguous "latest" result.
- Excessive locals can obscure values and dependency flow, while unbounded data-source lookups can make plans slow or non-deterministic.

## References

- [Terraform: Local values](https://developer.hashicorp.com/terraform/language/values/locals)
- [Terraform: Data sources](https://developer.hashicorp.com/terraform/language/data-sources)
