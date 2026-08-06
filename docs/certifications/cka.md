# Certified Kubernetes Administrator (CKA) coverage

This is a map of original practice Questions to the current official [CKA curriculum](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/). It is not a source of real exam questions and does not reproduce confidential exam material. The official page stated Kubernetes v1.35 at review on 2026-08-06; check it before studying because curriculum and version alignment can change.

All mapped Questions carry the `cka` tag and remain in their canonical Theme folder. Each Question has source metadata, primary references, and separate complementary reading.

| Official domain | Canonical practice Questions |
| --- | --- |
| Cluster Architecture, Installation & Configuration (25%) | [RBAC](../../questions/kubernetes/rbac-least-privilege.md), [cluster upgrade](../../questions/kubernetes/cluster-upgrade-strategy.md), [kubeadm lifecycle](../../questions/kubernetes/kubeadm-cluster-lifecycle.md), [HA control plane](../../questions/kubernetes/ha-control-plane-design.md), [Helm/Kustomize](../../questions/kubernetes/helm-kustomize-component-installation.md), [CRD/operator lifecycle](../../questions/kubernetes/crd-operator-lifecycle.md) |
| Workloads & Scheduling (15%) | [Deployment rollout](../../questions/kubernetes/deployment-rollout-and-rollback.md), [ConfigMaps](../../questions/kubernetes/configmap-delivery.md), [HPA](../../questions/kubernetes/hpa-behavior-and-metrics.md), [probes](../../questions/kubernetes/probe-selection.md), [admission](../../questions/kubernetes/admission-policy-and-guardrails.md), [affinity and taints](../../questions/kubernetes/scheduling-affinity-and-taints.md) |
| Services & Networking (20%) | [Service discovery](../../questions/kubernetes/service-discovery-basics.md), [Service types and endpoints](../../questions/kubernetes/service-types-and-endpoints.md), [NetworkPolicy](../../questions/kubernetes/network-policy-enforcement.md), [Gateway migration](../../questions/kubernetes/gateway-migration-governance.md), [CoreDNS debugging](../../questions/kubernetes/coredns-service-debugging.md) |
| Storage (10%) | [PVC lifecycle](../../questions/kubernetes/persistent-volume-claim-lifecycle.md), [StatefulSet or Deployment](../../questions/kubernetes/statefulset-versus-deployment.md), [disaster recovery](../../questions/kubernetes/disaster-recovery-and-restore-exercise.md) |
| Troubleshooting (30%) | [control-plane triage](../../questions/kubernetes/control-plane-incident-triage.md), [node NotReady triage](../../questions/kubernetes/node-not-ready-triage.md), [Pod lifecycle](../../questions/kubernetes/pod-lifecycle-and-restarts.md), [resources and QoS](../../questions/kubernetes/resource-requests-limits-and-qos.md), [CoreDNS debugging](../../questions/kubernetes/coredns-service-debugging.md) |

The coverage map is a learning index, not a claim that studying it guarantees examination performance.
