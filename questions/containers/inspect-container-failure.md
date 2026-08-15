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
  - url: https://docs.podman.io/en/latest/markdown/podman-logs.1.html
    source_type: official-docs
    verified_on: 2026-08-16
---

# Investigate a container that exits immediately

A newly started container stops in seconds. What evidence do you collect before changing the image or command?

## Answer guide

- Confirm that the configured main process was meant to stay running; a batch command that exits successfully is not a daemon failure. Read its exit code and `docker logs` output first.
- Inspect the effective command, entrypoint, environment, mounts, user, health configuration, and state rather than assuming the Dockerfile defaults are still in force.
- Separate application failure from runtime setup failure: missing configuration, an unreadable mount, port conflict, unsupported architecture, or permission error can each terminate the process.
- Do not keep a failed process alive with a shell loop merely to make the container appear healthy. Fix the contract or use an intentional debug override while preserving evidence.
- The first commands have direct equivalents — `podman logs`, `podman inspect`, and the exit status from `podman ps -a` — so read-before-rebuild is a portable discipline rather than a Docker CLI habit.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker CLI reference: docker container logs](https://docs.docker.com/reference/cli/docker/container/logs/)
- [Further reading: Docker CLI reference: docker container inspect](https://docs.docker.com/reference/cli/docker/container/inspect/)
- [Podman docs: podman-logs](https://docs.podman.io/en/latest/markdown/podman-logs.1.html)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
