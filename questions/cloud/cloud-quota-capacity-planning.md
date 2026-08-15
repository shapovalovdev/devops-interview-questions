---
title: Prevent cloud service quotas from becoming an outage
theme: cloud
difficulty: senior
type: scenario
tags: [aws, cloud, capacity-planning, reliability, monitoring]
sources:
  - url: https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://cloud.google.com/docs/quotas
    source_type: official-docs
    verified_on: 2026-08-16
---

# Prevent cloud service quotas from becoming an outage

How should a team manage AWS service quotas when planning a large launch or recovery?

## Answer guide

- Inventory quotas that constrain steady state, scaling, and disaster recovery across the accounts and Regions actually used. Service quotas are not universally identical and some can be adjusted while others cannot.
- Monitor usage against relevant quotas, forecast peak and recovery capacity, and request increases well before a launch. Validate the approved value in the target account and Region.
- Include quota consumption in load tests and DR exercises; a regional recovery may need substantially more capacity than normal operation and might contend with other workloads.
- Do not assume an autoscaling policy guarantees capacity. It can request more resources only until a quota, account limit, instance availability, or downstream dependency is reached.
- Admission control by quota exists everywhere: Azure enforces per-subscription and per-region service limits and Google Cloud per-project quotas, and a quota-increase request on either provider plays the same pre-launch role as a Service Quotas raise — plan for it in whichever cloud the launch lands.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS Service Quotas User Guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
- [Further reading: AWS Service Quotas console](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html#intro-how-it-works)
- [Azure — subscription service limits](https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits)
- [Google Cloud — working with quotas](https://cloud.google.com/docs/quotas)

## What to learn next

- Official documentation: [AWS Service Quotas guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
- Manual or specification: [Service Quotas console concepts](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html#intro-how-it-works)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [AWS Well-Architected Labs](https://www.wellarchitectedlabs.com/)
