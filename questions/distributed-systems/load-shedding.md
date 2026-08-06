---
title: Shed load to preserve a critical service
theme: distributed-systems
difficulty: middle
type: scenario
tags: [availability, capacity-planning, reliability]
sources:
  - url: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Shed load to preserve a critical service

How do you decide what work to reject when demand exceeds safe capacity?

## Answer guide

- Establish the protected resource and an admission signal, such as queue depth, concurrency, CPU saturation, or a downstream error budget. Rank requests by business importance and reject or defer lower-value work early with a clear retryable response.
- Keep a reserve for health checks and critical operations, bound queues, and measure both accepted and shed traffic. Capacity plans should account for a failed zone and recovery bursts rather than normal-average load alone.
- Unbounded queues hide overload as latency and memory growth. Random shedding can reject critical work, while retrying all rejected traffic recreates the spike; ensure clients back off and operators can see which class is being degraded.

## References

- [AWS Builders' Library: using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/)
- Further reading (personal blog): [Marc Brooker: queueing](https://brooker.co.za/blog/2018/06/20/fairness.html)

## What to learn next

- Official documentation: [Envoy overload manager](https://www.envoyproxy.io/docs/envoy/latest/configuration/operations/overload_manager/overload_manager)
- Manual or specification: [Google SRE: handling overload](https://sre.google/sre-book/handling-overload/)
- Maintainer or personal blog: [Marc Brooker's blog](https://brooker.co.za/blog/)
- Technical blog: [AWS Builders' Library: load shedding](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/)
- Hands-on guide: [Kubernetes HPA walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
