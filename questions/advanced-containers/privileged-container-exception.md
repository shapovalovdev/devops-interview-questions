---
title: Review a privileged-container exception
theme: advanced-containers
difficulty: senior
type: scenario
tags: [containers, security, capabilities, process-isolation, governance]
sources:
  - url: https://docs.docker.com/engine/security/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Review a privileged-container exception

What controls are needed when a team claims a production container must be privileged?

## Answer guide

- First verify that a specific capability, device mapping, namespace option, or host service cannot meet the requirement. Privileged mode substantially broadens access and should be a documented exception, not a convenience setting.
- Limit placement, identity, image provenance, network exposure, runtime API access, duration, and auditability. Require threat modeling, ownership, rollback, and periodic review with a plan to remove the exception.
- A privileged workload can turn an application compromise into a node compromise. Treat it as a platform boundary decision with compensating controls rather than a normal application configuration.

## References

- [Docker Docs: security](https://docs.docker.com/engine/security/)
- Further reading (blog): [Docker: container security best practices](https://www.docker.com/blog/10-docker-security-best-practices/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
