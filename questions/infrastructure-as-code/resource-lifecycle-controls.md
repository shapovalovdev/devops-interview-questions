---
title: Use Terraform lifecycle rules without masking risk
theme: infrastructure-as-code
difficulty: middle
type: scenario
tags: [terraform, infrastructure-as-code, deployment, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html
    source_type: official-docs
    verified_on: 2026-08-16
---

# Use Terraform lifecycle rules without masking risk

How should a team use Terraform lifecycle meta-arguments for a critical resource?

## Answer guide

- Use `prevent_destroy` to make destructive replacement or removal require an explicit configuration change, and use `create_before_destroy` only when the provider and service design can tolerate duplicate overlap.
- Use `replace_triggered_by` to model a deliberate replacement relationship rather than relying on incidental change ordering.
- Treat `ignore_changes` as a narrow, documented exception for an externally managed attribute; it deliberately tells Terraform not to reconcile that drift.
- Lifecycle rules cannot create provider capabilities. `create_before_destroy` can fail on globally unique names, quotas, or services that cannot run two copies; test the actual replacement path.
- Declarative replacement and retention controls have peers: CloudFormation's DeletionPolicy and UpdateReplacePolicy Retain give templates the same prevent-accidental-destroy leverage that prevent_destroy gives here, and Pulumi's protect resource option is the imperative-side equivalent.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: lifecycle meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle)
- [Terraform: Resource syntax](https://developer.hashicorp.com/terraform/language/resources/syntax)
- [AWS CloudFormation — UpdateReplacePolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
