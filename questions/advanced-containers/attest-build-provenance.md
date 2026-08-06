---
title: Attach and verify build provenance
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, docker, images, supply-chain, security, kcsa]
sources:
  - url: https://docs.docker.com/build/metadata/attestations/slsa-provenance/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Attach and verify build provenance

What should build provenance establish for a released container image?

## Answer guide

- Provenance links an image artifact to build inputs and a builder execution. Generate it in the controlled release pipeline and retain it alongside the image digest.
- Verify the subject digest, source revision, builder identity, and policy-relevant parameters before promotion. Tags are mutable pointers and are not a sufficient verification target.
- Decide which fields may be exposed: build arguments, environment details, and source locations can reveal information. Use a mode appropriate for your threat model.
- Provenance is evidence, not prevention. Protect CI credentials, require review for release configuration, and combine verification with signing and admission policy where applicable.

## References

- [Docker Docs: SLSA provenance attestations](https://docs.docker.com/build/metadata/attestations/slsa-provenance/)
- Further reading (blog): [Docker: Container security and why it matters](https://www.docker.com/blog/container-security-and-why-it-matters/)
