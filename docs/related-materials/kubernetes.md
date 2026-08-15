# Kubernetes related materials

These resources complement the Kubernetes Theme's Question-level references.
They are a curated starting point for workload and Pod behaviour, scheduling
and capacity, cluster networking and policy, cluster lifecycle and recovery,
and API extension; check every recommendation against the Kubernetes minor
version, container runtime, and CNI actually in use, because defaults and
feature gates change between releases.

## What to learn next

- Official documentation: [Kubernetes concepts](https://kubernetes.io/docs/concepts/)
- Manual or specification: [Kubernetes API reference](https://kubernetes.io/docs/reference/kubernetes-api/)
- Maintainer or personal blog: [Ahmet Alp Balkan — Kubernetes engineering notes](https://ahmet.im/blog/)
- Technical blog: [Kubernetes blog](https://kubernetes.io/blog/)
- Hands-on guide: [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/)

## Suggested study order

This Theme climbs the same route the platform path climbs: from the object a
tenant submits to the cluster an operator runs. Start with cloud-native
principles and the essential parts of a Pod specification — labels, selectors,
probes, security context — then Pod lifecycle and restarts. Set requests,
limits, and QoS before any rollout question, because maxSurge and
maxUnavailable are capacity decisions; Deployment rollout and rollback,
StatefulSet versus Deployment, ConfigMap and Secret delivery, init containers
versus sidecars, and affinity and taints follow. Service discovery and the
right Service type make the workload reachable; the debugging set — CLI triage,
CoreDNS resolution, the NotReady node, the control-plane incident — lands
mid-Theme on purpose, once every object it reads has been introduced. Security
and policy run as one movement: least-privilege RBAC and ServiceAccounts,
admission guardrails, the Kyverno family and its exception process, audit
policy, seccomp and AppArmor, RuntimeClass, and the CIS benchmark. Storage,
autoscaling, disruption budgets, Ingress TLS, and the Gateway API migration sit
between the workload and the operator tier, which is last and hardest: the
highly available kubeadm control plane, the production upgrade with deprecated
API migrations, the Cilium questions, disaster-recovery exercises, platform
SLOs and capacity governance, and the multi-tenant boundaries decision every
earlier chapter feeds.
