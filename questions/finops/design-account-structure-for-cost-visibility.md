---
title: Design account structure for cost visibility
theme: finops
difficulty: senior
type: scenario
tags: [finops, cost-allocation, cloud, architecture]
sources:
  - url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html
    source_type: official-docs
    verified_on: 2026-08-11
---

# Design account structure for cost visibility

You are designing the account and project layout for a new organisation. How do you make cost visibility a first-class property of that design?

## Answer guide

- Put the cost boundary where the ownership boundary is. An account, project, or subscription is a hard boundary the provider itself reports on, it cannot be forgotten the way a tag can, and it also carries blast radius, quota, and IAM isolation — so aligning it with team or product ownership pays for itself several times over.
- The mechanism is an organisational hierarchy — AWS Organizations with organisational units, Google Cloud folders and projects, Azure management groups and subscriptions — under one payer or billing account so that commitments and volume tiers are shared, with policy applied at the hierarchy level. Environment separation within a product (production, staging, development) then falls out naturally and lets you see non-production spend, which is usually where uncontrolled growth hides.
- Layer tags on top for the dimensions the hierarchy cannot express: which feature, which customer tier, which cost centre. Enforce the mandatory keys with policy at creation time and with infrastructure-as-code defaults, not with a monthly clean-up campaign.
- Material constraints: accounts are not free of overhead — each one needs baseline security, networking, logging, and quota management, so a per-microservice account is usually a mistake; quotas are per account and can become the binding constraint; cross-account networking and data paths can add transfer cost; and consolidating too aggressively recreates the untangling problem you were avoiding.
- Failure modes: a shared "sandbox" account that becomes production by accident and can never be attributed; a structure that mirrors last year's org chart and is never reshaped after a reorg; commitments purchased in a linked account rather than centrally, so the discount cannot float to where usage moves; and no plan for how an account is decommissioned when a product is retired.

## References

- [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)
- [AWS Organizations introduction](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- Further reading (blog): [AWS Architecture blog](https://aws.amazon.com/blogs/architecture/)

## What to learn next

- Official documentation: [AWS Organizations introduction](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- Manual or specification: [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)
- Maintainer or personal blog: [Corey Quinn — Duckbill Group blog](https://www.duckbillgroup.com/blog/)
- Technical blog: [Google Cloud developers and practitioners blog](https://cloud.google.com/blog/topics/developers-practitioners)
- Hands-on guide: [Create and manage Google Cloud labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels)
