---
title: Import an existing resource into Terraform
theme: infrastructure-as-code
difficulty: middle
type: scenario
tags: [terraform, infrastructure-as-code, automation, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/import
    source_type: official-docs
    verified_on: 2026-08-06
---

# Import an existing resource into Terraform

How do you bring a manually created production resource under Terraform control without accidentally replacing it?

## Answer guide

- Confirm the resource is intended, supported as importable by its provider, and not already bound to another Terraform address; one remote object must map to one resource address.
- Write or generate a resource configuration that describes the desired end state, then declare an import block with the provider-specific resource identity and destination address.
- Review the resulting plan before apply. Import establishes state binding; it does not prove the configuration exactly matches the remote object.
- Test imports on non-production or a copy of state where feasible. Importing the same remote object at two addresses or applying an incomplete configuration can produce unexpected changes.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: Import resources overview](https://developer.hashicorp.com/terraform/language/import)
- [Terraform: Import existing infrastructure](https://developer.hashicorp.com/terraform/cli/import)
