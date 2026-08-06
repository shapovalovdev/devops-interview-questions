---
title: Investigate a container cgroup memory limit and OOM kill
theme: advanced-containers
difficulty: middle
type: troubleshooting
tags: [containers, linux, cgroups, memory, resource-limits, troubleshooting]
sources:
  - url: https://docs.docker.com/engine/containers/resource_constraints/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a container cgroup memory limit and OOM kill

How do you distinguish a container hitting its memory limit from a node-wide memory failure?

## Answer guide

- Compare the container cgroup limit and current usage with kernel and runtime OOM evidence, exit status, and node memory pressure. A cgroup limit can terminate one workload without the whole host exhausting RAM.
- Profile resident memory, allocator behavior, cache, and concurrency before changing limits. Set an explicit limit with headroom for expected peaks and test the failure behavior.
- Increasing a limit without reserving capacity can turn an isolated failure into node pressure. Disabling limits masks leaks and lets one workload displace unrelated services.

## References

- [Docker Docs: memory constraints](https://docs.docker.com/engine/containers/resource_constraints/)
- Further reading (blog): [Docker: resource constraints](https://www.docker.com/blog/how-to-keep-your-containers-under-control-with-resource-constraints/)
