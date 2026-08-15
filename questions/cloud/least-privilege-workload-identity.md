---
title: Apply least privilege to a cloud workload identity
theme: cloud
difficulty: middle
type: scenario
tags: [aws, iam, cloud, security, least-privilege]
sources:
  - url: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://cloud.google.com/iam/docs/service-accounts
    source_type: official-docs
    verified_on: 2026-08-16
---

# Apply least privilege to a cloud workload identity

A service needs read access to a single object-storage prefix. How would you grant access without embedding static credentials?

## Answer guide

- Attach an IAM role to the workload's supported compute identity so the application obtains temporary credentials, rather than placing a long-lived access key in its image, configuration, or source repository.
- Grant only the required read actions and the exact bucket/prefix resources. For S3 this normally means separating bucket-level permissions from object ARNs, and adding condition keys only when their request context is understood.
- Keep runtime roles separate from human administrator roles and restrict the role trust policy so an unintended principal cannot assume it. Log access and inspect the actual assumed-role principal during investigations.
- Test both an allowed object read and a denied read outside the prefix. Broad wildcards, resource-policy grants, and an overly broad role trust policy are common ways a narrowly written identity becomes a data-exfiltration path.
- Temporary workload credentials exist everywhere: an Azure managed identity or a GCP service account bound through Workload Identity Federation plays the same role as an IAM role on compute, and both exist precisely to keep long-lived keys out of images and configuration.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Further reading: Amazon S3 IAM policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html)
- [Azure — managed identities for Azure resources](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview)
- [Google Cloud IAM — service accounts](https://cloud.google.com/iam/docs/service-accounts)

## What to learn next

- Official documentation: [AWS IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- Manual or specification: [Amazon S3 IAM policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Security Blog](https://aws.amazon.com/blogs/security/)
- Hands-on guide: [AWS IAM workshops](https://catalog.workshops.aws/iam/en-US)
