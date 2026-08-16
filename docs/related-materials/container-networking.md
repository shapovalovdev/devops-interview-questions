# Container networking: related materials

Use these materials to understand the data path before changing a CNI, route, policy, attachment, or published port. Start with the CNI contract, then trace a workload’s interfaces, routes, name resolution, and policy enforcement.

## What to learn next

- Official documentation: [Kubernetes: Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf: networking and eBPF writing](https://thomasgraf.net/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Multus CNI quickstart](https://github.com/k8snetworkplumbingwg/multus-cni/blob/master/docs/quickstart.md)

## Suggested study order

Start inside one container's namespace and finish at platform governance,
because choosing a dataplane presumes knowing what it replaces.

1. [Explain a container network namespace](../../questions/container-networking/container-network-namespace.html)
    — The namespace is the vantage point you must inspect from before any driver
    or cluster layer makes sense.
2. [Explain Docker network drivers](../../questions/container-networking/network-driver-basics.html)
    — Bridge, overlay, and host drivers are the first thing the namespace
    connects to.
3. [Use a user-defined bridge for service discovery](../../questions/container-networking/user-defined-bridge-dns.html)
    — The user-defined bridge brings DNS-based service discovery to plain Docker
    networking.
4. [Design network aliases for service lifecycle](../../questions/container-networking/network-alias-lifecycle.html)
    — Aliases make that discovery survive service lifecycle events rather than
    depend on coincidences.
5. [Distinguish EXPOSE from port publishing](../../questions/container-networking/expose-versus-publish.html)
    — EXPOSE documents while publishing forwards, and confusing the two breaks
    the model early.
6. [Debug container DNS resolution](../../questions/container-networking/container-dns-resolution.html)
    — Container DNS failures recur later in Kubernetes with harder symptoms, so
    they are debugged here first.
7. [Debug failed container egress](../../questions/container-networking/container-egress-debugging.html)
    — Failed egress is the other pre-cluster failure the Theme insists you meet
    early.
8. [Trace Kubernetes Service traffic](../../questions/container-networking/kubernetes-service-traffic-path.html)
    — A name that resolves with zero usable backends is the canonical tenant
    complaint, so Service traffic is traced early.
9. [Diagnose an MTU mismatch across container paths](../../questions/container-networking/mtu-mismatch-troubleshooting.html)
    — MTU symptoms only become legible after the Service traces the Theme has
    just taught.
10. [Validate Kubernetes NetworkPolicy enforcement](../../questions/container-networking/network-policy-enforcement-limits.html)
    — Default deny only exists if the installed plugin enforces it, so
    capability is verified before policy is trusted.
11. [Segment a multi-tier application with Docker networks](../../questions/container-networking/multi-network-segmentation.html)
    — Multi-tier segmentation applies the verified policy to a real application
    topology.
12. [Define ingress and gateway boundaries](../../questions/container-networking/ingress-gateway-boundary.html)
    — The gateway is about who owns the front door, a question that only opens
    after what-may-talk is settled.
13. [Explain Cilium's eBPF datapath trade-offs](../../questions/container-networking/cilium-ebpf-datapath-tradeoffs.html)
    — The Cilium family opens with its dataplane, the replacement everything
    else in the family presumes.
14. [Evaluate Cilium kube-proxy replacement](../../questions/container-networking/cilium-kube-proxy-replacement.html)
    — Replacing kube-proxy is the concrete trade the dataplane question frames.
15. [Apply Cilium identity-aware L7 network policy](../../questions/container-networking/cilium-l7-network-policy.html)
    — Identity-aware L7 policy is what the eBPF dataplane uniquely buys.
16. [Design controlled egress with Cilium Egress Gateway](../../questions/container-networking/cilium-egress-gateway-design.html)
    — Egress Gateway extends the identity model to outbound traffic.
17. [Advertise Kubernetes routes with Cilium BGP Control Plane](../../questions/container-networking/cilium-bgp-external-routing.html)
    — BGP advertisement connects the cluster to the network that surrounds it.
18. [Prepare clusters for Cilium Cluster Mesh](../../questions/container-networking/cilium-clustermesh-prerequisites.html)
    — Cluster Mesh presumes the dataplane and routing decisions made above it.
19. [Configure and troubleshoot a multi-interface Pod with Multus](../../questions/container-networking/multus-multi-interface-pod-troubleshooting.html)
    — Multus adds per-Pod interfaces, the multi-network edge case after the
    Cilium core.
20. [Establish container network observability standards](../../questions/container-networking/network-observability-standard.html)
    — Observability standards open the platform tier every tool family above
    must serve.
21. [Enable IPv6 container networking safely](../../questions/container-networking/ipv6-container-networking.html)
    — IPv6 enablement is a platform programme the standards tier makes safe to
    attempt.
22. [Define a multi-cluster connectivity strategy](../../questions/container-networking/multi-cluster-connectivity-strategy.html)
    — The multi-cluster strategy spends the single-cluster story across
    boundaries.
23. [Govern workload egress on a container platform](../../questions/container-networking/platform-egress-governance.html)
    — Egress governance turns connectivity into policy with named owners.
24. [Govern high-risk container network changes](../../questions/container-networking/network-change-governance.html)
    — High-risk change control keeps the platform's own network mutations
    survivable.
25. [Design container network security architecture](../../questions/container-networking/container-network-security-architecture.html)
    — The security architecture closes the Theme by composing policy, identity,
    and boundaries into one design.
