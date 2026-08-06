---
title: Choose runtime isolation tiers for a multi-tenant platform
theme: advanced-containers
difficulty: staff
type: scenario
tags: [containers, security, process-isolation, governance, platform-engineering]
sources:
  - url: https://docs.docker.com/engine/security/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Choose runtime isolation tiers for a multi-tenant platform

How should a platform team select container isolation tiers for tenants with different risk profiles?

## Answer guide

- Classify workloads by trust, data sensitivity, required privileges, and escape impact. Offer a constrained default tier and stronger isolation or dedicated nodes for exceptional high-risk workloads, with clear ownership and cost rules.
- Combine runtime controls with identity, network segmentation, image provenance, node patching, monitoring, and an auditable exception process. Publish the supported interfaces so teams do not rely on privileged workarounds.
- Containers share a kernel, so they may not satisfy every adversarial-tenant model. Overpromising isolation creates security debt; an expensive maximum-isolation default can prevent adoption and drive unmanaged shadow platforms.

## References

- [Docker Docs: security](https://docs.docker.com/engine/security/)
- Further reading (blog): [Docker: container security best practices](https://www.docker.com/blog/10-docker-security-best-practices/)
