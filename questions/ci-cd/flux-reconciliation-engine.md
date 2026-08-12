---
title: Explain how Flux reconciles a cluster from a source
theme: ci-cd
difficulty: middle
type: theory
tags: [ci-cd, kubernetes, git, flux, gitops, deployment, automation, cgoa]
sources:
  - url: https://fluxcd.io/flux/components/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://fluxcd.io/flux/concepts/
    source_type: official-docs
    verified_on: 2026-08-12
---

# Explain how Flux reconciles a cluster from a source

Walk through what Flux does between a commit landing in a tracked repository and the change being live, and say what an operator should check when the cluster is not moving.

## Answer guide

- Flux is not one process but a set of Kubernetes controllers, the GitOps Toolkit, each with its own custom resources. source-controller acquires and verifies artifacts from a `GitRepository`, `OCIRepository`, `Bucket`, or `HelmRepository`; kustomize-controller and helm-controller turn an acquired artifact into applied objects; notification-controller carries events and alerts in both directions. Because each controller owns a resource with its own interval, "Flux is stuck" is never a single answer.
- The path is: source-controller polls or is notified, fetches the revision, and publishes it as a local artifact recorded in the source's status. A `Kustomization` referencing that source then builds the overlay, applies it with server-side apply, and records an inventory of the objects it owns; if pruning is enabled, objects that disappear from the source and are still in the inventory get deleted. The important detail is that correction happens because the apply runs again every interval, not because a watcher noticed someone edited the cluster.
- The bounds matter operationally. The reconcile interval sets both how fast drift is corrected and how much API traffic the controllers generate, so shortening it is not free. Pruning depends on the inventory being continuous, so renaming or moving a `Kustomization` can orphan live objects or delete them, depending on how the change is made. Server-side apply field ownership decides who wins when an autoscaler or a mutating webhook also writes a field. Ordering between dependent resources comes from `dependsOn` and health checks, not from file order.
- Look for these when nothing is moving. A suspended `Kustomization` or source stops reconciling while its last status still reads as a success, which looks healthy at a glance. A build or fetch failure leaves the previous good revision applied, so the cluster is running fine and quietly out of date — the signal is the revision in status, not workload health. Signature and provenance verification is opt-in, so an unverified source is trusted by default unless configured otherwise. And two `Kustomization` objects that both claim the same manifest will contend for it on every interval, each reporting success.

## References

- [Flux: GitOps Toolkit components and controllers](https://fluxcd.io/flux/components/)
- [Flux: core concepts and reconciliation](https://fluxcd.io/flux/concepts/)
- Further reading (blog): [Flux maintainers' blog](https://fluxcd.io/blog/)

## What to learn next

- Official documentation: [Flux GitOps Toolkit components](https://fluxcd.io/flux/components/)
- Manual or specification: [Kubernetes controller pattern](https://kubernetes.io/docs/concepts/architecture/controller/)
- Maintainer or personal blog: [Flux maintainers' blog](https://fluxcd.io/blog/)
- Technical blog: [Red Hat — what a GitOps workflow looks like](https://www.redhat.com/en/topics/devops/what-is-gitops-workflow)
- Hands-on guide: [Flux: get started](https://fluxcd.io/flux/get-started/)
