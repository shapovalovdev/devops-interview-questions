---
title: Apply seccomp and AppArmor to a Kubernetes workload
theme: kubernetes
difficulty: senior
type: scenario
tags: [kubernetes, security, linux, containers, least-privilege, cks]
sources:
  - url: https://kubernetes.io/docs/tutorials/security/seccomp/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Apply seccomp and AppArmor to a Kubernetes workload

How would you reduce a Pod's kernel attack surface with seccomp and AppArmor without turning an application rollout into an outage?

## Answer guide

- Begin with the workload's required behavior and apply a supported seccomp profile through its security context; Kubernetes supports `RuntimeDefault` as a portable baseline when the runtime provides it. Use an AppArmor profile only on nodes and Kubernetes versions where it is installed, loaded, and supported by the selected runtime.
- Stage enforcement in a representative environment, observe denied syscalls and file-access failures, and adjust the application or narrowly justified profile before production rollout. Pair it with non-root execution, dropped capabilities, read-only filesystems where feasible, and Pod Security Admission rather than assuming one control is sufficient.
- Verify the effective Pod specification, node profile state, and runtime events, then document profile ownership and regression tests. Keep the policy versioned with the workload and test upgrades because an image or runtime change can introduce a required syscall.
- Seccomp limits system calls and AppArmor mediates configured paths/capabilities; neither prevents all kernel exploits nor repairs a privileged Pod, host mount, or exposed container socket. A profile that is too permissive is theater; one that is too narrow can break startup or emergency diagnostics.

## References

- [Kubernetes: Restrict a container's syscalls with seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/)
- [Kubernetes: Restrict a container's access to resources with AppArmor](https://kubernetes.io/docs/tutorials/security/apparmor/)
- Further reading (blog): [Kubernetes: Seccomp default feature](https://kubernetes.io/blog/2021/08/25/seccomp-default/)

## What to learn next

- Official documentation: [Linux kernel security constraints for Pods and containers](https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/)
- Manual or specification: [seccomp(2) manual page](https://man7.org/linux/man-pages/man2/seccomp.2.html)
- Maintainer or personal blog: [Dave Altena — from Linux primitives to Kubernetes security contexts](https://learnkube.com/security-contexts)
- Technical blog: [Kubernetes blog — distributing seccomp, SELinux and AppArmor profiles as OCI artifacts](https://kubernetes.io/blog/2023/05/24/oci-security-profiles/)
- Hands-on guide: [Restrict a container's syscalls with seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/)
