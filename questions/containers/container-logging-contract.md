---
title: Define a container logging contract
theme: containers
difficulty: middle
type: scenario
tags: [containers, docker, logging, observability, reliability, ckad]
sources:
  - url: https://docs.docker.com/engine/logging/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define a container logging contract

How should an application emit logs in a containerized service, and what belongs to the platform?

## Answer guide

- Write event logs to standard output and standard error in a structured, documented format when the platform collects container streams. Include stable correlation fields without emitting secrets.
- Docker routes container output through a configured logging driver; choose retention, transport, and back-pressure behavior at the platform level rather than embedding host-specific log agents in every image by default.
- Treat logs as a bounded operational resource. High-cardinality, unbounded, or synchronous remote logging can increase cost, delay requests, or fill storage during an incident.
- Define how operators retrieve logs after restarts and what information is safe to record. Container logs alone do not replace metrics, traces, or application audit records.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Configure logging drivers](https://docs.docker.com/engine/logging/)
- [Further reading: Docker Docs on the local logging driver](https://docs.docker.com/engine/logging/drivers/local/)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
