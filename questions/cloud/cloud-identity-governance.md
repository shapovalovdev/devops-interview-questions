---
title: Govern cloud identity at organization scale
theme: cloud
difficulty: staff
type: scenario
tags: [aws, cloud, iam, security, governance, least-privilege]
sources:
  - url: https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://learn.microsoft.com/entra/fundamentals/what-is-entra
    source_type: official-docs
    verified_on: 2026-08-16
---

# Govern cloud identity at organization scale

How do you provide engineers access to many cloud accounts without long-lived user credentials or uncontrolled administrator roles?

## Answer guide

- Federate workforce identities through IAM Identity Center or an external identity provider and assign permission sets to named job functions and accounts. Require short-lived sessions, MFA, and centrally auditable access.
- Separate human break-glass access from routine automation; use dedicated workload roles with explicit trust policies, minimal permissions, and separate deployment paths.
- Review assignments, privileged roles, unused permissions, and access logs regularly. Make access requests, elevation, and emergency access time-bounded and traceable.
- Avoid sharing root credentials or static access keys. Root users have exceptional authority and should be protected, monitored, and used only for tasks that require them.
- Workforce federation has named peers: Microsoft Entra ID assigns group and application entitlements where AWS uses permission sets, and Google Cloud maps an external identity provider onto IAM roles — the short-lived, audited, least-privilege argument is unchanged by the vendor.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Further reading: AWS IAM root user best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)
- [Microsoft Entra ID — what is Entra](https://learn.microsoft.com/entra/fundamentals/what-is-entra)

## What to learn next

- Official documentation: [AWS IAM Identity Center guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- Manual or specification: [IAM root-user best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)
- Maintainer or personal blog: [Corey Quinn — Last Week in AWS](https://www.lastweekinaws.com/blog/)
- Technical blog: [AWS Security Blog](https://aws.amazon.com/blogs/security/)
- Hands-on guide: [AWS IAM workshops](https://catalog.workshops.aws/iam/en-US)
