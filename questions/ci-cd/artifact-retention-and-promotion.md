---
title: Set artifact retention and promotion rules
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, delivery, supply-chain, reliability]
sources:
  - url: https://docs.github.com/en/actions/how-tos/store-and-share-data
    source_type: official-docs
    verified_on: 2026-08-06
---

# Set artifact retention and promotion rules

What should a team retain after a build, and which item should move between environments?

## Answer guide

- Retain the release artifact, digest, manifest, provenance, SBOM where used, test reports, and deployment record for a period aligned to rollback, audit, and incident needs.
- Promote the exact immutable release artifact, not a rebuilt artifact or a moving branch. Attach environment-specific configuration at deployment without changing the artifact.
- Balance retention cost and privacy against recovery needs; logs and test artifacts can contain sensitive data. Test restoration periodically because a retention policy cannot help after the data has expired.

## References

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [GitHub Docs: Storing and sharing data from a workflow](https://docs.github.com/en/actions/how-tos/store-and-share-data)
- [Further reading: SLSA—build security levels](https://slsa.dev/spec/v1.0/levels)

## What to learn next

- Official documentation: [GitHub Actions deployments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Charity Majors](https://charity.wtf/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [GitHub Actions deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments)
