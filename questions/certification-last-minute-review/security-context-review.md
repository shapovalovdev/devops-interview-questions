---
title: Review a Pod security context for least privilege
theme: certification-last-minute-review
difficulty: senior
type: scenario
tags: [kubernetes, security, containers, least-privilege, cks, kcsa]
sources:
  - url: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Review a Pod security context for least privilege

Which security-context choices should be questioned before admitting a workload?

## Answer guide

- Prefer a non-root user, drop unnecessary Linux capabilities, set `allowPrivilegeEscalation: false`, and use a read-only root filesystem where the application supports it. These are defense-in-depth controls, not substitutes for trusted images and runtime isolation.
- Treat `privileged`, host namespaces, hostPath mounts, added capabilities, and broad device access as explicit exceptions. Each can weaken workload isolation or expose host resources, so document the need and narrow scope.
- Verify compatibility with the actual image and platform, then enforce a baseline through admission policy and review. Test the workload under the restricted settings; silently relaxing controls after startup failure defeats the purpose of the review.

## References

- [Kubernetes: configure a security context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [Kubernetes: Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- Further reading (blog): [Rory McCune — Kubernetes security contexts](https://rorymccune.com/2020/03/11/kubernetes-security-contexts/)

## What to learn next

- Official documentation: [Security contexts](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- Manual or specification: [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- Maintainer or personal blog: [Rory McCune — security contexts](https://rorymccune.com/2020/03/11/kubernetes-security-contexts/)
- Technical blog: [Google Cloud — harden GKE workloads](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)
- Hands-on guide: [Kubernetes restrict a container's syscalls](https://kubernetes.io/docs/tutorials/security/seccomp/)
