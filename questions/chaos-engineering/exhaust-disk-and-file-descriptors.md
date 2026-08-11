---
title: Exhaust disk space and file descriptors
theme: chaos-engineering
difficulty: middle
type: troubleshooting
tags: [chaos-engineering, fault-injection, disk, file-descriptors]
sources:
  - url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Exhaust disk space and file descriptors

Why are disk and descriptor exhaustion worth injecting, and how do you do it without wrecking the host?

## Answer guide

- These two faults are common in real incidents and rare in test suites, which is exactly why they are worth an experiment. Both produce errors on paths that are almost never exercised: a write that fails partway through, a log line that cannot be flushed, an accept call that returns EMFILE, a TLS handshake that fails because no descriptor is free. Applications frequently handle the happy path and the network path well and these two badly.
- Inject them at a bounded layer. Fill a dedicated volume rather than the root filesystem, or use the container's ephemeral-storage limit so the kubelet enforces the ceiling; on Kubernetes the node-pressure eviction thresholds for `nodefs` and `imagefs` decide whether the fault stays inside your pod or evicts neighbours. For descriptors, lower the process soft limit with setrlimit or systemd's LimitNOFILE rather than opening files until the whole node runs out.
- Watch for the second-order effects, which are the real finding: logging that blocks the request thread when the disk is full, metrics and traces silently dropped so the incident becomes invisible, a database that refuses writes but keeps accepting connections, health checks that pass because they never touch disk, and leaked descriptors that reveal a connection pool with no upper bound.
- Failure modes: filling the filesystem that holds the container runtime or etcd and taking down the node; leaving a large file behind after the run; a descriptor limit change that only applies to new processes so the experiment silently does nothing; and cleanup that cannot run because the tooling itself needs the resource you exhausted. Reserve the recovery step — a pre-allocated ballast file you can delete — before you start.

## References

- [Kubernetes — node-pressure eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/)
- Further reading (blog): [Slack Engineering](https://slack.engineering/)

## What to learn next

- Official documentation: [Kubernetes — node-pressure eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/)
- Manual or specification: [setrlimit(2) — resource limits](https://man7.org/linux/man-pages/man2/setrlimit.2.html)
- Maintainer or personal blog: [Lorin Hochstein — Surfing Complexity](https://surfingcomplexity.blog/)
- Technical blog: [Slack Engineering](https://slack.engineering/)
- Hands-on guide: [Chaos Mesh — simulate I/O chaos on Kubernetes](https://chaos-mesh.org/docs/simulate-io-chaos-on-kubernetes/)
