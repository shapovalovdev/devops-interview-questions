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
  - url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/import-resources.html
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://opentofu.org/docs/language/import/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Import an existing resource into Terraform

How do you bring a manually created production resource under Terraform control without accidentally replacing it?

## Answer guide

- Confirm the resource is intended, supported as importable by its provider, and not already bound to another Terraform address; one remote object must map to one resource address.
- Write or generate a resource configuration that describes the desired end state, then declare an import block with the provider-specific resource identity and destination address.
- Review the resulting plan before apply. Import establishes state binding; it does not prove the configuration exactly matches the remote object.
- Test imports on non-production or a copy of state where feasible. Importing the same remote object at two addresses or applying an incomplete configuration can produce unexpected changes.
- Bringing an existing object under declarative management is a shared capability: CloudFormation imports a resource into a stack with a retained physical ID, Pulumi's import marks a resource as managed, and OpenTofu keeps the same import-block flow of configuration plus identity plus reviewed plan.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: Import resources overview](https://developer.hashicorp.com/terraform/language/import)
- [Terraform: Import existing infrastructure](https://developer.hashicorp.com/terraform/cli/import)
- [AWS CloudFormation — import resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/import-resources.html)
- [OpenTofu — import blocks](https://opentofu.org/docs/language/import/)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
