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

- [Docker Docs: Rootless mode](https://docs.docker.com/engine/security/rootless/)
- [Further reading: Docker Docs on rootless limitations](https://docs.docker.com/engine/security/rootless/#known-limitations)
