---
title: Diagnose an unexpected AWS IAM authorization decision
theme: cloud
difficulty: middle
type: troubleshooting
tags: [aws, iam, cloud, security, least-privilege]
sources:
  - url: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose an unexpected AWS IAM authorization decision

An API call is denied although an identity policy appears to allow it. What do you check?

## Answer guide

- Identify the exact principal, action, resource, request context, and denial event. IAM evaluates all applicable identity, resource, permissions-boundary, session, organization, and service-control policies.
- An explicit deny overrides an allow; an action without an applicable allow is implicitly denied. Check condition keys, resource ARN shape, assumed-role session, and region or network conditions.
- Use the IAM policy simulator or access analysis as evidence, but reproduce with the least-privileged test role where safe and inspect CloudTrail for the actual request.
- Do not solve an unclear denial by granting AdministratorAccess. That hides the failing policy boundary and expands blast radius; make the minimum source-policy correction and add a regression test.

## References

- Further reading (blog): [Complementary cloud practice article](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/)
- [AWS IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [Further reading: IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)
