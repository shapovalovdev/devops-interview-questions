---
title: Deliver application configuration with ConfigMaps
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, configuration-management, deployment, reliability, cka, ckad, kcna, cba]
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

- Further reading (blog): [Complementary kubernetes practice article](https://kubernetes.io/blog/2024/12/09/kubernetes-v1-32-release/)
- [Kubernetes: ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Kubernetes: Configure a Pod to use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)

## What to learn next

- Official documentation: [Kubernetes concepts: ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- Manual or specification: [ConfigMap v1 API reference](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/config-map-v1/)
- Maintainer or personal blog: [Ahmet Alp Balkan — why mounted ConfigMap and Secret updates are delayed](https://ahmet.im/blog/kubernetes-secret-volumes-delay/)
- Technical blog: [CNCF — principles for designing and deploying scalable applications on Kubernetes](https://www.cncf.io/blog/2022/02/17/principles-for-designing-and-deploying-scalable-applications-on-kubernetes/)
- Hands-on guide: [Configure a Pod to use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
