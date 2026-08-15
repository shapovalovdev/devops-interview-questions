---
title: Detect and handle infrastructure drift
theme: infrastructure-as-code
difficulty: middle
type: scenario
tags: [terraform, infrastructure-as-code, reliability, troubleshooting, cgoa]
sources:
  - url: https://developer.hashicorp.com/terraform/cli/commands/plan
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html
    source_type: official-docs
    verified_on: 2026-08-16
---

# Detect and handle infrastructure drift

How do you identify a manually changed cloud resource that no longer matches declared infrastructure, and how do you restore control safely?

## Answer guide

- Run `terraform plan` with normal refresh behavior to compare the configuration, prior state, and remote objects. For an intentional out-of-band change, use a reviewed `-refresh-only` plan to inspect proposed state updates without changing infrastructure.
- First establish whether the configuration or the live change represents the intended end state; do not let an automated apply decide that business question.
- Reconcile deliberately: update configuration and apply, import an unmanaged object where supported, or restore the approved configuration. Restrict routine manual changes and record emergency changes to prevent recurring drift.
- Do not use the deprecated `terraform refresh` as an unattended repair step: it updates state automatically and bad provider credentials can produce misleading state changes.
- Drift detection is a shared control: CloudFormation's stack drift detection reports template-versus-live differences on a schedule, Pulumi's refresh updates the stack state from real resources, and OpenTofu's plan with normal refresh behaves identically to Terraform's — reconcile intent deliberately in all of them.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: plan command](https://developer.hashicorp.com/terraform/cli/commands/plan)
- [Terraform: refresh-only mode tutorial](https://developer.hashicorp.com/terraform/tutorials/state/refresh)
- [AWS CloudFormation — stack drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
