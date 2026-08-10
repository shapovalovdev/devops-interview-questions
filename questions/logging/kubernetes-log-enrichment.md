---
title: Enrich Kubernetes logs without destroying provenance
theme: logging
difficulty: middle
type: scenario
tags: [logging, kubernetes, observability, debugging, otca]
sources:
  - url: https://opentelemetry.io/docs/specs/semconv/resource/k8s/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Enrich Kubernetes logs without destroying provenance

Which Kubernetes metadata belongs on collected logs, and what are the risks?

## Answer guide

- Add stable resource context such as cluster, namespace, workload, pod, container, node, and image version so an operator can filter by the actual execution environment. Keep application-supplied event fields separate from collector-added resource attributes to make provenance clear.
- Bound label and annotation enrichment. Copying arbitrary Kubernetes metadata creates high-cardinality indexes, leaks annotations intended for internal tooling, and makes a mutable pod label look like immutable event truth. Allowlist the keys needed for operations.
- Correlate lifecycle changes carefully: a pod name is not a durable deployment identity, containers restart, and records can arrive after deletion. Test enrichment during rolling updates and node failure, and expose collector errors when API access, RBAC, or metadata caching fails.

## References

- [OpenTelemetry Kubernetes resource semantic conventions](https://opentelemetry.io/docs/specs/semconv/resource/k8s/)
- Further reading (blog): [Grafana: Kubernetes labels in Loki](https://grafana.com/blog/2020/04/21/how-labels-in-loki-can-make-log-queries-faster-and-more-efficient/)

## What to learn next

- Official documentation: [Kubernetes logging architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
- Manual or specification: [OpenTelemetry Kubernetes resource conventions](https://opentelemetry.io/docs/specs/semconv/resource/k8s/)
- Maintainer or personal blog: [OpenTelemetry blog](https://opentelemetry.io/blog/)
- Technical blog: [Grafana Loki labels](https://grafana.com/blog/2020/04/21/how-labels-in-loki-can-make-log-queries-faster-and-more-efficient/)
- Hands-on guide: [OpenTelemetry Kubernetes attributes processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/k8sattributesprocessor)
