---
title: Evaluate Docker rootless mode for a build worker
theme: containers
difficulty: senior
type: scenario
tags: [containers, docker, rootless, security, least-privilege]
sources:
  - url: https://docs.docker.com/engine/security/rootless/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Evaluate Docker rootless mode for a build worker

When is Docker rootless mode useful, and what compatibility constraints must you assess before adopting it?

## Answer guide

- Rootless mode runs both the Docker daemon and containers without root privileges, reducing the impact of a daemon or container compromise on the host's root account.
- Assess required kernel/user-namespace support, storage driver behavior, networking and port requirements, and operational tooling before migration. Some capabilities and host integrations have limitations in rootless environments.
- Rootless mode complements rather than replaces image provenance, least privilege, patching, tenant separation, and workload-specific authorization.
- Pilot representative builds and runtime workloads. Falling back to privileged daemon access for a single incompatible job can defeat the intended risk reduction if it becomes the normal exception.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Rootless mode](https://docs.docker.com/engine/security/rootless/)
- [Further reading: Docker Docs on rootless limitations](https://docs.docker.com/engine/security/rootless/#known-limitations)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
