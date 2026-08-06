# Kubernetes and Cloud Native Security Associate (KCSA) coverage

This study map aligns original practice Questions to the current [KCSA
curriculum](https://training.linuxfoundation.org/certification/kubernetes-and-cloud-native-security-associate-kcsa/).
It is a learning index, not a reproduction of real, confidential, or leaked
exam content. The curriculum was reviewed on 2026-08-06; check the official
page before studying because domains and product behavior can change.

Mapped Questions carry the `kcsa` tag and remain in their canonical Theme
folder. Each has an original prompt, full answer guide, structured
primary-source metadata, and separately labeled complementary reading.

| Official domain | Weight | Representative canonical practice Questions |
| --- | ---: | --- |
| Cloud Native Security | 14% | [Linux capabilities](../../questions/linux/linux-capabilities-least-privilege.md), [container image provenance](../../questions/security/container-image-provenance.md), [container runtime hardening](../../questions/security/container-runtime-hardening.md) |
| Kubernetes Cluster Component Security | 22% | [control-plane triage](../../questions/kubernetes/control-plane-incident-triage.md), [Service discovery](../../questions/kubernetes/service-discovery-basics.md), [persistent-volume lifecycle](../../questions/kubernetes/persistent-volume-claim-lifecycle.md) |
| Kubernetes Security Fundamentals | 22% | [RBAC least privilege](../../questions/kubernetes/rbac-least-privilege.md), [NetworkPolicy enforcement](../../questions/kubernetes/network-policy-enforcement.md), [secret rotation](../../questions/kubernetes/secrets-access-and-rotation.md) |
| Kubernetes Threat Model | 16% | [production policy exceptions](../../questions/kubernetes/production-policy-exception-process.md), [network-policy limits](../../questions/container-networking/network-policy-enforcement-limits.md), [multi-tenant boundaries](../../questions/kubernetes/multi-tenant-platform-boundaries.md) |
| Platform Security | 16% | [admission guardrails](../../questions/kubernetes/admission-policy-and-guardrails.md), [gateway migration governance](../../questions/kubernetes/gateway-migration-governance.md), [platform SLO and capacity governance](../../questions/kubernetes/platform-slo-and-capacity-governance.md) |
| Compliance and Security Frameworks | 10% | [image supply-chain controls](../../questions/security/software-supply-chain-controls.md), [security incident triage](../../questions/security/security-incident-triage.md), [Kubernetes audit policy](../../questions/kubernetes/audit-policy-runtime-detection.md) |

This map deliberately reuses canonical Questions across related certification
paths. It does not claim that these prompts predict examination content or
guarantee an exam result.
