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
tenant submits to the cluster an operator runs.

1. [Explain cloud-native principles and open-source collaboration](../../questions/kubernetes/cloud-native-principles-and-community.html)
    — Cloud-native principles come first: what the platform promises and how its
    community governs change.
2. [Distinguish labels, selectors, and annotations](../../questions/kubernetes/labels-selectors-and-annotations.html)
    — Labels and selectors are the query contract every object below carries.
3. [Read the essential parts of a Pod specification](../../questions/kubernetes/pod-spec-basics.html)
    — The Pod specification is the object a tenant actually submits, so it opens
    the workload tier.
4. [Select Kubernetes readiness, liveness, and startup probes](../../questions/kubernetes/probe-selection.html)
    — Probes decide readiness and liveness inside the specification the Theme
    has just read.
5. [Explain Pod lifecycle and container restarts](../../questions/kubernetes/pod-lifecycle-and-restarts.html)
    — Lifecycle and restarts define what the cluster does with the probe's
    verdict.
6. [Set Pod resource requests and limits](../../questions/kubernetes/resource-requests-limits-and-qos.html)
    — Requests, limits, and QoS come before any rollout question because
    capacity decisions drive maxSurge and maxUnavailable.
7. [Explain a Kubernetes Deployment rollout and rollback](../../questions/kubernetes/deployment-rollout-and-rollback.html)
    — Rollout and rollback are the capacity decisions the requests tier just
    priced.
8. [Choose StatefulSet or Deployment](../../questions/kubernetes/statefulset-versus-deployment.html)
    — StatefulSet versus Deployment is the workload choice the rollout machinery
    serves.
9. [Deliver application configuration with ConfigMaps](../../questions/kubernetes/configmap-delivery.html)
    — ConfigMap delivery decouples configuration from the images the rollouts
    promote.
10. [Choose an init container or sidecar for an application Pod](../../questions/kubernetes/multi-container-pod-patterns.html)
    — Init containers versus sidecars compose the Pod the specification defined.
11. [Place Kubernetes workloads with affinity and taints](../../questions/kubernetes/scheduling-affinity-and-taints.html)
    — Affinity and taints place the workloads the objects above create.
12. [Explain Kubernetes Service discovery](../../questions/kubernetes/service-discovery-basics.html)
    — Service discovery makes the placed workload reachable by name.
13. [Expose an application with the right Service type](../../questions/kubernetes/service-types-and-endpoints.html)
    — The right Service type and its endpoints complete the reachability story.
14. [Debug a failing Kubernetes application with built-in CLI tools](../../questions/kubernetes/application-debugging-with-cli.html)
    — The debugging set lands mid-Theme on purpose, once every object it reads
    has been introduced.
15. [Debug CoreDNS and Kubernetes Service resolution](../../questions/kubernetes/coredns-service-debugging.html)
    — CoreDNS failures are the discovery tier breaking, read with the CLI tier
    above.
16. [Triage a Kubernetes node that becomes NotReady](../../questions/kubernetes/node-not-ready-triage.html)
    — The NotReady node moves debugging from objects to the machines that run
    them.
17. [Triage a Kubernetes control-plane availability incident](../../questions/kubernetes/control-plane-incident-triage.html)
    — The control-plane incident is the hardest debugging case the tier builds
    toward.
18. [Design least-privilege Kubernetes RBAC](../../questions/kubernetes/rbac-least-privilege.html)
    — Security opens with who may act, before the platform can enforce anything.
19. [Give a Kubernetes workload the least-privilege ServiceAccount](../../questions/kubernetes/service-account-workload-identity.html)
    — Workload identities are kept separate from humans, the RBAC tier applied
    to software.
20. [Establish Kubernetes admission policy guardrails](../../questions/kubernetes/admission-policy-and-guardrails.html)
    — Admission policy makes the platform's contract executable at the API
    boundary.
21. [Explain Kyverno policy-engine fundamentals](../../questions/kubernetes/kyverno-policy-engine-basics.html)
    — The Kyverno family opens with the policy engine's model.
22. [Design a maintainable Kyverno policy set](../../questions/kubernetes/kyverno-policy-authoring-design.html)
    — Authoring a maintainable policy set is the engine's first real use.
23. [Test Kyverno policy changes with the CLI in CI](../../questions/kubernetes/kyverno-cli-policy-ci.html)
    — Testing policy in CI gives the set the delivery discipline the Theme
    teaches elsewhere.
24. [Install or upgrade Kyverno without blocking the cluster](../../questions/kubernetes/kyverno-installation-upgrade-safety.html)
    — Installing or upgrading Kyverno must never block the cluster it guards.
