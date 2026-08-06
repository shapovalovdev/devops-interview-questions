---
title: Why does Terraform use state?
theme: infrastructure-as-code
difficulty: middle
type: theory
tags: [terraform, infrastructure-as-code, automation, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/state
    source_type: official-docs
    verified_on: 2026-08-06
---

# Why does Terraform use state?

What information does Terraform state hold, and what practices protect it in a team environment?

## Answer guide

- State maps a resource address in configuration to its remote object and retains metadata Terraform needs to plan changes. Without that mapping Terraform cannot reliably determine what it manages.
- A team should store state in a remote backend with restrictive access and a recovery/versioning policy. Use a backend that supports locking where concurrent writers are possible; Terraform locking depends on the selected backend.
- Treat state and saved plans as sensitive: they can contain credentials or values marked sensitive. Do not commit state or backend credentials to source control.
- Review plans, use the `terraform state` subcommands only under a controlled recovery procedure, and never directly edit the state JSON. A stale, lost, or concurrently modified state can lead to duplicate resources or destructive changes.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: State](https://developer.hashicorp.com/terraform/language/state)
- [Terraform: State locking](https://developer.hashicorp.com/terraform/language/state/locking)
