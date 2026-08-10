---
title: Trace a request across ephemeral serverless components
theme: serverless
difficulty: middle
type: troubleshooting
tags: [cloud, observability, latency, debugging, event-driven]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Trace a request across ephemeral serverless components

Users report intermittent slowness across a chain of functions and queues. You cannot log into anything. How do you find where the time goes?

## Answer guide

- Distributed tracing is the only workable answer, because there is no host to inspect and no process that outlives the request. Instrument every hop so that a single trace identifier travels from the entry point through each function, queue, and datastore call, and make sure that identifier is also emitted on every structured log line so traces and logs join.
- The mechanism to explain: context propagation happens in metadata, not in the payload body. Synchronous HTTP hops carry it in headers; asynchronous hops must carry it in message attributes or event metadata, because the message body is the application's contract and the queue is where causal links are usually lost. Sampling decisions must propagate too, or downstream spans of a sampled trace go missing.
- Serverless traces need spans the platform owns as well as spans your code owns. Initialization time, queue residency, batch handling, and retry attempts belong in the trace; otherwise a chart of handler duration looks healthy while users experience seconds of waiting. Record attempt number and cold-start status as span attributes so a slow tail can be attributed rather than guessed at.
- Constraints worth naming: telemetry buffered in memory can be lost when an environment is frozen after the response, so use the platform's telemetry or extension mechanism to flush rather than a background thread. Vendor-neutral instrumentation through OpenTelemetry keeps the data portable, at the cost of some added initialization weight in the function.
- Failure modes to expect: broken traces at every asynchronous boundary because propagation was never implemented, head-based sampling that discards exactly the rare slow requests you are chasing, tracing added only to the entry function so the real culprit is invisible, and cardinality from per-request identifiers turned into metric labels, which quietly bankrupts the metrics backend.

## References

- [Using AWS X-Ray with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html)
- Further reading (blog): [AWS Compute Blog — serverless observability articles](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [Lambda Telemetry API](https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api.html)
- Manual or specification: [OpenTelemetry semantic conventions for FaaS](https://opentelemetry.io/docs/specs/semconv/faas/)
- Maintainer or personal blog: [Yan Cui — theburningmonk on serverless observability](https://theburningmonk.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [Getting started with AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-gettingstarted.html)
