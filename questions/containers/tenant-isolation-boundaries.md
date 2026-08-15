---
title: Define tenant isolation boundaries for a container platform
theme: containers
difficulty: staff
type: scenario
tags: [containers, docker, security, least-privilege, platform-engineering, governance, cnpa]
sources:
  - url: https://docs.docker.com/engine/security/
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://gvisor.dev/docs/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Define tenant isolation boundaries for a container platform

Multiple teams will run untrusted build and workload images. How do you decide whether containers alone provide sufficient isolation?

## Answer guide

- Start with a threat model: identify who controls images, what host, network, credentials, and data they can reach, and the consequence of a container escape or daemon compromise.
- Containers use multiple kernel isolation mechanisms but share a host kernel. For stronger tenant boundaries, combine workload policy with dedicated nodes, virtual machines, sandboxed runtimes, or separate accounts according to risk.
- Prohibit or tightly govern privileged containers, Docker socket access, broad host mounts, device access, and uncontrolled capabilities; these can bypass the intended boundary.
- Make the decision explicit and testable through admission policy, audit evidence, incident response ownership, and periodic reassessment. A single "containerized" label is not a security classification.
- The shared-kernel ceiling is spec-level: every OCI runtime applies the same namespace-and-cgroup isolation over one host kernel, so graduating tenants to gVisor's userspace kernel or Kata's micro-VMs is a category move any engine's tenants may need.

## References

- Further reading (blog): [Complementary containers practice article](https://www.docker.com/blog/container-security-and-why-it-matters/)
- [Docker Docs: Docker security](https://docs.docker.com/engine/security/)
- [Further reading: Docker Docs on runtime privileges](https://docs.docker.com/engine/containers/run/#runtime-privilege-and-linux-capabilities)
- [gVisor documentation](https://gvisor.dev/docs/)

## What to learn next

- Official documentation: [Docker Docs — what is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- Manual or specification: [OCI Image Format specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)
- Maintainer or personal blog: [Ivan Velichko — learning containers from the bottom up](https://iximiuz.com/en/posts/container-learning-path/)
- Technical blog: [Red Hat — what is a Linux container?](https://www.redhat.com/en/topics/containers/whats-a-linux-container)
- Hands-on guide: [Rootless Containers — free online book](https://rootless.vagmi.ca/)
