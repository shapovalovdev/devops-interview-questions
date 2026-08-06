---
title: Investigate a container that exits immediately
theme: containers
difficulty: junior
type: troubleshooting
tags: [containers, docker, debugging, troubleshooting]
sources:
  - url: https://docs.docker.com/reference/cli/docker/container/logs/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a container that exits immediately

A newly started container stops in seconds. What evidence do you collect before changing the image or command?

## Answer guide

- Confirm that the configured main process was meant to stay running; a batch command that exits successfully is not a daemon failure. Read its exit code and `docker logs` output first.
- Inspect the effective command, entrypoint, environment, mounts, user, health configuration, and state rather than assuming the Dockerfile defaults are still in force.
- Separate application failure from runtime setup failure: missing configuration, an unreadable mount, port conflict, unsupported architecture, or permission error can each terminate the process.
- Do not keep a failed process alive with a shell loop merely to make the container appear healthy. Fix the contract or use an intentional debug override while preserving evidence.

## References

- [Docker CLI reference: docker container logs](https://docs.docker.com/reference/cli/docker/container/logs/)
- [Further reading: Docker CLI reference: docker container inspect](https://docs.docker.com/reference/cli/docker/container/inspect/)
