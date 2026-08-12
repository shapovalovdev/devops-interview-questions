---
title: Choose a pull-based reconciler or a push-based deployment pipeline
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, kubernetes, git, argo-cd, deployment, architecture, least-privilege]
sources:
  - url: https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://fluxcd.io/flux/concepts/
    source_type: official-docs
    verified_on: 2026-08-12
---

# Choose a pull-based reconciler or a push-based deployment pipeline

A platform team runs thirty clusters and today deploys by having each CI job apply manifests with cluster credentials. They are asked to move to a reconciler. How should they decide between a pull model and their current push model, and where should the reconciler run?

## Answer guide

- Prefer the pull model here: an agent that runs with, or on behalf of, the target fetches the desired state itself and applies it, so the pipeline no longer needs thirty sets of cluster credentials and a merge stops being the last point at which anything checks the cluster. Keep push only for targets that cannot host or reach an agent, and for bootstrap of the agent itself.
- The agent is what makes the difference. Argo CD's application controller renders the tracked revision through the repo-server and compares it with live state on a periodic loop that a webhook can shorten; Flux's source-controller fetches the artifact and its kustomize- and helm-controllers apply it on their own interval. An event-driven trigger only reduces the latency of that loop — the agent still decides to apply, so it is still a pull.
- Placement is a separate decision from the model. A reconciler inside each cluster keeps blast radius per-cluster and needs no inbound credentials, at the cost of installing, upgrading, and monitoring thirty copies. A single external or hub reconciler managing all thirty is one thing to operate, but it must hold credentials for every cluster, which makes it both the highest-value target on the network and a single failure domain. At thirty clusters, sharding the hub or running in-cluster agents is usually the better trade.
- Watch for these failures: leaving the old CI apply enabled alongside the agent produces a permanent tug-of-war over the same objects; a hub outage stops reconciliation everywhere simultaneously, and nothing alerts because nothing is failing; relying on webhooks with a long fallback interval hides dropped deliveries until someone notices a stale revision; and pull does not reduce the value of the state store — merge access to it is now production access, so branch protection and review become security controls.

## References

- [Argo CD: architectural overview](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/)
- [Flux: core concepts](https://fluxcd.io/flux/concepts/)
- Further reading (blog): [Octopus Deploy — GitOps engineering guide](https://octopus.com/devops/gitops/)

## What to learn next

- Official documentation: [Argo CD architectural overview](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/)
- Manual or specification: [Flux GitOps Toolkit components](https://fluxcd.io/flux/components/)
- Maintainer or personal blog: [Flux maintainers' blog](https://fluxcd.io/blog/)
- Technical blog: [Google Cloud — an introduction to GitOps with Config Management](https://cloud.google.com/blog/topics/developers-practitioners/introduction-gitops-anthos-config-management)
- Hands-on guide: [Flux installation](https://fluxcd.io/flux/installation/)
