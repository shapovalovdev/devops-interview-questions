---
title: Pass artifacts safely between Argo Workflow steps
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, kubernetes, argo, argo-workflows, capa, storage]
sources:
  - url: https://argo-workflows.readthedocs.io/en/latest/walk-through/artifacts/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Pass artifacts safely between Argo Workflow steps

How would you make a build output available to a later Argo Workflow step without baking it into the next image?

## Answer guide

- Define an output artifact for the producing template and an input artifact for the consuming template, backed by a configured artifact repository such as object storage. The controller stages declared artifacts rather than relying on two Pods sharing a local filesystem.
- Use immutable, run-scoped artifact names or keys, validate checksums or signatures where integrity matters, and give the Workflow identity only the storage permissions it needs.
- Set retention and lifecycle rules. Large artifacts, retries, and failed runs can raise storage cost or expose stale sensitive data; do not use artifacts as an unbounded database or to pass secrets.

## References

- [Argo Workflows: artifacts](https://argo-workflows.readthedocs.io/en/latest/walk-through/artifacts/)
- Further reading (blog): [GitHub Blog: Secure your supply chain with artifact attestations](https://github.blog/security/supply-chain-security/secure-your-software-supply-chain-and-build-faster-with-github-actions/)

## What to learn next

- Official documentation: [Argo Workflows artifact repository configuration](https://argo-workflows.readthedocs.io/en/latest/configure-artifact-repository/)
- Manual or specification: [OCI distribution specification](https://github.com/opencontainers/distribution-spec/blob/main/spec.md)
- Maintainer or personal blog: [Martin Fowler — deployment pipeline](https://martinfowler.com/bliki/DeploymentPipeline.html)
- Technical blog: [CNCF — cloud native project blog](https://www.cncf.io/blog/)
- Hands-on guide: [Argo Workflows quick start](https://argo-workflows.readthedocs.io/en/latest/quick-start/)
