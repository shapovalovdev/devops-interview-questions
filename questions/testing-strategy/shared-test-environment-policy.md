---
title: Set shared test environment policy
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch14.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Set shared test environment policy

Twelve teams deploy to one staging cluster, someone's migration breaks it roughly weekly, and the debugging cost lands on whoever notices first. What policy makes a shared environment usable, and what should not be shared at all?

## Answer guide

- Give each team its own boundary inside the cluster before writing any rules. A Kubernetes namespace per team or per change, with a ResourceQuota and LimitRange so one workload cannot starve the others, NetworkPolicy so traffic does not cross unless declared, and RBAC scoped to the namespace, converts most of the weekly breakage from a shared-fate problem into a local one. Namespaces do not isolate cluster-scoped objects — CRDs, node-level resources, a shared ingress controller, admission webhooks — so name those explicitly as the surface that stays shared and gets change control.
- Databases and message brokers are where sharing actually hurts, and they need a different answer from compute. Prefer a schema or database per namespace over a shared instance; where that is impossible, require every migration to be backward-compatible and applied by an owned job, since an in-place destructive migration on a shared database is exactly the failure described and no namespace policy prevents it. Third-party sandboxes usually cannot be split at all, so treat them as a booked resource with a lock, not as something everyone shares silently.
- Write down the operating rules and make them enforceable. Ownership: every namespace has a named team in a catalog and an on-call route, so a broken deployment has an addressee. Lifetime: a TTL with automatic cleanup, because environments that live forever accumulate state nobody understands. Freshness: a scheduled reset to a known baseline, so drift has a bounded lifetime. Change announcement for the shared surface only, since requiring announcements for everything trains people to ignore them.
- Failure modes: staging drifting so far from production that a green run means nothing, usually through hand-applied fixes nobody put in the repository; a shared environment used as both an integration surface and a demo environment, where the demo's stability requirement quietly blocks everyone's testing; quotas set high enough to be decorative, so a load test still takes the cluster down; and the environment becoming the only place a certain test can run, which turns every outage into a delivery stoppage.

## References

- [Kubernetes — namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
- [Software Engineering at Google — larger testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Further reading (blog): [Google Testing Blog — hermetic servers](https://testing.googleblog.com/2012/10/hermetic-servers.html)

## What to learn next

- Official documentation: [Kubernetes — namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
- Manual or specification: [Software Engineering at Google — larger testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Maintainer or personal blog: [J. B. Rainsberger — beware the integrated tests scam](https://blog.thecodewhisperer.com/permalink/integrated-tests-are-a-scam)
- Technical blog: [Google Testing Blog — hermetic servers](https://testing.googleblog.com/2012/10/hermetic-servers.html)
- Hands-on guide: [Kubernetes — namespaces walkthrough](https://kubernetes.io/docs/tutorials/cluster-management/namespaces-walkthrough/)
