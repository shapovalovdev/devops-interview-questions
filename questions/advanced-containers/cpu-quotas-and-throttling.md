---
title: Diagnose cgroup CPU throttling in a container
theme: advanced-containers
difficulty: middle
type: troubleshooting
tags: [containers, linux, cgroups, cpu, performance, troubleshooting]
sources:
  - url: https://docs.docker.com/engine/containers/resource_constraints/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Diagnose cgroup CPU throttling in a container

A service has low average node CPU use but high latency. How do CPU quotas change your investigation?

## Answer guide

- Inspect the container cgroup's configured quota or CPU weight and its throttling counters alongside request latency and runnable work. A quota can throttle a busy process even when the whole node has idle cores.
- Confirm the runtime and cgroup version semantics, then reproduce representative concurrency. Prefer a measured request or quota based on demand rather than disabling controls indiscriminately.
- Raising the quota may move contention to another tenant or exceed cluster capacity. Leaving a too-small quota can create bursty latency and misleading application-level timeout symptoms.

## References

- [Docker Docs: resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)
- Further reading (blog): [Docker: resource constraints](https://www.docker.com/blog/how-to-keep-your-containers-under-control-with-resource-constraints/)
