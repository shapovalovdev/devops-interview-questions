---
title: Establish a governed cloud landing zone
theme: cloud
difficulty: staff
type: scenario
tags: [aws, cloud, governance, security, platform-engineering, cnpa, must-know]
sources:
  - url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/landing-zone.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Establish a governed cloud landing zone

What should a staff engineer establish before many teams independently deploy into AWS?

## Answer guide

- Create a landing zone that provides account structure, identity federation, baseline networking, centralized logging, security monitoring, billing visibility, and a repeatable account-vending path.
- Encode non-negotiable controls as organization-level guardrails and automate the baseline. Give teams documented self-service interfaces with clear ownership rather than requiring a central team to hand-configure every resource.
- Define standards for exceptions, change rollout, control testing, and deprecation. Measure adoption, policy violations, provisioning lead time, and incidents caused by platform defaults.
- Do not confuse centralization with governance. A landing zone that blocks delivery drives unmanaged shadow accounts; one with no enforced baseline makes the shared environment untrustworthy.
- Landing zone is a cross-cloud concept: Azure landing zones and Google's landing-zone guidance prescribe the same identity, network, logging, and account-vending baseline beneath self-service deployment, so specify the enforced baseline rather than Control Tower mechanics.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS Security Reference Architecture: landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/landing-zone.html)
- [Further reading: AWS Control Tower concepts](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- [Azure — landing zone design principles](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/)

## What to learn next

- Official documentation: [AWS landing-zone guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/landing-zone.html)
- Manual or specification: [AWS Control Tower concepts](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [AWS Control Tower workshops](https://catalog.workshops.aws/control-tower/en-US)
