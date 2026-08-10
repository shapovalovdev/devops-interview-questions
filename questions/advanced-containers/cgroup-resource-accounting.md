---
title: Explain cgroup resource accounting for containers
theme: advanced-containers
difficulty: middle
type: theory
tags: [containers, linux, cgroups, resource-limits, performance]
sources:
  - url: https://man7.org/linux/man-pages/man7/cgroups.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain cgroup resource accounting for containers

How do cgroups account for a container's resource use, and why does that matter in production?

## Answer guide

- Cgroups group processes in a hierarchy and expose controllers for resources such as CPU, memory, I/O, and PIDs. The runtime places container processes in a cgroup so the host can measure and constrain them together.
- Accounting must be read with workload context: CPU throttling, memory pressure, I/O delay, and process limits can each look like application slowness. Observe both cgroup metrics and host saturation.
- Limits are not capacity planning. Incorrect hierarchy, unbounded sidecars, or aggregate tenant demand can still exhaust node resources and cause noisy-neighbor or eviction incidents.

## References

- [Linux man-pages: cgroups](https://man7.org/linux/man-pages/man7/cgroups.7.html)
- Further reading (blog): [Docker: resource constraints](https://www.docker.com/blog/how-to-keep-your-containers-under-control-with-resource-constraints/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
