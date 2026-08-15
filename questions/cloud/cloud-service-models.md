---
title: Choose an appropriate cloud service model
theme: cloud
difficulty: junior
type: theory
tags: [cloud, security, reliability]
sources:
  - url: https://docs.aws.amazon.com/whitepapers/latest/aws-overview/amazon-web-services-cloud-platform.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://csrc.nist.gov/pubs/sp/800/145/final
    source_type: standard
    verified_on: 2026-08-16
---

# Choose an appropriate cloud service model

How do IaaS, PaaS, and SaaS change a team's operational responsibilities?

## Answer guide

- IaaS supplies virtualized infrastructure; the customer still operates the guest OS, runtime, application, and much of its security configuration. PaaS supplies a managed application platform, while SaaS supplies a finished application operated largely by its provider.
- Moving up this spectrum trades control and customization for less undifferentiated operational work. The responsibility is not eliminated: the customer remains responsible for data, identities, access configuration, and how it uses the service.
- Select the least-managed model that satisfies required control, portability, compliance, latency, and operational skills. Document which controls are provider-operated and which the product team owns.
- A common failure is assuming a managed service makes every security or availability duty the provider's problem. Misconfigured identity, data retention, network access, or client retry behavior still causes outages and exposure.
- The IaaS/PaaS/SaaS split predates AWS: NIST SP 800-145 defines the three service models vendor-neutrally, and Azure's and Google Cloud's responsibility models draw the same customer-duties line, so argue from the model boundary rather than from a product name.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS overview: cloud service models](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/amazon-web-services-cloud-platform.html)
- [Further reading: AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [NIST SP 800-145 — The NIST Definition of Cloud Computing](https://csrc.nist.gov/pubs/sp/800/145/final)

## What to learn next

- Official documentation: [AWS overview: cloud service models](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/amazon-web-services-cloud-platform.html)
- Manual or specification: [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [AWS Cloud Quest](https://aws.amazon.com/training/digital/aws-cloud-quest/)
