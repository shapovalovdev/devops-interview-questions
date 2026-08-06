---
title: Design a Kubernetes audit policy for security detection
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, security, logging, observability, incident-response, cks, cnpe]
sources:
  - url: https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design a Kubernetes audit policy for security detection

How would you configure Kubernetes API audit logging to investigate privileged changes without collecting every request body or exhausting control-plane storage?

## Answer guide

- Start from concrete detection needs: authentication and authorization failures, RBAC and service-account changes, Secret access, privileged workload creation, and changes to admission or network controls. Use ordered audit-policy rules with an appropriate level, such as metadata for broad visibility and request data only for narrowly justified high-value operations.
- Configure the API-server audit backend through the supported cluster-management mechanism, protect the destination, set retention and access controls, and send events to a system where they can be correlated with workload and identity telemetry. Test a known event end-to-end and ensure responders can retrieve it during an incident.
- Exclude or reduce high-volume, low-value read paths only after measuring the effect, and document each suppression. Audit records describe requests to the API server; they do not automatically prove runtime behavior inside a container or capture activity that bypasses the Kubernetes API.
- Full request/response logging can expose Secrets and create serious cost, availability, and privacy risk. Conversely, weak rules or mutable local-only logs make investigations impossible, so change control and integrity monitoring are part of the design.

## References

- [Kubernetes: Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
- [Kubernetes: Audit policy configuration](https://kubernetes.io/docs/reference/config-api/apiserver-audit.v1/)
- Further reading (blog): [Kubernetes: Audit logging](https://kubernetes.io/blog/2017/05/kubernetes-audit/)
