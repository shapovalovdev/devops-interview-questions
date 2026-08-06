---
title: Upgrade Istio with a bounded canary
theme: service-mesh
difficulty: senior
type: scenario
tags: [service-mesh, istio, kubernetes, ica, deployment, reliability]
sources:
  - url: https://istio.io/latest/docs/setup/upgrade/canary/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Upgrade Istio with a bounded canary

How would you upgrade an Istio mesh while limiting the blast radius of a control-plane or proxy incompatibility?

## Answer guide

- Read the target release notes and supported upgrade path, back up versioned installation configuration, and test the upgrade against representative workloads first. Install the new control-plane revision alongside the old one, rather than assuming an in-place replacement can be undone after all workloads have moved.
- Move selected namespaces or workloads to the new revision in small batches, restart them so they obtain proxies from that revision, and compare request success, latency, policy decisions, certificate behavior, telemetry, and proxy synchronization. Include gateways and externally exposed traffic in the plan because their compatibility and rollback impact differ from an internal workload.
- Define measurable promotion and rollback gates. Do not remove the prior revision until all enrolled workloads, gateways, and control-plane health checks are stable; incompatible proxy configuration, unsupported APIs, missing images, or a rushed restart can turn a control-plane upgrade into an application outage.

## References

- [Istio: Canary upgrade](https://istio.io/latest/docs/setup/upgrade/canary/)
- [Istio: Upgrade notes](https://istio.io/latest/docs/releases/)
- Further reading (blog): [Istio: Canary upgrades](https://istio.io/latest/blog/2021/revision-tag/)
