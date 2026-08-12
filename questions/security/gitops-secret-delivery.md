---
title: Deliver secrets to a GitOps-reconciled cluster
theme: security
difficulty: senior
type: scenario
tags: [security, kubernetes, ci-cd, git, least-privilege, governance, gitops, cgoa]
sources:
  - url: https://fluxcd.io/flux/guides/mozilla-sops/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://kubernetes.io/docs/concepts/configuration/secret/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://external-secrets.io/latest/
    source_type: official-docs
    verified_on: 2026-08-12
---

# Deliver secrets to a GitOps-reconciled cluster

A team is moving to a reconciler that applies everything committed to a deployment repository. Database passwords and API tokens currently arrive as pipeline variables. How should those values reach the cluster now, and what does each approach cost?

## Answer guide

- Plaintext secret material must never enter the state store, because a commit is permanent and a reconciler makes the store the deployment interface. Two designs are acceptable: commit ciphertext that only an in-cluster key can open, or commit a *reference* and let a controller fetch the value from an external secret manager at reconcile time. Which one fits depends on whether the organisation already runs a secret manager the clusters can reach.
- Encryption in place works because the value is sealed before it is committed. With SOPS the manifest keeps its structure and only the values are encrypted, so a reviewer still sees which keys changed and by whom; the reconciler holds the decryption key inside the cluster and decrypts as part of applying. Reference-based delivery works differently: the committed object names a store and a remote key, and the operator materialises a Kubernetes Secret from the manager's current value. Note that a Kubernetes Secret is base64-encoded, not encrypted, so encryption at rest for etcd and tight RBAC still apply under either design.
- The costs are not symmetric. Encrypted-in-store makes rotation a commit that re-encrypts every affected file, and old ciphertext stays in history forever, so a key compromise is retroactive across the whole repository. Reference-based delivery removes ciphertext from the store but adds a hard runtime dependency: the manager's availability, its rate limits, and a workload identity per cluster now sit on the reconcile path, and an unavailable manager blocks reconciliation of otherwise healthy workloads.
- Anticipate these failures. Decrypting inside the pipeline and pushing the result defeats the whole design. Giving the controller broad read access across the secret manager turns one component into a cluster-wide credential oracle, so scope its identity to the paths that cluster needs. Values can escape through reconciler diffs, Kubernetes events, and notification payloads, so check what the tooling renders on error. And a value rotated in the manager does not reach a running pod until something re-reads it, so plan for the window where the Secret is new and the process is still holding the old credential.

## References

- [Flux: manage Kubernetes secrets with SOPS](https://fluxcd.io/flux/guides/mozilla-sops/)
- [Kubernetes: Secrets concept and encryption caveats](https://kubernetes.io/docs/concepts/configuration/secret/)
- [External Secrets Operator documentation](https://external-secrets.io/latest/)
- Further reading (blog): [GitGuardian — how to handle secrets in Kubernetes](https://blog.gitguardian.com/how-to-handle-secrets-in-kubernetes/)

## What to learn next

- Official documentation: [Flux SOPS guide](https://fluxcd.io/flux/guides/mozilla-sops/)
- Manual or specification: [Kubernetes Secret concept reference](https://kubernetes.io/docs/concepts/configuration/secret/)
- Maintainer or personal blog: [Flux maintainers' blog](https://fluxcd.io/blog/)
- Technical blog: [GitGuardian — handling secrets in Kubernetes](https://blog.gitguardian.com/how-to-handle-secrets-in-kubernetes/)
- Hands-on guide: [External Secrets Operator getting started](https://external-secrets.io/latest/introduction/getting-started/)
