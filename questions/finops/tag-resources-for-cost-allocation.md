---
title: Tag resources for cost allocation
theme: finops
difficulty: junior
type: theory
tags: [finops, tagging, cost-allocation, cloud]
sources:
  - url: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html
    source_type: official-docs
    verified_on: 2026-08-11
  - url: https://cloud.google.com/resource-manager/docs/creating-managing-labels
    source_type: official-docs
    verified_on: 2026-08-11
---

# Tag resources for cost allocation

What makes a cost-allocation tagging scheme work, and what breaks one?

## Answer guide

- A workable scheme is a small, mandatory set of keys with controlled values — owner, service, environment, cost-centre — applied consistently across every account and provider, rather than a large optional vocabulary that each team fills in its own way.
- Mechanically, a tag only becomes a billing dimension after it is activated as a cost-allocation tag in the billing account, and activation is not retrospective: AWS applies activated user-defined tags from the point of activation forward, and Google Cloud labels appear in the billing export only for resources that carried them when usage was recorded. So the scheme must be activated before the reporting period it is meant to explain.
- Material constraints: not every resource type supports tags, tags do not propagate automatically from a parent to children in most services, key comparison is case-sensitive in reporting even where the API is lenient, and there are hard limits on the number of keys per resource and activated keys per payer account.
- Failure modes: free-text values that fragment into `Prod`, `prod`, and `production`; tags applied by hand and lost on the next redeploy because the infrastructure code does not set them; resources created by autoscalers, managed services, or the console with no tags at all; and a policy that blocks untagged creation being switched off during an incident and never switched back.

## References

- [AWS user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
- [Create and manage Google Cloud labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels)
- Further reading (blog): [Vantage engineering blog](https://www.vantage.sh/blog)

## What to learn next

- Official documentation: [AWS user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
- Manual or specification: [FinOps Framework — allocation capability](https://www.finops.org/framework/capabilities/allocation/)
- Maintainer or personal blog: [Corey Quinn — Duckbill Group blog](https://www.duckbillgroup.com/blog/)
- Technical blog: [AWS Cloud Financial Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/)
- Hands-on guide: [Enable Azure Cost Management tag inheritance](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-tag-inheritance)
