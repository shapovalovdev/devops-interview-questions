---
title: Design an Argo Events Sensor for a production trigger
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, kubernetes, argo, argo-events, capa, event-driven, security, cgoa]
sources:
  - url: https://argoproj.github.io/argo-events/sensors/trigger/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design an Argo Events Sensor for a production trigger

How would you trigger a deployment Workflow only after a signed release event and an approval event have both arrived?

## Answer guide

- Configure separate event dependencies, validate the release identity and payload, and use the Sensor dependency logic to require both conditions before invoking a trigger. Pass only the specific, validated parameters needed by the target Workflow.
- Give the Sensor service account minimal permissions to create the target object and isolate untrusted webhooks from privileged triggers. Keep approval evidence and event identifiers for auditability.
- Design for duplicate, out-of-order, and missing events. An idempotency key, expiry policy, and operator-visible failure path prevent an old or replayed event from starting an unintended deployment.

## References

- [Argo Events: Sensor triggers](https://argoproj.github.io/argo-events/sensors/trigger/)
- Further reading (blog): [AWS Compute Blog: event-driven architecture patterns](https://aws.amazon.com/blogs/compute/introducing-the-serverless-lens-for-the-aws-well-architected-framework/)

## What to learn next

- Official documentation: [Argo Events documentation](https://argoproj.github.io/argo-events/)
- Manual or specification: [Argo project documentation](https://argo-cd.readthedocs.io/en/stable/)
- Maintainer or personal blog: [Akuity — application dependencies with Argo CD](https://akuity.io/blog/application-dependencies-with-argo-cd)
- Technical blog: [Codefresh — trigger a pipeline from Argo CD](https://codefresh.io/blog/trigger-codefresh-pipeline-argocd/)
- Hands-on guide: [Argo Rollouts getting started](https://argo-rollouts.readthedocs.io/en/stable/getting-started/)
