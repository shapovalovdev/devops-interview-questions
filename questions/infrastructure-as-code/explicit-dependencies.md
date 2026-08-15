---
title: Model Terraform dependencies without overusing depends_on
theme: infrastructure-as-code
difficulty: middle
type: theory
tags: [terraform, infrastructure-as-code, automation, reliability]
sources:
  - url: https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://opentofu.org/docs/language/meta-arguments/depends_on/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Model Terraform dependencies without overusing depends_on

When is `depends_on` appropriate, and why are expression references preferred?

## Answer guide

- Terraform infers an implicit dependency when one expression uses an attribute from another managed object. This is the preferred, precise way to express data flow.
- Use `depends_on` only for a hidden behavioral dependency that Terraform cannot infer from values, and point it at the smallest relevant object or module.
- Broad module-level `depends_on` can make plans more conservative, obscure why ordering exists, and cause more values to be unknown during planning.
- A dependency controls ordering, not readiness. If an API becomes usable after creation, model that provider behavior or add a separately reviewed readiness mechanism.
- The explicit-versus-inferred dependency split recurs: CloudFormation's DependsOn is the same last-resort attribute for ordering inference cannot see, with Ref and Fn::GetAtt playing the expression-reference role that makes ordering derive from data flow.

## References

- Further reading (blog): [Complementary infrastructure as code practice article](https://support.hashicorp.com/hc/en-us/articles/45101629429523-Best-Practices-Organising-Terraform-and-Application-Code)
- [Terraform: depends_on meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on)
- [Terraform: Resource dependencies](https://developer.hashicorp.com/terraform/language/resources/behavior#resource-dependencies)
- [AWS CloudFormation — DependsOn attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html)
- [OpenTofu — depends_on meta-argument](https://opentofu.org/docs/language/meta-arguments/depends_on/)

## What to learn next

- Official documentation: [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- Manual or specification: [Terraform configuration language reference](https://developer.hashicorp.com/terraform/language/syntax/configuration)
- Maintainer or personal blog: [Martin Atkins — Terraform and HCL articles](https://log.martinatkins.me/)
- Technical blog: [HashiCorp engineering blog](https://www.hashicorp.com/blog)
- Hands-on guide: [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
