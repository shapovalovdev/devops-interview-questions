---
title: Establish a change-provenance strategy for production
theme: version-control
difficulty: staff
type: scenario
tags: [git, version-control, supply-chain, security, governance, delivery]
sources:
  - url: https://slsa.dev/spec/v1.0/levels
    source_type: standard
    verified_on: 2026-08-06
  - url: https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish a change-provenance strategy for production

How would you connect a production artifact to the reviewed source change without claiming that Git history alone proves software safety?

## Answer guide

- Define the provenance chain: protected reviewed source commit, immutable release tag, isolated build identity, recorded build inputs, artifact digest, attestation, and deployment record. Make each link queryable during an incident or audit.
- Use CI to build from a checked-out commit rather than a mutable branch name, verify required policy gates, sign or attest artifacts with managed identities, and store evidence alongside immutable artifacts.
- Design key, identity, retention, exception, and verification workflows across repositories and environments. Rehearse lookup and revocation during a compromised dependency or emergency rollback.
- Git commits and signatures establish useful source context, but they do not prove a build used that commit, that dependencies were safe, or that a deployment used the tested artifact. Preserve those boundaries explicitly.

## References

- [SLSA: levels](https://slsa.dev/spec/v1.0/levels)
- [GitHub Docs: artifact attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations)
- Further reading (blog): [GitHub Security Blog](https://github.blog/security/)

## What to learn next

- Official documentation: [GitHub: artifact attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Dan Lorenc's blog](https://dlorenc.medium.com/)
- Technical blog: [GitHub Security Blog](https://github.blog/security/)
- Hands-on guide: [SLSA build track](https://slsa.dev/spec/v1.1/requirements)
