---
title: Govern runtime-isolation exceptions across an organization
theme: advanced-containers
difficulty: staff
type: scenario
tags: [containers, security, governance, capabilities, rootless, platform-engineering]
sources:
  - url: https://docs.docker.com/engine/security/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern runtime-isolation exceptions across an organization

What operating model keeps necessary runtime exceptions visible and temporary?

## Answer guide

- Require each exception to name the capability, mount, namespace, device, or profile change; record business owner, threat model, compensating controls, expiry, and removal plan. Make requests reviewable in normal delivery flow.
- Measure exception volume and recurrence, then turn common justified needs into safer platform features. Audit live runtime state against declared policy and involve security and reliability owners in high-impact decisions.
- Permanent undocumented exceptions accumulate privileged attack paths and make incidents harder to scope. A slow, opaque approval system causes teams to bypass controls, so publish service levels and supported alternatives.

## References

- [Docker Docs: security](https://docs.docker.com/engine/security/)
- Further reading (blog): [Docker: container security best practices](https://www.docker.com/blog/10-docker-security-best-practices/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
