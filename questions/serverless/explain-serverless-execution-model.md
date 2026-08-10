---
title: Explain the serverless function execution model
theme: serverless
difficulty: junior
type: theory
tags: [cloud, architecture, event-driven, performance]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Explain the serverless function execution model

What actually happens between an event arriving and your function code returning, and why does that shape how you write the code?

## Answer guide

- A managed service owns the lifecycle. It receives an event from a trigger, selects or creates an execution environment, loads your package, runs an initialization phase once, then calls your handler with the event payload. The platform, not your process, decides how many environments exist and when they disappear.
- One execution environment serves one request at a time in the classic function-as-a-service model, so parallelism comes from the platform starting more environments rather than from threads inside yours. Scaling is therefore a property of the invocation path and its configured limits, not of your web framework.
- Environments are reused opportunistically. Work done outside the handler—clients, connection pools, parsed configuration—survives between invocations on the same environment, which is the reason initialization cost is amortized but also the reason leaked global state produces cross-request bugs.
- Environments are frozen after the response and can be reclaimed at any time. Background threads, deferred writes, and buffered telemetry started during one invocation may never run, so anything that must complete has to complete before the handler returns.
- Failure modes to expect: a slow initialization phase that shows up as tail latency, mutable module-level state that leaks data between tenants, and work scheduled after the response that silently disappears when the environment is frozen.

## References

- [AWS Lambda concepts](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html)
- Further reading (blog): [AWS Compute Blog — serverless engineering articles](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [AWS Lambda concepts and execution environments](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html)
- Manual or specification: [AWS Lambda API reference — Invoke](https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html)
- Maintainer or personal blog: [Marc Brooker — distributed systems and serverless internals](https://brooker.co.za/blog/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [Get started with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
