---
title: Reduce Linux capabilities for a containerized service
theme: containers
difficulty: senior
type: scenario
tags: [containers, docker, security, least-privilege]
sources:
  - url: https://docs.docker.com/engine/containers/run/#runtime-privilege-and-linux-capabilities
    source_type: official-docs
    verified_on: 2026-08-06
---

# Reduce Linux capabilities for a containerized service

How would you reduce a service container's Linux privileges without breaking it?

## Answer guide

- Start with the service's concrete operations, then run it as a non-root user and drop unneeded Linux capabilities. Add back only a named capability justified by a tested requirement.
- Do not use `--privileged` as a troubleshooting shortcut: it grants broad device and capability access and collapses much of the container isolation model.
- Validate filesystem mounts, seccomp/AppArmor or equivalent policy, user namespaces, and network access alongside capabilities. Capability reduction alone cannot secure a writable host mount or exposed control socket.
- Test startup, steady state, upgrades, and failure paths under the restricted profile. A common failure is an init step or diagnostic command that silently assumes a capability the service should not retain.

## References

- [Docker Docs: Runtime privilege and Linux capabilities](https://docs.docker.com/engine/containers/run/#runtime-privilege-and-linux-capabilities)
- [Further reading: Docker Docs on seccomp profiles](https://docs.docker.com/engine/security/seccomp/)
