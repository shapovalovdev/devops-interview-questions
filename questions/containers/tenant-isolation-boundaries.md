---
title: Define tenant isolation boundaries for a container platform
theme: containers
difficulty: staff
type: scenario
tags: [containers, docker, security, least-privilege, platform-engineering, governance]
sources:
  - url: https://docs.docker.com/engine/security/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define tenant isolation boundaries for a container platform

Multiple teams will run untrusted build and workload images. How do you decide whether containers alone provide sufficient isolation?

## Answer guide

- Start with a threat model: identify who controls images, what host, network, credentials, and data they can reach, and the consequence of a container escape or daemon compromise.
- Containers use multiple kernel isolation mechanisms but share a host kernel. For stronger tenant boundaries, combine workload policy with dedicated nodes, virtual machines, sandboxed runtimes, or separate accounts according to risk.
- Prohibit or tightly govern privileged containers, Docker socket access, broad host mounts, device access, and uncontrolled capabilities; these can bypass the intended boundary.
- Make the decision explicit and testable through admission policy, audit evidence, incident response ownership, and periodic reassessment. A single "containerized" label is not a security classification.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Docker security](https://docs.docker.com/engine/security/)
- [Further reading: Docker Docs on runtime privileges](https://docs.docker.com/engine/containers/run/#runtime-privilege-and-linux-capabilities)