25. [Roll out Kyverno enforcement using policy reports](../../questions/kubernetes/kyverno-enforcement-and-policy-reports.html)
    — Rolling out enforcement through policy reports is warn-then-enforce made
    data.
26. [Design a production Kubernetes policy exception process](../../questions/kubernetes/production-policy-exception-process.html)
    — The exception process keeps the guardrails honest when a workload cannot
    meet them.
27. [Govern the Kyverno policy lifecycle and exceptions](../../questions/kubernetes/kyverno-policy-lifecycle-governance.html)
    — Lifecycle governance keeps the policy set alive long after the rollout
    succeeds.
28. [Design a Kubernetes audit policy for security detection](../../questions/kubernetes/audit-policy-runtime-detection.html)
    — Audit policy turns runtime behaviour into detectable evidence.
29. [Apply seccomp and AppArmor to a Kubernetes workload](../../questions/kubernetes/seccomp-apparmor-workload.html)
    — Seccomp and AppArmor harden the workload itself rather than its
    surroundings.
30. [Use RuntimeClass for higher-risk workload isolation](../../questions/kubernetes/runtimeclass-sandbox-isolation.html)
    — RuntimeClass buys higher-risk workloads a stronger sandbox on demand.
31. [Remediate a Kubernetes CIS benchmark finding](../../questions/kubernetes/cis-benchmark-remediation.html)
    — The CIS benchmark closes the security movement with its outer measurement.
32. [Design PersistentVolumeClaim lifecycle for a stateful workload](../../questions/kubernetes/persistent-volume-claim-lifecycle.html)
    — Storage opens with the claim lifecycle every stateful workload rides.
33. [Configure HorizontalPodAutoscaler behavior](../../questions/kubernetes/hpa-behavior-and-metrics.html)
    — The autoscaler scales the workloads the placement tier pinned down.
34. [Use PodDisruptionBudgets for voluntary disruptions](../../questions/kubernetes/pod-disruption-budget-design.html)
    — Disruption budgets bound the voluntary disruptions autoscaling and
    upgrades cause.
35. [Configure TLS for Kubernetes Ingress safely](../../questions/kubernetes/ingress-tls-security.html)
    — Ingress TLS secures the traffic the Service tier exposed.
36. [Govern a migration from Ingress to Gateway API](../../questions/kubernetes/gateway-migration-governance.html)
    — The Gateway API migration is an ownership change, governed rather than
    renamed.
37. [Design a highly available kubeadm control plane](../../questions/kubernetes/ha-control-plane-design.html)
    — The operator tier opens by making the control plane itself highly
    available.
38. [Build and maintain a kubeadm-managed cluster](../../questions/kubernetes/kubeadm-cluster-lifecycle.html)
    — The kubeadm lifecycle keeps the HA design reproducible from day one.
39. [Plan a production Kubernetes cluster upgrade](../../questions/kubernetes/cluster-upgrade-strategy.html)
    — The production upgrade spends the version-skew rules and drain capacity
    the tiers above built.
40. [Migrate an application away from a deprecated Kubernetes API](../../questions/kubernetes/api-deprecation-migration.html)
    — Deprecated API migrations are the upgrade's application-facing half.
41. [Explain the roles of Cilium agents, operator, and Envoy](../../questions/kubernetes/cilium-component-roles.html)
    — The Cilium questions open with what each component actually does.
42. [Validate a new Cilium installation before production traffic](../../questions/kubernetes/cilium-install-connectivity-validation.html)
    — A new Cilium installation is validated before it carries production
    traffic.
43. [Choose a Cilium IPAM mode for a Kubernetes cluster](../../questions/kubernetes/cilium-ipam-mode-selection.html)
    — IPAM mode decides where pod addresses come from.
44. [Choose a Cilium policy-enforcement mode](../../questions/kubernetes/cilium-policy-enforcement-modes.html)
    — Enforcement mode selection sets what policy can honestly promise.
45. [Lead Kubernetes disaster recovery and restore exercises](../../questions/kubernetes/disaster-recovery-and-restore-exercise.html)
    — Disaster-recovery exercises rehearse the control-plane tiers' worst day.
46. [Set Kubernetes platform SLO and capacity governance](../../questions/kubernetes/platform-slo-and-capacity-governance.html)
    — Platform SLOs and capacity governance publish what the operator tier
    promises.
47. [Define multi-tenant Kubernetes platform boundaries](../../questions/kubernetes/multi-tenant-platform-boundaries.html)
    — The multi-tenant boundaries decision is last and hardest because every
    earlier chapter feeds it.
