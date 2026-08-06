---
title: Isolate tenants in a shared logging platform
theme: logging
difficulty: senior
type: scenario
tags: [logging, security, reliability, platform-engineering]
sources:
  - url: https://grafana.com/docs/loki/latest/operations/authentication/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Isolate tenants in a shared logging platform

How would you prevent one tenant from reading, exhausting, or corrupting another tenant's logs?

## Answer guide

- Carry a trusted tenant identity from authenticated ingress through collector, queue, storage, and query layers; do not accept a tenant label supplied by an untrusted application as the authorization boundary. Enforce query authorization and storage partitioning consistently at every API.
- Apply per-tenant limits for ingestion rate, burst, streams, query concurrency, result size, and retention. These are availability controls as well as cost controls: a noisy tenant can otherwise cause index pressure or expensive searches that affect every customer.
- Make administrative access explicit and auditable, encrypt traffic, and test isolation with adversarial requests. Watch for cross-tenant data in dashboards, saved queries, alerts, exports, caches, and error messages; a correct backend policy can be defeated by a shared UI default.

## References

- [Loki authentication and multi-tenancy](https://grafana.com/docs/loki/latest/operations/authentication/)
- Further reading (blog): [Grafana: multi-tenant Loki](https://grafana.com/blog/2021/01/20/how-to-run-grafana-loki-as-a-multi-tenant-log-aggregation-system/)

## What to learn next

- Official documentation: [Loki authentication](https://grafana.com/docs/loki/latest/operations/authentication/)
- Manual or specification: [OpenTelemetry security guidance](https://opentelemetry.io/docs/security/)
- Maintainer or personal blog: [Ed Welch's Grafana writing](https://grafana.com/blog/author/ed-welch/)
- Technical blog: [Grafana multi-tenant Loki](https://grafana.com/blog/2021/01/20/how-to-run-grafana-loki-as-a-multi-tenant-log-aggregation-system/)
- Hands-on guide: [Loki configuration](https://grafana.com/docs/loki/latest/configure/)
