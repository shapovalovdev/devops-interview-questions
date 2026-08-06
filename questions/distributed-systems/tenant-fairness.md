---
title: Protect tenant fairness in a shared distributed platform
theme: distributed-systems
difficulty: staff
type: scenario
tags: [capacity-planning, reliability, platform-engineering]
sources:
  - url: https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Protect tenant fairness in a shared distributed platform

How would you stop one tenant or workload class from consuming a shared service's capacity?

## Answer guide

- Identify the shared bottlenecks and assign isolation keys that reflect customer and workload boundaries. Enforce admission, concurrency, rate, storage, and cost budgets at the earliest controllable point, with a reserved path for critical control-plane work.
- Publish fair-use behavior, measure per-tenant queueing and latency, and make limits adjustable through reviewed policy. Partition noisy or high-risk workloads when statistical sharing cannot provide the required isolation.
- Average utilization conceals starvation. A global queue, retry storm, or unbounded batch tenant can exhaust a resource before per-tenant limits apply; punitive throttling without observability or appeal can also create hard-to-diagnose customer failures.

## References

- [AWS Builders' Library: fairness in multi-tenant systems](https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems/)
- Further reading (personal blog): [Marc Brooker: fairness](https://brooker.co.za/blog/2018/06/20/fairness.html)

## What to learn next

- Official documentation: [Kubernetes resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- Manual or specification: [Google SRE: load balancing](https://sre.google/sre-book/load-balancing-datacenter/)
- Maintainer or personal blog: [Marc Brooker's blog](https://brooker.co.za/blog/)
- Technical blog: [AWS Builders' Library: fairness](https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems/)
- Hands-on guide: [Kubernetes limit ranges](https://kubernetes.io/docs/concepts/policy/limit-range/)
