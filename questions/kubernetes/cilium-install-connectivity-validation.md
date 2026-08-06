---
title: Validate a new Cilium installation before production traffic
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, networking, deployment, troubleshooting, reliability, cca, ckne]
sources:
  - url: https://docs.cilium.io/en/stable/installation/k8s-install-helm/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Validate a new Cilium installation before production traffic

What checks would you run after installing Cilium on a new Kubernetes cluster?

## Answer guide

- Pin a supported Cilium release and review the installation values against the cluster's kernel, Kubernetes version, CNI ownership, IPAM, routing, and kube-proxy design.
- Check Cilium component readiness and status, then run the documented connectivity test to exercise expected service and policy paths.
- Add representative application tests for DNS, cross-node traffic, ingress, egress, NetworkPolicy, and any enabled features such as Gateway API or Hubble.
- A green DaemonSet alone does not prove a safe datapath. Failed connectivity tests, an incompatible existing CNI, or untested cloud routing can surface only under workload traffic, so stop promotion and preserve diagnostics before changing values.

## References

- [Install Cilium with Helm](https://docs.cilium.io/en/stable/installation/k8s-install-helm/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
