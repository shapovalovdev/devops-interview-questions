---
title: Plan a zero-downtime infrastructure migration with Terraform
theme: infrastructure-as-code
difficulty: senior
type: scenario
tags: [terraform, infrastructure-as-code, deployment, availability, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://opentofu.org/docs/language/meta-arguments/lifecycle/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Plan a zero-downtime infrastructure migration with Terraform

How would you migrate a critical service resource when its configuration requires replacement?

## Answer guide

- First determine whether the provider supports overlapping old and new resources, whether names, addresses, quotas, certificates, and data replication permit it, and define measurable cutover and rollback criteria.
- Model a staged deployment: create and validate the new capacity, shift traffic or consumers through an explicit service-level mechanism, observe health, then retire the old capacity.
- `create_before_destroy` can request replacement ordering, but it does not solve uniqueness constraints, data migration, DNS caching, or client connection draining.
- Test the migration and rollback at representative scale. A Terraform apply graph is not by itself an availability plan.
- The staged create, validate, shift-traffic, retire sequence is engine-neutral: OpenTofu keeps the identical create_before_destroy semantics with the same uniqueness and quota caveats, and on CloudFormation the equivalent dance combines UpdateReplacePolicy with stack-level blue/green patterns.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: lifecycle meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle)
- [Terraform: Resource behavior](https://developer.hashicorp.com/terraform/language/resources/behavior)
- [OpenTofu — lifecycle meta-argument](https://opentofu.org/docs/language/meta-arguments/lifecycle/)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
