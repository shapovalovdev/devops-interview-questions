---
title: Explain synchronous and asynchronous serverless invocation
theme: serverless
difficulty: junior
type: theory
tags: [cloud, event-driven, reliability, message-queues]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Explain synchronous and asynchronous serverless invocation

What changes about errors, retries, and latency when the same function is called synchronously versus asynchronously?

## Answer guide

- Synchronous invocation holds the caller open until the function returns. The caller receives the result or the error directly, and the platform does not retry on its own: retry policy belongs to the client SDK or the calling service, which is why duplicated work here is the caller's decision.
- Asynchronous invocation hands the event to a managed internal queue and returns an acknowledgement immediately. The platform then invokes the function on the caller's behalf and retries failed invocations according to its own policy, with unprocessable events routed to a dead-letter or on-failure destination once attempts are exhausted.
- Event-source mappings—queues, streams, and topics—are a third mode. The platform polls the source and controls batching, ordering within a partition or message group, and whether a failure returns the whole batch or only the unprocessed remainder for redelivery.
- The practical consequence is delivery semantics: asynchronous and poll-based paths are at-least-once, so handlers must tolerate the same event arriving twice. Only the synchronous path lets the caller observe the error, so asynchronous failures are invisible unless you monitor the platform's error and dead-letter metrics.
- Failure modes to expect: an asynchronous handler whose exception is retried into a duplicate side effect, a caller timeout shorter than the function timeout that causes work to complete after the client gave up, and a dead-letter target nobody alerts on so poison events accumulate unnoticed.

## References

- [AWS Lambda synchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html)
- [AWS Lambda asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)
- Further reading (blog): [AWS Compute Blog — event-driven architecture articles](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [AWS Lambda asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)
- Manual or specification: [CloudEvents specification](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md)
- Maintainer or personal blog: [Yan Cui — theburningmonk on event-driven design](https://theburningmonk.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [Knative getting started](https://knative.dev/docs/getting-started/)
