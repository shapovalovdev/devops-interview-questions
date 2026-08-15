---
title: Govern data classification in cloud services
theme: cloud
difficulty: staff
type: scenario
tags: [aws, cloud, security, governance, storage]
sources:
  - url: https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-classification.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/azure/well-architected/security/data-classification
    source_type: official-docs
    verified_on: 2026-08-16
---

# Govern data classification in cloud services

How would you ensure cloud teams apply appropriate controls to sensitive data without relying on ad-hoc judgment?

## Answer guide

- Define a small data-classification scheme based on sensitivity, regulatory obligations, retention, residency, and business impact. Publish examples and require an owner for each important data store and flow.
- Map each class to technical controls: identity access, encryption and key ownership, logging/redaction, backup retention, network exposure, and approved service patterns. Automate discovery and policy checks where signals are reliable.
- Review classifications when schemas, integrations, regions, or purpose change, and make data handling part of design and incident reviews. Provide a fast exception process with compensating controls.
- Do not rely solely on a bucket tag or encryption checkbox. Classification fails when data copies, logs, exports, backups, and analytics paths are not included in the inventory.
- Classification schemes travel across clouds: Azure's Well-Architected data-classification guidance drives encryption, access, and retention controls from sensitivity tiers in the same way, and GCP sensitive-data tooling implements the discovery half of it — define the taxonomy once, provider-neutrally.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS Well-Architected Security Pillar: data classification](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-classification.html)
- [Further reading: AWS Macie sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- [Azure Well-Architected — data classification](https://learn.microsoft.com/azure/well-architected/security/data-classification)

## What to learn next

- Official documentation: [AWS data classification guidance](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-classification.html)
- Manual or specification: [Amazon Macie overview](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Security Blog](https://aws.amazon.com/blogs/security/)
- Hands-on guide: [AWS data protection workshops](https://catalog.workshops.aws/security/en-US)
