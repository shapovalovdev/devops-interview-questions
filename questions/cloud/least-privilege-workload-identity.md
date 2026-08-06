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
---

# Apply least privilege to a cloud workload identity

A service needs read access to a single object-storage prefix. How would you grant access without embedding static credentials?

## Answer guide

- Attach an IAM role to the workload's supported compute identity so the application obtains temporary credentials, rather than placing a long-lived access key in its image, configuration, or source repository.
- Grant only the required read actions and the exact bucket/prefix resources. For S3 this normally means separating bucket-level permissions from object ARNs, and adding condition keys only when their request context is understood.
- Keep runtime roles separate from human administrator roles and restrict the role trust policy so an unintended principal cannot assume it. Log access and inspect the actual assumed-role principal during investigations.
- Test both an allowed object read and a denied read outside the prefix. Broad wildcards, resource-policy grants, and an overly broad role trust policy are common ways a narrowly written identity becomes a data-exfiltration path.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Further reading: Amazon S3 IAM policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html)
