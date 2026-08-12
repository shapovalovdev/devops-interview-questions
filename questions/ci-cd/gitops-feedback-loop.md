---
title: Close the feedback loop for a GitOps deployment
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, kubernetes, argo-cd, gitops, monitoring, deployment, observability, cgoa]
sources:
  - url: https://argo-cd.readthedocs.io/en/stable/operator-manual/health/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://argo-cd.readthedocs.io/en/stable/operator-manual/notifications/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://fluxcd.io/flux/monitoring/
    source_type: official-docs
    verified_on: 2026-08-12
---

# Close the feedback loop for a GitOps deployment

Developers merge a change and their pipeline reports success, but they have no idea whether the change reached production. What has to be in place before a merge can be treated as a delivered change?

## Answer guide

- A merged commit is a request, not a result. The loop closes only when the reconciler reports that the requested revision was applied *and* that the resulting workload is healthy, and when that verdict is routed back to the person who merged rather than sitting on a dashboard nobody opens. The pipeline's green build says the artifact exists; it says nothing about the cluster.
- Two distinct states carry the answer, and conflating them is the usual mistake. Sync status answers whether live state matches the tracked revision. Health status answers whether those resources are actually working, and it is assessed per resource kind — a Deployment is Progressing until its rollout completes, Degraded when it will not. Notification controllers subscribe to transitions between these states and emit to chat, a pull-request check, or a webhook, and both reconcilers export metrics for reconcile duration, failures, and outstanding drift so alerts can be built on trends rather than single events.
- Understand what the loop still does not tell you. Synced and Healthy means the objects exist and their controllers are satisfied; it is not evidence that users are served correctly, which needs service SLIs and, for progressive rollouts, analysis against real traffic metrics. Custom resources report an unknown health state until someone writes a health check for them, so a platform built on operators is partly blind by default. At scale, per-application alerting produces a notification storm during a mass sync or a cluster upgrade, so aggregate by application set or by failure class.
- The gaps that bite: alerting only on sync *failure* misses the silent case where automatic sync was disabled or the application was suspended, because nothing fails — it simply stops. A successful sync of a broken image reports Progressing rather than Degraded until the probe budget runs out, so the first notification is optimistic. Notifications that omit the revision and the destination force a responder to reconstruct what changed before they can revert it. And treating pipeline success as delivery reports the outcome before the reconciler has run at all.

## References

- [Argo CD: resource health assessment](https://argo-cd.readthedocs.io/en/stable/operator-manual/health/)
- [Argo CD: notifications and triggers](https://argo-cd.readthedocs.io/en/stable/operator-manual/notifications/)
- [Flux: monitoring and alerting](https://fluxcd.io/flux/monitoring/)
- Further reading (blog): [Codefresh — Argo CD learning guide](https://codefresh.io/learn/argo-cd/)

## What to learn next

- Official documentation: [Argo CD resource health](https://argo-cd.readthedocs.io/en/stable/operator-manual/health/)
- Manual or specification: [Argo CD metrics reference](https://argo-cd.readthedocs.io/en/stable/operator-manual/metrics/)
- Maintainer or personal blog: [Argo project maintainers' blog](https://blog.argoproj.io/)
- Technical blog: [Codefresh — Argo CD guide](https://codefresh.io/learn/argo-cd/)
- Hands-on guide: [Flux: configure notifications](https://fluxcd.io/flux/guides/notifications/)
