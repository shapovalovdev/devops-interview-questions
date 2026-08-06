---
title: Explain why containers log to standard streams
theme: logging
difficulty: junior
type: theory
tags: [logging, containers, kubernetes, observability]
sources:
  - url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain why containers log to standard streams

Why is stdout and stderr usually the preferred application logging target in a container?

## Answer guide

- Container runtimes capture a container's standard output and standard error, and Kubernetes exposes those records through its node logging path. Writing there lets a node-level agent collect application output without sharing an application-specific file path or adding a log daemon to every image.
- Emit one structured event per line and include application timestamps and severity. Standard streams are transport, not a durable database: their retention, rotation, and availability depend on the runtime and node configuration.
- Do not assume `kubectl logs` is a complete incident archive. A terminated pod, node loss, rotation policy, or collector outage can remove local data. Export central logs, monitor collector health, and use volumes only when a product explicitly needs local files.

## References

- [Kubernetes: logging architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
- Further reading (blog): [Grafana engineering blog](https://grafana.com/blog/)

## What to learn next

- Official documentation: [Kubernetes logging architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
- Manual or specification: [CRI logging proposal](https://github.com/kubernetes/design-proposals-archive/blob/main/node/kubelet-cri-logging.md)
- Maintainer or personal blog: [Kelsey Hightower's blog](https://kelsey.dev/)
- Technical blog: [Grafana engineering blog](https://grafana.com/blog/)
- Hands-on guide: [Loki Kubernetes installation](https://grafana.com/docs/loki/latest/setup/install/helm/)
