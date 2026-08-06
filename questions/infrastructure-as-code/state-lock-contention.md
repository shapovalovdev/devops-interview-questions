---
title: Handle Terraform state lock contention
theme: infrastructure-as-code
difficulty: middle
type: troubleshooting
tags: [terraform, infrastructure-as-code, troubleshooting, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/state/locking
    source_type: official-docs
    verified_on: 2026-08-06
---

# Handle Terraform state lock contention

What do you do when Terraform cannot acquire a state lock in a shared environment?

## Answer guide

- Stop and identify the run and owner holding the lock; a lock protects state-writing operations from concurrent writers when the backend supports locking.
- Wait for or safely terminate the confirmed stale run according to the incident/change process. Inspect CI logs and backend audit records before intervening.
- Use `force-unlock` only when you know the lock belongs to your failed operation and use the lock ID Terraform reports. Unlocking another active writer can permit state corruption.
- Do not routinely disable locking with `-lock=false`; it converts a controlled wait into a race and does not solve backlog or workflow design problems.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: State locking](https://developer.hashicorp.com/terraform/language/state/locking)
- [Terraform: Backend configuration](https://developer.hashicorp.com/terraform/language/backend)
