---
title: Plan for serverless runtime deprecations across an estate
theme: serverless
difficulty: staff
type: scenario
tags: [cloud, governance, change-management, security, dependencies]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/runtime-support-policy.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Plan for serverless runtime deprecations across an estate

Hundreds of functions run on language runtimes the provider will retire. How do you turn that recurring deadline into a routine process?

## Answer guide

- The underlying fact is that managed runtimes follow the upstream language's support lifecycle, and the provider publishes deprecation dates in advance. After a deprecation date the provider typically stops patching the runtime, then blocks function updates, and finally blocks new function creation—so the risk is not only unpatched code but a function you can no longer change during an incident.
- Build an inventory before a policy. Enumerate every function with its runtime, owner, last deploy, invocation volume, and the pipeline that produces it, using the provider's API rather than a spreadsheet. Most estates discover a long tail of unowned functions at this point, and finding them is the highest-value part of the exercise.
- Choose the upgrade mechanism deliberately. Automatic runtime patch updates keep minor versions current with the least effort but introduce change you did not schedule; pinning a specific runtime version gives control at the cost of an explicit upgrade obligation. Container-image packaging moves the base-image lifecycle into your own supply chain, which is more work and more control. State which mode is the default and which needs an exception.
- Run it as a rolling programme, not an annual scramble: a version policy tied to upstream support, automated detection with a dashboard and alert well before each date, canary and alias-based deployment for the upgrade itself, and a service-level objective for how long an estate may lag. Treat unowned functions as a separate decommissioning workstream with a published shutdown date.
- Failure modes to expect: a rush at the deadline that upgrades runtime and application dependencies simultaneously so failures cannot be attributed, an automatic patch that changes TLS or serialization defaults and breaks a downstream integration, functions frozen out of updates mid-incident, and a low-traffic function nobody upgrades until it fails in an audit.

## References

- [AWS Lambda runtime deprecation policy](https://docs.aws.amazon.com/lambda/latest/dg/runtime-support-policy.html)
- Further reading (blog): [AWS Compute Blog — runtime lifecycle articles](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [AWS Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)
- Manual or specification: [AWS Lambda API reference — GetRuntimeManagementConfig](https://docs.aws.amazon.com/lambda/latest/api/API_GetRuntimeManagementConfig.html)
- Maintainer or personal blog: [Yan Cui — theburningmonk on operating serverless estates](https://theburningmonk.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [Update a Lambda function runtime version](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html)
