# Container networking: related materials

Use these materials to understand the data path before changing a CNI, route, policy, attachment, or published port. Start with the CNI contract, then trace a workload’s interfaces, routes, name resolution, and policy enforcement.

## What to learn next

- Official documentation: [Kubernetes: Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf: networking and eBPF writing](https://thomasgraf.net/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Multus CNI quickstart](https://github.com/k8snetworkplumbingwg/multus-cni/blob/master/docs/quickstart.md)

## Suggested study order

Start inside one container: the network namespace as the vantage point you must
inspect from, then bridge drivers, the user-defined bridge, service-discovery
aliases, and the difference between EXPOSE and a published port. Debug
container DNS and failed egress before Kubernetes, because both failures recur
there with harder symptoms. In the cluster, trace Service traffic from selector
to ready endpoints early — a name that resolves with zero usable backends is
the canonical tenant complaint — then the MTU mismatch whose symptoms those
traces make legible. NetworkPolicy enforcement limits and multi-tier
segmentation follow, and only then the ingress and gateway boundary, since
policy is about what may talk and the gateway is about who owns the front door.
The Cilium family — the eBPF dataplane, kube-proxy replacement, identity-aware
L7 policy, Egress Gateway, BGP routes, Cluster Mesh, with Multus for
multi-interface Pods — sits near the end because choosing it presumes you know
what it replaces. Finish with the platform questions: observability standards,
IPv6 enablement, multi-cluster connectivity, egress governance, high-risk
change control, and network security architecture.
