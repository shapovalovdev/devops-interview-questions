---
title: Apply Linux capabilities with least privilege
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, linux, capabilities, security, least-privilege]
sources:
  - url: https://man7.org/linux/man-pages/man7/capabilities.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Apply Linux capabilities with least privilege

A workload needs one privileged operation. How do capabilities reduce the risk compared with running fully privileged?

## Answer guide

- Linux capabilities split powers traditionally associated with root into independently controlled checks. Start with the runtime default set, drop unneeded capabilities, and add only the specific capability proved necessary.
- Validate effective, permitted, inheritable, and ambient sets inside the actual runtime configuration. User namespaces and security modules can further constrain what a capability means on the host.
- Capabilities are powerful and version-sensitive: adding broad capabilities such as SYS_ADMIN can create a substantial attack surface. A privileged container commonly bypasses multiple isolation controls and needs exceptional review.

## References

- [Linux man-pages: capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html)
- Further reading (blog): [Docker: runtime privilege and capabilities](https://www.docker.com/blog/understanding-the-docker-user-namespace-remapping/)
## What to learn next

- Official documentation: [OCI runtime specification](https://github.com/opencontainers/runtime-spec)
- Manual or specification: [Linux kernel cgroup v2 guide](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- Maintainer or personal blog: [Liz Rice — containers and Linux security](https://www.lizrice.com/)
- Technical blog: [Docker engineering blog](https://www.docker.com/blog/)
- Hands-on guide: [Docker Get Started guide](https://docs.docker.com/get-started/)
