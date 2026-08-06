---
title: Design a stateless backend service
theme: backend-architecture
difficulty: junior
type: theory
tags: [availability, cloud, load]
sources:
  - url: https://12factor.net/processes
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a stateless backend service

What does stateless mean for a web backend, and why does it help operations?

## Answer guide

- A stateless process keeps durable session and business state outside the running instance, such as in a database, object store, or explicitly managed cache. Any healthy instance can serve a request when it receives the needed authenticated context.
- This enables replacement, horizontal scaling, and rolling deployment, but it requires explicit persistence boundaries, connection-pool limits, and a session strategy. Store only data that has defined durability and expiry characteristics.
- Stateless does not mean there is no state: in-memory caches, local files, and asynchronous work still exist. Treat them as disposable, avoid relying on load-balancer affinity for correctness, and test a request while its serving instance is terminated.

## References

- [The Twelve-Factor App: processes](https://12factor.net/processes)
- Further reading (blog): [Netflix: chaos engineering](https://netflixtechblog.com/chaos-engineering-upgraded-878d341f15b1)

## What to learn next

- Official documentation: [Kubernetes workload concepts](https://kubernetes.io/docs/concepts/workloads/)
- Manual or specification: [The Twelve-Factor App](https://12factor.net/)
- Maintainer or personal blog: [Charity Majors' blog](https://charity.wtf/)
- Technical blog: [Netflix TechBlog](https://netflixtechblog.com/)
- Hands-on guide: [Kubernetes deployment tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
