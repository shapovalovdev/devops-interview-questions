---
title: Choose a serverless trigger safely
theme: serverless
difficulty: junior
type: theory
tags: [cloud, event-driven, reliability, architecture]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Choose a serverless trigger safely

How do you choose between a synchronous request, queue, stream, or scheduled trigger for a function?

## Answer guide

- Start with the caller’s delivery, latency, ordering, and failure requirements. A synchronous trigger suits an immediate response; a queue absorbs bursts; a stream carries ordered partitioned records; a schedule suits periodic work.
- Check the trigger’s retry, batching, concurrency, and failure-destination behavior. Those properties vary by source and determine whether the handler must be idempotent, checkpoint progress, or isolate poisoned records.
- Avoid using a function trigger as a substitute for a workflow boundary. A long-running, stateful, or human-approval process needs explicit orchestration; otherwise timeouts and retries can create duplicate effects.

## References

- [AWS Lambda event source mappings and services](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)
- Further reading (blog): [AWS Compute Blog — event-driven Lambda](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [AWS Lambda event sources](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)
- Manual or specification: [AWS Lambda asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)
- Maintainer or personal blog: [Jeremy Daly — serverless articles](https://www.jeremydaly.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [AWS Lambda tutorials](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
