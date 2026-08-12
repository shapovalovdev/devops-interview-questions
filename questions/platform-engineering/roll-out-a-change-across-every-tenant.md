---
title: Roll out a change across every tenant
theme: platform-engineering
difficulty: senior
type: scenario
tags: [platform-engineering, blast-radius, change-management, multi-tenancy]
sources:
  - url: https://openfeature.dev/docs/reference/intro/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Roll out a change across every tenant

You need to change the platform's default sidecar injection for every workload in the company. How do you ship it?

## Answer guide

- Treat a platform default as the highest-blast-radius change in the organization and ship it behind a decoupling mechanism so that deploying the code and enabling the behaviour are two separate acts. A flag system — OpenFeature gives a vendor-neutral API and evaluation-context model for this — lets you deploy the new injection logic everywhere while it evaluates to "off", then enable it for a targeting rule that names one namespace, then a cohort, then the fleet, with an instant kill switch that does not require a redeploy of the platform.
- Sequence by tenant cohort, not by percentage of pods, because a platform change lands per workload and the interesting failures are workload-specific. Order the cohorts as: the platform team's own services, volunteers who agreed to be first, a representative mix (one latency-sensitive service, one batch job, one stateful set, one very large deployment), then the rest by increasing criticality. Between cohorts, wait long enough to cover a full traffic cycle including the nightly and weekly peaks, and hold explicit stop conditions — the affected services' own SLOs, not the platform's.
- Constraints specific to a default change: existing workloads must not silently pick it up at an arbitrary time. A change that applies on the next pod restart means the fleet converges over days in an order determined by unrelated deploys, so pin the old behaviour explicitly for existing workloads and opt them in deliberately, or force the convergence on a schedule you control. Communicate before, during and after with the actual owner of each affected workload, and make sure the flag's evaluation context is something durable like the namespace or catalog entity, not a value that changes when the pod restarts.
- Failure modes: a flag whose default in the code differs from the default in the flag service, so a flag-service outage flips the fleet; enabling for a "small" cohort that happens to include the identity service everything else depends on; rolling forward because rollback was never tested against workloads that already restarted under the new behaviour; resource footprint changing enough that the fleet no longer fits its nodes at full enablement, which only shows up in the last cohort; and no per-tenant telemetry, so you can see the platform is healthy but not that one tenant's latency doubled.

## References

- [OpenFeature specification and reference](https://openfeature.dev/docs/reference/intro/)
- Further reading (blog): [Netflix technology blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [OpenFeature specification and reference](https://openfeature.dev/docs/reference/intro/)
- Manual or specification: [OpenTelemetry versioning and stability](https://opentelemetry.io/docs/specs/otel/versioning-and-stability/)
- Maintainer or personal blog: [Charity Majors — charity.wtf](https://charity.wtf/)
- Technical blog: [Netflix technology blog](https://netflixtechblog.com/)
- Hands-on guide: [Kubernetes deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
