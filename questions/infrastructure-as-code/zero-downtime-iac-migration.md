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
---

# Plan a zero-downtime infrastructure migration with Terraform

How would you migrate a critical service resource when its configuration requires replacement?

## Answer guide

- First determine whether the provider supports overlapping old and new resources, whether names, addresses, quotas, certificates, and data replication permit it, and define measurable cutover and rollback criteria.
- Model a staged deployment: create and validate the new capacity, shift traffic or consumers through an explicit service-level mechanism, observe health, then retire the old capacity.
- `create_before_destroy` can request replacement ordering, but it does not solve uniqueness constraints, data migration, DNS caching, or client connection draining.
- Test the migration and rollback at representative scale. A Terraform apply graph is not by itself an availability plan.

## References

- [Terraform: lifecycle meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle)
- [Terraform: Resource behavior](https://developer.hashicorp.com/terraform/language/resources/behavior)
