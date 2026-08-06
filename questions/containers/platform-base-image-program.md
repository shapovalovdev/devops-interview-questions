---
title: Design a governed base-image program
theme: containers
difficulty: staff
type: scenario
tags: [containers, docker, images, security, supply-chain, governance, platform-engineering]
sources:
  - url: https://docs.docker.com/build/building/best-practices/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a governed base-image program

How would you create a shared base-image program for many teams without turning it into an unmaintained central bottleneck?

## Answer guide

- Publish a small, versioned set of purpose-specific base images with documented support windows, owners, source repositories, digest references, SBOM/provenance expectations, and compatibility contracts.
- Automate rebuild, test, scan, and notification flows so upstream fixes reach downstream teams as actionable pull requests or release events rather than ad-hoc announcements.
- Provide an exception process with a named risk owner and expiry, while measuring adoption, stale consumers, update latency, and breakage. A mandatory image with no migration support invites unsafe forks.
- Keep the platform boundary narrow: the program supplies maintained foundations and policy evidence; application teams own their runtime dependencies, service behavior, and rollout safety.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Build image best practices](https://docs.docker.com/build/building/best-practices/)
- [Further reading: Docker Docs on image labels](https://docs.docker.com/reference/dockerfile/#label)
