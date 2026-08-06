---
title: Prepare clusters for Cilium Cluster Mesh
theme: container-networking
difficulty: senior
type: scenario
tags: [containers, kubernetes, networking, security, reliability, cca]
sources:
  - url: https://docs.cilium.io/en/stable/network/clustermesh/setup/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Prepare clusters for Cilium Cluster Mesh

What prerequisites must be proven before connecting two production clusters with Cilium Cluster Mesh?

## Answer guide

- Verify unique, non-overlapping Pod and node addressing, node-to-node reachability, firewall rules, compatible datapath settings, and a supported Cilium version on both clusters.
- For native routing, ensure routing CIDRs cover the Pod ranges and that cross-cluster pod traffic can traverse the underlying network.
- Establish the control-plane exposure and certificates, wait for mesh status, then run a multi-cluster connectivity test before enabling shared services.
- Cluster Mesh expands failure and blast-radius boundaries. Conflicting CIDRs, unreachable nodes, mismatched modes, or changing identity-scale settings on a live mesh can interrupt connectivity or policy enforcement; use a staged design with rollback.

## References

- [Set up Cilium Cluster Mesh](https://docs.cilium.io/en/stable/network/clustermesh/setup/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
