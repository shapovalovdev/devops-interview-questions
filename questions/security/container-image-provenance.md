---
title: Verify container image provenance before deployment
theme: security
difficulty: senior
type: scenario
tags: [containers, images, security, supply-chain]
sources:
  - url: https://slsa.dev/spec/v1.1/provenance
    source_type: standard
    verified_on: 2026-08-06
---

# Verify container image provenance before deployment

What evidence should a deployment policy require before allowing a container image into production?

## Answer guide

- Require an immutable digest from an approved registry; a mutable tag only names a possible image and must not be the release identity.
- Verify a signature and provenance attestation against trusted identities and policies. The evidence should bind the digest to the expected builder, source revision, and build inputs before deployment.
- Enforce the decision close to deployment, retain the verified digest and evidence in the release record, and define a break-glass path with audit and expiry.
- Provenance proves claims about a build, not that the code is safe. Compromised signing identities, permissive trust roots, or skipped admission checks defeat the control and require revocation and investigation.

## References

- [SLSA: Provenance](https://slsa.dev/spec/v1.1/provenance)
- [NIST SP 800-190: Application Container Security Guide](https://csrc.nist.gov/pubs/sp/800/190/final)
