---
title: Use the cgroup PIDs controller to contain fork storms
theme: advanced-containers
difficulty: middle
type: scenario
tags: [containers, linux, cgroups, pid-1, reliability, security]
sources:
  - url: https://man7.org/linux/man-pages/man7/cgroups.7.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use the cgroup PIDs controller to contain fork storms

How would you protect a multi-tenant node from one container creating excessive processes?

## Answer guide

- Set a cgroup PIDs limit for the workload and monitor its process count and limit failures. The PIDs controller constrains task creation in the cgroup rather than relying only on a host-wide user limit.
- Choose the value from known worker, helper, and burst requirements; test upgrade and error paths that temporarily create processes. Alert before the limit rather than discovering it through failed forks.
- Too small a value causes unexplained application failures; too large a value leaves a fork bomb able to consume host PID space and impair unrelated workloads or node management.

## References

- [Linux man-pages: cgroups](https://man7.org/linux/man-pages/man7/cgroups.7.html)
- Further reading (blog): [Docker: resource constraints](https://www.docker.com/blog/how-to-keep-your-containers-under-control-with-resource-constraints/)
