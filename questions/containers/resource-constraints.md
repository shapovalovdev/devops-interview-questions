---
title: Apply CPU and memory constraints to a container
theme: containers
difficulty: middle
type: scenario
tags: [containers, docker, cgroups, resource-limits, reliability]
sources:
  - url: https://docs.docker.com/engine/containers/resource_constraints/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Apply CPU and memory constraints to a container

How do CPU and memory limits affect a container, and how do you choose safe initial values?

## Answer guide

- Docker applies resource controls through the host kernel. A memory limit bounds available memory; exceeding it can lead to an out-of-memory termination. CPU controls limit or weight CPU access rather than promising instantaneous performance.
- Start from measured workload behavior and a service-level latency or throughput objective, then leave headroom for normal bursts and language-runtime behavior. Observe throttling, memory usage, and OOM events after rollout.
- Set both application-level concurrency/backpressure and platform limits. A limit alone cannot prevent a request queue, connection pool, or cache from creating failure pressure.
- Do not treat defaults as isolation. Overly low limits cause restart storms; no limits let one workload impair neighbors. Kernel, cgroup version, and orchestrator policy can affect the observable behavior.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Runtime resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)
- [Further reading: Docker Docs on OOM priority](https://docs.docker.com/engine/containers/resource_constraints/#understand-the-risks-of-running-out-of-memory)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
