---
title: Run a workload with a read-only root filesystem
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, filesystem, security, least-privilege, reliability]
sources:
  - url: https://docs.docker.com/engine/containers/run/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Run a workload with a read-only root filesystem

How do you make a container root filesystem read-only without breaking normal operation?

## Answer guide

- Enable a read-only root filesystem and enumerate legitimate write paths such as temporary files, runtime sockets, caches, and application state. Provide narrow tmpfs or managed volumes only where they are truly required.
- Make writes explicit in the deployment contract, set ownership for the runtime user, and test startup, log rotation, upgrades, and failure recovery with the same mounts.
- Read-only roots do not make mounted data read-only and can break software that writes configuration or certificates at startup. Broad writable host mounts undo much of the intended containment.

## References

- [Docker Docs: running containers](https://docs.docker.com/engine/containers/run/)
- Further reading (blog): [Docker: container security best practices](https://www.docker.com/blog/10-docker-security-best-practices/)
