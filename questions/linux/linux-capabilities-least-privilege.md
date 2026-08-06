---
title: Apply Linux capabilities instead of full root privilege
theme: linux
difficulty: senior
type: scenario
tags: [linux, security, least-privilege]
sources:
  - url: https://man7.org/linux/man-pages/man7/capabilities.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Apply Linux capabilities instead of full root privilege

How do Linux capabilities reduce privilege for a service, and what are their limits?

## Answer guide

- Capabilities divide historically root-only operations into named privileges. Grant only the capability required for the specific operation, such as binding low ports, rather than running an entire service with unrestricted UID 0 privileges.
- Evaluate all capability sets and execution context: permitted, effective, inheritable, bounding, ambient, file capabilities, user namespaces, and the service manager can affect the result. The exact viable configuration depends on kernel, application, and container/runtime behavior.
- Capabilities are not a complete sandbox. Combine them with a non-root identity, filesystem and network restrictions, seccomp/MAC policy where appropriate, and tests proving the service still works after privileges are removed.

## References

- [capabilities(7): Linux capability model](https://man7.org/linux/man-pages/man7/capabilities.7.html)
- Further reading: [systemd.exec: CapabilityBoundingSet](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html)
