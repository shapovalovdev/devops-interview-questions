---
title: Promote container images by digest
theme: advanced-containers
difficulty: senior
type: scenario
tags: [containers, docker, images, registries, supply-chain]
sources:
  - url: https://docs.docker.com/dhi/core-concepts/digests/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Promote container images by digest

Why should a release promotion workflow use an image digest rather than rebuilding or copying a mutable tag?

## Answer guide

- A digest identifies immutable image content, whereas a tag is a mutable name. Promote the tested digest so staging and production refer to the same artifact.
- Store approvals, SBOMs, provenance, vulnerability decisions, and rollback records against the digest. A new tag assignment must not inherit approval intended for earlier content.
- Verify registry access controls and copy semantics, especially across registries. Confirm the destination digest and attached referrers rather than assuming all metadata followed the image.
- Rebuild only when inputs or policy changed. Rebuilding during promotion risks deploying a different artifact than the one tested.

## References

- [Docker Docs: Image digests](https://docs.docker.com/dhi/core-concepts/digests/)
- Further reading (blog): [Docker: Container security and why it matters](https://www.docker.com/blog/container-security-and-why-it-matters/)
