---
title: Create a risk-based IaC change-management model
theme: infrastructure-as-code
difficulty: staff
type: scenario
tags: [terraform, infrastructure-as-code, governance, deployment, reliability, security]
sources:
  - url: https://developer.hashicorp.com/terraform/cli/commands/plan
    source_type: official-docs
    verified_on: 2026-08-06
---

# Create a risk-based IaC change-management model

How would you scale IaC approvals without applying the same process to every change?

## Answer guide

- Classify plans by impact signals such as destructive actions, privilege changes, public network exposure, production scope, data movement, and replacement of stateful services.
- Require the evidence proportionate to the risk: reviewed plan, owner approval, maintenance/cutover plan, rollback evidence, and policy result. Low-risk repeatable changes should flow automatically through protected CI.
- Preserve the reviewed configuration, plan metadata, policy decision, actor identity, and apply result for audit and incident investigation.
- A plan becomes stale when inputs or remote infrastructure change. Risk classification reduces review noise; it does not make a speculative plan safe to apply later without revalidation.

## References

- [Terraform: plan command](https://developer.hashicorp.com/terraform/cli/commands/plan)
- [Terraform: apply command](https://developer.hashicorp.com/terraform/cli/commands/apply)
