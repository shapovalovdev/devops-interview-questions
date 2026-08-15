---
title: Why does Terraform use state?
theme: infrastructure-as-code
difficulty: middle
type: theory
tags: [terraform, infrastructure-as-code, automation, reliability, cgoa]
sources:
  - url: https://developer.hashicorp.com/terraform/language/state
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://opentofu.org/docs/language/state/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Why does Terraform use state?

What information does Terraform state hold, and what practices protect it in a team environment?

## Answer guide

- State maps a resource address in configuration to its remote object and retains metadata Terraform needs to plan changes. Without that mapping Terraform cannot reliably determine what it manages.
- A team should store state in a remote backend with restrictive access and a recovery/versioning policy. Use a backend that supports locking where concurrent writers are possible; Terraform locking depends on the selected backend.
- Treat state and saved plans as sensitive: they can contain credentials or values marked sensitive. Do not commit state or backend credentials to source control.
- Review plans, use the `terraform state` subcommands only under a controlled recovery procedure, and never directly edit the state JSON. A stale, lost, or concurrently modified state can lead to duplicate resources or destructive changes.
- The need for a configuration-to-object map is what state is, and other tools answer it differently: OpenTofu state is identical by fork lineage, Pulumi keeps its own statefile, and CloudFormation stores the binding service-side — explaining any of them starts from this mapping argument.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: State](https://developer.hashicorp.com/terraform/language/state)
- [Terraform: State locking](https://developer.hashicorp.com/terraform/language/state/locking)
- [OpenTofu — state](https://opentofu.org/docs/language/state/)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
