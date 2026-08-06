---
title: Design software supply-chain controls
theme: security
difficulty: senior
type: scenario
tags: [security, supply-chain, ci-cd, governance, kcsa]
sources:
  - url: https://slsa.dev/spec/v1.1/
    source_type: standard
    verified_on: 2026-08-06
---

# Design software supply-chain controls

What controls should a platform require from source change to production artifact?

## Answer guide

- Protect source review and branch policy, use isolated repeatable builds, inventory dependencies, and produce signed provenance that binds an immutable artifact to its build and source.
- Verify provenance and policy before promotion, protect signing identities, record the artifact digest in release evidence, and constrain who can change the pipeline.
- Start with the highest-value artifacts and measure adoption, bypasses, and failed verification. Make controls usable so teams do not create shadow release paths.
- A signed artifact can still contain vulnerable or malicious source. Compromise of a builder, repository, signer, or trust configuration changes the threat model and requires revocation, rebuild, and audit capability.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [SLSA specification](https://slsa.dev/spec/v1.1/)
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
