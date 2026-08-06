---
title: Deliver application configuration with ConfigMaps
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, configuration-management, deployment, reliability]
sources:
  - url: https://kubernetes.io/docs/concepts/configuration/configmap/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Deliver application configuration with ConfigMaps

How would you provide non-secret configuration to an application and roll out a safe change?

## Answer guide

- Store non-confidential configuration in a ConfigMap and consume it as environment variables, command arguments, or a mounted file according to the application's reload behavior.
- Environment-variable consumers do not see a ConfigMap update without Pod replacement; mounted updates are eventually propagated but an application may still need a reload.
- Version or checksum-reference configuration in the Pod template when a deterministic rollout is required, and validate configuration before promoting it.
- Do not put credentials in ConfigMaps, and avoid mounting mutable configuration with `subPath` when updates are expected because `subPath` mounts do not receive updates.

## References

- [Kubernetes: ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Kubernetes: Configure a Pod to use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
