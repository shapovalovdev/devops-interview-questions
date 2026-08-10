---
title: Explain serverless payload, memory, and duration limits
theme: serverless
difficulty: junior
type: theory
tags: [cloud, limits, reliability, performance]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Explain serverless payload, memory, and duration limits

Which platform quotas constrain a function design, and how do you tell a hard limit from a tunable one?

## Answer guide

- Serverless platforms publish quotas in several independent families: request and response payload size, deployment package and uncompressed image size, ephemeral disk, memory, maximum invocation duration, and account-level concurrency. Each family fails differently, so read them as separate design constraints rather than one number.
- Some quotas are tunable per function—memory, timeout, ephemeral storage, reserved concurrency—and some are account quotas that can be raised by request. A smaller group is architectural: synchronous request and response payload ceilings do not move, which is why large objects travel by reference to object storage instead of inline in the event.
- Memory is usually the single knob that also buys CPU and network throughput, so a function that looks memory-bound is often really CPU-starved. Raising memory can reduce both duration and total cost, and the only honest way to pick a value is to measure across candidate settings.
- Check version-specific values in the provider's quota page rather than memorising them; providers raise ceilings over time, and answers that quote a stale number age badly.
- Failure modes to expect: a payload that grows past the synchronous response ceiling once a customer scales up, a package that stops deploying after a dependency upgrade, a timeout raised without raising the caller's timeout so retries stack, and concurrency exhaustion that throttles unrelated functions sharing the account quota.

## References

- [AWS Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- Further reading (blog): [Datadog — State of Serverless research](https://www.datadoghq.com/state-of-serverless/)

## What to learn next

- Official documentation: [AWS Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- Manual or specification: [AWS Lambda API reference — CreateFunction](https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunction.html)
- Maintainer or personal blog: [Yan Cui — theburningmonk on serverless practice](https://theburningmonk.com/)
- Technical blog: [Datadog — State of Serverless](https://www.datadoghq.com/state-of-serverless/)
- Hands-on guide: [Get started with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
