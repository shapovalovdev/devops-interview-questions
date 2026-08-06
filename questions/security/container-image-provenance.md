---
title: Verify container image provenance before deployment
theme: security
difficulty: senior
type: scenario
tags: [containers, images, security, supply-chain]
---

# Verify container image provenance before deployment

What evidence should a deployment policy require before allowing a container image into production?

## Answer guide

- Require an immutable image digest from an approved registry.
- Verify signature or attestation linking the image to an authorized build and source revision.
- Enforce policy at admission time and retain a release audit trail.
