---
title: Publish an SBOM with a container image
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, docker, images, supply-chain, security]
sources:
  - url: https://docs.docker.com/build/metadata/attestations/sbom/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Publish an SBOM with a container image

How should an image SBOM be used in a release process?

## Answer guide

- Generate an SBOM during the controlled build and associate it with the immutable image digest so consumers can identify components in the exact artifact they deploy.
- Use it as inventory for vulnerability response and license analysis, then define who triages findings and how false positives, reachability, and compensating controls are recorded.
- An SBOM may be incomplete for dynamically downloaded plugins, operating-system packages, or opaque binaries. Validate generator scope and do not promise perfect vulnerability detection.
- Keep provenance and SBOM retention aligned with image retention. Deleting evidence while keeping a production image weakens incident response and auditability.

## References

- [Docker Docs: SBOM attestations](https://docs.docker.com/build/metadata/attestations/sbom/)
- Further reading (blog): [Docker: Container security and why it matters](https://www.docker.com/blog/container-security-and-why-it-matters/)
