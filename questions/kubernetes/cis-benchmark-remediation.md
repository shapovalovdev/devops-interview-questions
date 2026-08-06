---
title: Remediate a Kubernetes CIS benchmark finding
theme: kubernetes
difficulty: senior
type: troubleshooting
tags: [kubernetes, security, cks, troubleshooting, governance]
sources:
  - url: https://kubernetes.io/docs/concepts/security/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Remediate a Kubernetes CIS benchmark finding

`kube-bench` reports that the API server permits anonymous authentication. How should you decide, apply, and verify the remediation without blindly changing cluster flags?

## Answer guide

- First identify the exact component, benchmark recommendation, Kubernetes version, and current managed-service or kubeadm ownership model. Read the API server manifest or provider configuration and establish whether any health, bootstrap, or external integration depends on anonymous access before changing it.
- Apply the documented control through the supported cluster-management path, test authentication and control-plane health, then make the change durable in the declarative cluster configuration. Record the benchmark version, exception owner, evidence, and reason for any control that cannot apply to that platform.
- Re-run the benchmark and verify the effective API-server configuration and relevant allowed and denied requests. A benchmark result is an indicator, not proof that the cluster is secure; it must be combined with RBAC, network controls, patching, and runtime monitoring.
- Avoid treating every finding as universally safe to remediate. Managed control planes may not expose flags, a stale benchmark can recommend obsolete settings, and direct edits to generated static-Pod manifests can be reverted or break cluster recovery.

## References

- [Kubernetes: Security overview](https://kubernetes.io/docs/concepts/security/)
- [Aqua Security kube-bench documentation](https://github.com/aquasecurity/kube-bench)
- Further reading (blog): [Kubernetes SIG Security: Kubernetes hardening guidance](https://kubernetes.io/blog/2021/04/06/pod-security-policy-deprecation-past-present-and-future/)
