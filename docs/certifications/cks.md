# Certified Kubernetes Security Specialist (CKS) coverage

This map links original, source-verified practice Questions to the official [CKS curriculum](https://github.com/cncf/curriculum/tree/master/cks) and [Linux Foundation CKS program](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/). It is not a source of real exam questions and does not reproduce confidential exam content.

CKS is a performance-based certification and requires a passed CKA certification before the exam. The Linux Foundation program listed Kubernetes v1.35 at review on 2026-08-06; the open CNCF curriculum listed the six domains below. Check both before studying because weights, versions, and operational details can change.

All mapped Questions carry the `cks` tag and live in their canonical Theme folder. Every Question has structured primary-source metadata, a full answer guide, supporting primary references, and separately labeled complementary reading.

| Official domain | Weight | Canonical practice Questions |
| --- | ---: | --- |
| Cluster Setup | 10% | [NetworkPolicy](../../questions/kubernetes/network-policy-enforcement.md), [CIS benchmark remediation](../../questions/kubernetes/cis-benchmark-remediation.md), [TLS Ingress](../../questions/kubernetes/ingress-tls-security.md) |
| Cluster Hardening | 15% | [least-privilege RBAC](../../questions/kubernetes/rbac-least-privilege.md), [admission guardrails](../../questions/kubernetes/admission-policy-and-guardrails.md), [cluster upgrade](../../questions/kubernetes/cluster-upgrade-strategy.md) |
| System Hardening | 15% | [seccomp and AppArmor](../../questions/kubernetes/seccomp-apparmor-workload.md), [container runtime hardening](../../questions/security/container-runtime-hardening.md), [Linux capabilities](../../questions/containers/container-capabilities-security.md) |
| Minimize Microservice Vulnerabilities | 20% | [Pod Security Standards](../../questions/security/kubernetes-pod-security.md), [Secret access and rotation](../../questions/kubernetes/secrets-access-and-rotation.md), [RuntimeClass isolation](../../questions/kubernetes/runtimeclass-sandbox-isolation.md) |
| Supply Chain Security | 20% | [image provenance](../../questions/security/container-image-provenance.md), [dependency vulnerability management](../../questions/security/dependency-vulnerability-management.md), [software supply-chain controls](../../questions/security/software-supply-chain-controls.md), [base-image updates](../../questions/containers/base-image-update-policy.md) |
| Monitoring, Logging and Runtime Security | 20% | [Kubernetes audit policy](../../questions/kubernetes/audit-policy-runtime-detection.md), [security event logging](../../questions/security/security-logging-basics.md), [security incident triage](../../questions/security/security-incident-triage.md) |

The coverage map is a study index, not a claim that these Questions guarantee exam performance.
