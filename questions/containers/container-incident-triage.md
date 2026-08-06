---
title: Triage a container service restart storm
theme: containers
difficulty: senior
type: troubleshooting
tags: [containers, docker, debugging, monitoring, incident-response, reliability]
sources:
  - url: https://docs.docker.com/reference/cli/docker/container/inspect/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Triage a container service restart storm

A service repeatedly restarts after a release. Describe a safe triage sequence that limits customer impact and preserves evidence.

## Answer guide

- Stabilize first: stop further rollout, preserve the failing image digest and configuration, and roll back or reduce exposure using the established release procedure if customer impact warrants it.
- Compare the effective runtime state of a failing and healthy instance: exit code, logs, entrypoint, environment, mounts, user, resource events, health status, and dependency reachability.
- Correlate restart timing with deployment, secret/config changes, node conditions, and external dependency errors. A restart policy can make one root cause appear as many independent failures.
- Do not edit a live container as the fix. Turn the identified cause into a tested image/configuration change, then add a regression signal or pre-deploy check that would have caught it.

## References

- [Docker CLI reference: docker container inspect](https://docs.docker.com/reference/cli/docker/container/inspect/)
- [Further reading: Docker Docs on container logs](https://docs.docker.com/reference/cli/docker/container/logs/)
