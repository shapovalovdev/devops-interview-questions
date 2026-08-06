---
title: Build an image supply-chain control plane
theme: containers
difficulty: staff
type: scenario
tags: [containers, docker, images, registries, security, supply-chain, governance]
sources:
  - url: https://docs.docker.com/build/metadata/attestations/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build an image supply-chain control plane

What controls would you design so production accepts only explainable container images without blocking urgent delivery indefinitely?

## Answer guide

- Establish a release identity that links an immutable image digest to source revision, builder identity, build inputs, test and scan evidence, and environment-specific approval policy.
- Generate and retain attestations or equivalent verifiable metadata at build time, then enforce a deployment policy that checks the digest and required evidence at promotion or admission.
- Define risk-based paths: normal releases meet the standard policy; emergency exceptions require a named approver, bounded scope, compensating monitoring, and a tracked expiry/remediation action.
- Measure bypasses, unsigned or unverified deployments, evidence freshness, and time-to-remediate. A control plane that is opaque or permanently blocks teams will be bypassed rather than trusted.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Build attestations](https://docs.docker.com/build/metadata/attestations/)
- [Further reading: SLSA provenance](https://slsa.dev/provenance/)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
