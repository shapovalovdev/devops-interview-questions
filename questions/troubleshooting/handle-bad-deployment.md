---
title: Contain a bad deployment while protecting evidence
theme: troubleshooting
difficulty: senior
type: troubleshooting
tags: [troubleshooting, deployment, recovery, incident-response, reliability]
sources:
  - url: https://sre.google/sre-book/release-engineering/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Contain a bad deployment while protecting evidence
## Answer guide
- Correlate the rollout cohort with user impact using version labels, traces, logs, and the deployment timeline. Confirm whether code, configuration, schema, feature flags, or traffic routing changed together.
- Halt expansion, drain or roll back only the affected cohort when compatibility allows, and verify recovery with user-facing signals. For irreversible migrations, use a documented forward fix or restore procedure rather than a blindly applied binary rollback.
- Preserve artifacts, immutable image identifiers, effective configuration, and decision timestamps. Improve progressive delivery gates after the incident; a successful rollback does not explain why predeployment checks missed the regression.
## References
- [Google SRE Book — Release Engineering](https://sre.google/sre-book/release-engineering/)
- [Google SRE Book — Managing Incidents](https://sre.google/sre-book/managing-incidents/)
- Further reading (blog): [Martin Fowler — Continuous Delivery](https://martinfowler.com/bliki/ContinuousDelivery.html)
## What to learn next
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [Argo Rollouts](https://argo-rollouts.readthedocs.io/)
- Hands-on guide: [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- Maintainer or personal blog: [Martin Fowler](https://martinfowler.com/)
- Technical blog: [Google Cloud blog](https://cloud.google.com/blog/)
