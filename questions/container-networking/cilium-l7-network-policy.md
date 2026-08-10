---
title: Apply Cilium identity-aware L7 network policy
theme: container-networking
difficulty: senior
type: scenario
tags: [containers, kubernetes, networking, security, least-privilege, cca]
sources:
  - url: https://docs.cilium.io/en/stable/security/network/intro/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Apply Cilium identity-aware L7 network policy

How would you restrict a frontend so it can call only selected HTTP paths on a backend with Cilium?

## Answer guide

- Select workloads by stable labels and first establish the required L3/L4 flow; then add the Cilium policy's HTTP or RPC rule for the intended method, host, and path scope.
- Cilium uses identities derived from labels, so policy follows a workload when its IP changes; treat labels and namespaces as security-relevant inputs.
- Test both allowed and denied requests and inspect policy verdicts before enforcing a default-deny posture in a shared namespace.
- L7 enforcement uses proxy functionality and protocol-aware rules. TLS handling, DNS dependencies, policy ordering, and overly broad regexes can cause outages or weaken controls, so phase changes and retain a recovery path.

## References

- [Cilium network security introduction](https://docs.cilium.io/en/stable/security/network/intro/)
- Further reading (blog): [Cilium 1.15 overview](https://isovalent.com/blog/post/cilium-1-15/)
## What to learn next

- Official documentation: [Docker networking documentation](https://docs.docker.com/network/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf — networking articles](https://tgraf.io/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Docker standalone networking tutorial](https://docs.docker.com/engine/network/tutorials/standalone/)
