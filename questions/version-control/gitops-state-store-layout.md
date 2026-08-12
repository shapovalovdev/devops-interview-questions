---
title: Structure a Git state store for GitOps environments
theme: version-control
difficulty: middle
type: scenario
tags: [version-control, git, ci-cd, kubernetes, deployment, governance, gitops, cgoa]
sources:
  - url: https://fluxcd.io/flux/guides/repository-structure/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/
    source_type: official-docs
    verified_on: 2026-08-12
---

# Structure a Git state store for GitOps environments

A team keeps application code and deployment manifests in one repository and promotes to staging and production by editing files on a long-lived branch per environment. How should the state store be restructured, and what does each option cost?

## Answer guide

- Split the application source repository from the repository that holds the deployed manifests, and represent each environment as its own path with an explicitly pinned revision, so promoting is a reviewable commit that names exactly which artifact moves. The upstream guidance from both major reconcilers is the same: separate the two repositories and let the deployment repository be the desired-state record.
- The mechanics follow from what the agent tracks. A reconciler is pointed at a repository, a revision, and a path; shared bases hold everything common while a per-environment overlay or values file supplies only the differences. Promotion then means writing the digest that staging already runs into the production overlay, which leaves a diff a reviewer can read and a history that answers "what was running on Tuesday" without inspecting a cluster.
- Weigh the layouts honestly. Directory-per-environment keeps one history and one review process but needs path-scoped ownership rules and path filters, or every reconciler wakes for every unrelated change. Branch-per-environment makes promotion a merge, which sounds tidy but accumulates cherry-picks and permanent divergence between branches. A single large state store eventually costs clone and render time on every reconcile. Storing the desired state as an OCI artifact instead of a branch buys registry-grade immutability and signing but gives up the pull-request review that made the change legible.
- The failure modes are specific to a store, not to a cluster. Tracking a mutable branch or a movable tag means the deployed revision is not reproducible after the fact. Two applications pointed at overlapping paths fight over the same objects forever. A secret committed in the clear stays in history after it is deleted, so the store's retention is the secret's true lifetime. And keeping code and manifests together makes a CI job that commits an image tag re-trigger the very pipeline that wrote it.

## References

- [Flux: ways to structure your repositories](https://fluxcd.io/flux/guides/repository-structure/)
- [Argo CD: best practices for application repositories](https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/)
- Further reading (blog): [GitLab — GitOps best practices](https://about.gitlab.com/topics/gitops/gitops-best-practices/)

## What to learn next

- Official documentation: [Flux repository structure guidance](https://fluxcd.io/flux/guides/repository-structure/)
- Manual or specification: [Kustomize reference](https://kubectl.docs.kubernetes.io/references/kustomize/)
- Maintainer or personal blog: [Akuity — application dependencies with Argo CD](https://akuity.io/blog/application-dependencies-with-argo-cd)
- Technical blog: [GitLab — GitOps best practices](https://about.gitlab.com/topics/gitops/gitops-best-practices/)
- Hands-on guide: [Flux: OCI artifacts cheatsheet](https://fluxcd.io/flux/cheatsheets/oci-artifacts/)
