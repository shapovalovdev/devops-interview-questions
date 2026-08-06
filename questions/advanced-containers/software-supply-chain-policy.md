---
title: Set container image supply-chain policy
theme: advanced-containers
difficulty: staff
type: scenario
tags: [containers, images, supply-chain, security, governance, platform-engineering]
sources:
  - url: https://slsa.dev/spec/v1.0/
    source_type: standard
    verified_on: 2026-08-06
---

# Set container image supply-chain policy

What policy should govern which container images may reach production?

## Answer guide

- Define an enforceable promotion contract: immutable digest, trusted registry, approved source and builder, provenance, SBOM, vulnerability decision, and named accountable owner.
- Apply rules proportionally by risk. A public internet-facing workload, a developer preview, and a patched emergency release need different review urgency, but all exceptions must be time-bound and auditable.
- Keep policy evaluation close to release and deployment so a mutable tag cannot bypass evidence gathered earlier. Provide clear feedback and remediation paths to teams.
- Track outcomes: blocked-release reasons, time to remediate critical findings, exception age, and unsupported base-image use. Policy that cannot be measured becomes either ignored or obstructive.

## References

- [SLSA specification v1.0](https://slsa.dev/spec/v1.0/)
- Further reading (blog): [Docker: Container security and why it matters](https://www.docker.com/blog/container-security-and-why-it-matters/)
