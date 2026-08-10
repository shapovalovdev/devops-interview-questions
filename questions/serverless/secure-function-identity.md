---
title: Secure serverless function identity
theme: serverless
difficulty: middle
type: scenario
tags: [cloud, iam, security, least-privilege]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Secure serverless function identity

How do you give a function access to dependencies without embedding long-lived credentials?

## Answer guide

- Give the function a dedicated execution role and grant only the actions, resources, and conditions required by its current workload. Separate roles reduce blast radius and make access review meaningful.
- Use the provider’s workload identity and short-lived credentials rather than environment variables containing static access keys. Scope secrets separately and rotate or revoke them through their owning system.
- Audit denied calls, role changes, and unexpected resource access. Broad wildcard policies can make a small handler compromise an account; overly narrow policies can cause retries and outages, so validate permissions in deployment tests.

## References

- [AWS Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)
- Further reading (blog): [AWS Compute Blog — Lambda security](https://aws.amazon.com/blogs/compute/operating-lambda-building-a-solid-security-foundation/)

## What to learn next

- Official documentation: [AWS Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)
- Manual or specification: [AWS IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- Maintainer or personal blog: [Jeremy Daly — serverless articles](https://www.jeremydaly.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [AWS Lambda tutorials](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
