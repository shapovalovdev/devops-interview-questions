---
title: Configure and troubleshoot a multi-interface Pod with Multus
theme: container-networking
difficulty: senior
type: troubleshooting
tags: [containers, kubernetes, networking, cni, multus, ipam, routing, troubleshooting, ckne]
sources:
  - url: https://raw.githubusercontent.com/k8snetworkplumbingwg/multus-cni/master/docs/how-to-use.md
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://raw.githubusercontent.com/k8snetworkplumbingwg/multus-cni/master/docs/configuration.md
    source_type: official-docs
    verified_on: 2026-08-06
---

## What to learn next

- Official documentation: [Multus CNI usage guide](https://github.com/k8snetworkplumbingwg/multus-cni/blob/master/docs/how-to-use.md)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Doug Smith and Tomofumi Hayashi: secondary networks with Multus](https://www.redhat.com/en/blog/how-to-use-kubernetes-services-on-secondary-networks-with-multus-cni)
- Technical blog: [Red Hat: Multus in container networking](https://www.redhat.com/en/blog/multus-takes-leading-role-container-networking)
- Hands-on guide: [Multus CNI quickstart](https://github.com/k8snetworkplumbingwg/multus-cni/blob/master/docs/quickstart.md)

# Configure and troubleshoot a multi-interface Pod with Multus

A workload needs the normal cluster network plus a secondary data network. How
would you configure and troubleshoot the Pod without accidentally sending its
control-plane traffic over the secondary interface?

## Answer guide

- Treat the cluster's primary CNI network as the normal `eth0` path and create a named `NetworkAttachmentDefinition` (NAD) for each deliberately owned secondary network. Reference the NAD with the Multus Pod annotation, including an explicit interface name when that makes automation and diagnosis unambiguous. The NAD owns the delegated CNI/IPAM configuration; the Pod owner should not silently embed an alternate network configuration that bypasses platform review.
- Decide routing before rollout. Multus normally leaves the primary network as the Pod default route; a `default-route` attachment option deliberately changes that and can break API, DNS, Service, node, or egress reachability that assumed `eth0`. Use policy routing or narrowly scoped routes where the data network needs selective destinations, and only make a secondary attachment default after proving all required control and management flows.
- Debug from the API down: check the Pod event and Multus/kubelet logs, resolve the NAD in the intended namespace, inspect the annotation and CNI configuration, then compare `ip addr`, `ip route`, rules, DNS, and packet captures inside the Pod with the host/CNI logs. Verify that IPAM allocated the expected address, gateway, routes, MTU, VLAN/macvlan prerequisites, and that the route lookup chooses the expected egress interface for both data and control destinations.
- Do not mutate attachments on a live production workload as a routine fix. An attachment or route change can require Pod recreation, change source addresses and connection state, exhaust or leak IPAM allocations, or redirect all traffic through an unobserved network. Stage a replacement Pod, test probes and application traffic, preserve a rollback path, and coordinate the NAD/platform-network owners; namespace-isolation settings can also reject an otherwise valid cross-namespace reference.

## References

- [Multus: attach networks and select a default route](https://github.com/k8snetworkplumbingwg/multus-cni/blob/master/docs/how-to-use.md)
- [Multus configuration and NetworkAttachmentDefinition namespace isolation](https://github.com/k8snetworkplumbingwg/multus-cni/blob/master/docs/configuration.md)
- [CNI specification](https://www.cni.dev/docs/spec/)
- Further reading (blog): [Doug Smith and Tomofumi Hayashi: secondary networks with Multus](https://www.redhat.com/en/blog/how-to-use-kubernetes-services-on-secondary-networks-with-multus-cni)
