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
---

# Design a useful container health check

What should a Docker `HEALTHCHECK` test, and what should not depend on it?

## Answer guide

- A health check runs a command in the container and reports a health status in addition to process state. Test the minimal capability that makes the service useful, not merely whether PID 1 exists.
- Set interval, timeout, retries, and start period to match startup and expected transient behavior. A check must finish within its timeout and return the documented success or failure code.
- Keep it cheap, deterministic, and observable. A probe that calls expensive dependencies or creates traffic can worsen an outage and convert a dependency incident into mass restarts.
- Docker records health; it does not automatically make every deployment platform remove or restart an unhealthy service. Wire the result into the actual supervisor or orchestrator and distinguish readiness from liveness there.

## References

- [Dockerfile reference: HEALTHCHECK](https://docs.docker.com/reference/dockerfile/#healthcheck)
- [Further reading: Docker Docs on health status events](https://docs.docker.com/reference/cli/docker/system/events/)
