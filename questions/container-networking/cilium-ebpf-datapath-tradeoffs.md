---
title: Explain Cilium's eBPF datapath trade-offs
theme: container-networking
difficulty: middle
type: theory
tags: [containers, kubernetes, networking, performance, security, cca]
sources:
  - url: https://docs.cilium.io/en/stable/overview/intro/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain Cilium's eBPF datapath trade-offs

Why does Cilium use eBPF, and what must an operator validate before depending on eBPF-based features?

## Answer guide

- eBPF lets Cilium execute verified programs in the Linux kernel for networking, security, and observability decisions, which can reduce reliance on iptables rule processing and provide richer workload identity context.
- The design does not remove Kubernetes, Linux, or network prerequisites: compatibility depends on the Cilium release, kernel features, enabled datapath mode, and the environment's routing and security model.
- Validate feature status, agent health, policy and service behavior, and observability on representative nodes before enabling an advanced datapath capability fleet-wide.
- Kernel differences, resource pressure, unsupported combinations, and opaque troubleshooting assumptions are operational risks. Keep versioned configuration, collect Cilium diagnostics, and plan a reversible rollout rather than assuming eBPF is automatically faster or safer.

## References

- [Cilium and Hubble introduction](https://docs.cilium.io/en/stable/overview/intro/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)

## What to learn next

- Official documentation: [Cilium eBPF datapath](https://docs.cilium.io/en/stable/overview/intro/)
- Manual or specification: [Linux BPF documentation](https://docs.kernel.org/bpf/)
- Maintainer or personal blog: [Thomas Graf: networking writing](https://thomasgraf.net/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Cilium troubleshooting guide](https://docs.cilium.io/en/stable/operations/troubleshooting/)
