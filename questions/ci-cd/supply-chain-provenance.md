---
title: Verify supply-chain provenance before deployment
theme: ci-cd
difficulty: senior
type: scenario
tags: [ci-cd, supply-chain, security, deployment, cnpa]
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

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [SLSA: Build security levels](https://slsa.dev/spec/v1.0/levels)
- [Further reading: GitHub Docs—artifact attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations)

## What to learn next

- Official documentation: [Sigstore Cosign signing overview](https://docs.sigstore.dev/cosign/signing/overview/)
- Manual or specification: [SLSA v1.0 provenance specification](https://slsa.dev/spec/v1.0/provenance)
- Maintainer or personal blog: [Kelly Shortridge — security engineering blog](https://kellyshortridge.com/blog/posts/)
- Technical blog: [OpenSSF blog](https://openssf.org/blog/)
- Hands-on guide: [SLSA GitHub generator — build provenance in Actions](https://github.com/slsa-framework/slsa-github-generator)
