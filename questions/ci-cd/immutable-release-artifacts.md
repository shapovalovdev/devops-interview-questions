---
title: Why should CI publish immutable release artifacts?
theme: ci-cd
difficulty: middle
type: theory
tags: [ci-cd, delivery, supply-chain, security]
sources:
  - url: https://slsa.dev/spec/v1.0/levels
    source_type: standard
    verified_on: 2026-08-06
---

# Why should CI publish immutable release artifacts?

Why is rebuilding “the same version” at deployment time risky, and what traceability should a release artifact provide?

## Answer guide

- Build once, then promote the exact content-addressed artifact through environments; rebuilding can change dependencies, tools, timestamps, or inputs despite the same version label.
- Record the source revision, build invocation, artifact digest, test evidence, and provenance. A mutable tag is convenient for discovery but is not a release identity.
- This makes rollback and audit reproducible and lets a verifier bind an artifact to its declared build. Retention, registry access, and signing-key compromise remain operational risks to design for.

## References

- [SLSA: Build security levels and provenance](https://slsa.dev/spec/v1.0/levels)
- [Further reading: GitHub Docs—artifact attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations)
