---
title: Deploy a serverless function safely
theme: serverless
difficulty: senior
type: scenario
tags: [cloud, deployment, reliability, observability]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Deploy a serverless function safely

How do you release a function change without exposing every invocation to an untested version?

## Answer guide

- Publish an immutable version, then direct traffic through an alias or equivalent deployment boundary. Keep configuration, code, permissions, and event-source changes reviewed as one release contract.
- Shift a small, observable share first and compare business errors, duration, throttles, and dependency behavior against the prior version. Roll back the traffic pointer rather than rebuilding under incident pressure.
- Validate schema compatibility and asynchronous replay behavior. A safe synchronous canary can still poison queued events or break consumers after a full cutover, so maintain a recovery and replay plan.

## References

- [AWS Lambda versions and aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html)
- Further reading (blog): [AWS Compute Blog — safe Lambda deployments](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [AWS Lambda versions and aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html)
- Manual or specification: [AWS Lambda deployment preferences](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
- Maintainer or personal blog: [Jeremy Daly — serverless articles](https://www.jeremydaly.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [AWS Lambda tutorials](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
