---
title: Verify supply-chain provenance before deployment
theme: ci-cd
difficulty: senior
type: scenario
tags: [ci-cd, supply-chain, security, deployment]
sources:
  - url: https://slsa.dev/spec/v1.0/levels
    source_type: standard
    verified_on: 2026-08-06
---

# Verify supply-chain provenance before deployment

Which evidence should a deployment policy verify before accepting a release artifact?

## Answer guide

- Verify the artifact digest, signature or attestation, trusted builder identity, source revision, and declared build inputs against an allowlist and the release policy.
- Store and evaluate provenance with the artifact so a mutable tag or detached report cannot be substituted later. Make verification fail closed for the risk class it protects.
- Provenance describes how an artifact was built; it does not itself prove source code safety or correct runtime configuration. Protect signing identities, define key/identity rotation, and retain evidence for incident response.

## References

- [SLSA: Build security levels](https://slsa.dev/spec/v1.0/levels)
- [Further reading: GitHub Docs—artifact attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations)
