---
title: Design a useful container health check
theme: containers
difficulty: middle
type: scenario
tags: [containers, docker, healthchecks, reliability]
sources:
  - url: https://docs.docker.com/reference/dockerfile/#healthcheck
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Design a useful container health check

What should a Docker `HEALTHCHECK` test, and what should not depend on it?

## Answer guide

- A health check runs a command in the container and reports a health status in addition to process state. Test the minimal capability that makes the service useful, not merely whether PID 1 exists.
- Set interval, timeout, retries, and start period to match startup and expected transient behavior. A check must finish within its timeout and return the documented success or failure code.
- Keep it cheap, deterministic, and observable. A probe that calls expensive dependencies or creates traffic can worsen an outage and convert a dependency incident into mass restarts.
- Docker records health; it does not automatically make every deployment platform remove or restart an unhealthy service. Wire the result into the actual supervisor or orchestrator and distinguish readiness from liveness there.
- Where the verdict lives is platform-specific: Kubernetes ignores the image `HEALTHCHECK` and defines liveness, readiness, and startup probes in the Pod spec, while podman honors the image field and emits an event — write the check so either placement enforces it.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Dockerfile reference: HEALTHCHECK](https://docs.docker.com/reference/dockerfile/#healthcheck)
- [Further reading: Docker Docs on health status events](https://docs.docker.com/reference/cli/docker/system/events/)
- [Kubernetes: liveness, readiness, and startup probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
