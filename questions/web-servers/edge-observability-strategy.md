---
title: Establish an edge observability strategy
theme: web-servers
difficulty: staff
type: scenario
tags: [observability, metrics, logging, governance]
sources:
  - url: https://opentelemetry.io/docs/specs/otel/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish an edge observability strategy

What is the observability design for a web edge shared by hundreds of services?

## Answer guide

- Define common dimensions and cardinality rules for request rate, error class, latency, bytes, protocol, cache outcome, upstream outcome, TLS handshake and saturation. Propagate a safe request or trace identifier through proxy and application layers, and give service owners dashboards plus a central fleet view.
- Build SLOs around user-visible availability and latency, with explicit treatment for client cancellations and expected denials. Keep raw logs searchable for a bounded incident window, sample high-volume success traffic, protect sensitive fields, and test that a trace can cross every hop.
- Unlimited labels for URLs, IDs or headers make telemetry unaffordable and unreliable; over-aggregation hides a failing tenant or region. Counting every 4xx as platform failure creates false alerts. A vendor dashboard is not a data contract—retain ownership, retention and access decisions in the platform design.

## References

- [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/)
- Further reading (personal blog): [Charity Majors on observability](https://charity.wtf/)

## What to learn next

- Official documentation: [NGINX monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/)
- Manual or specification: [W3C Trace Context](https://www.w3.org/TR/trace-context/)
- Maintainer or personal blog: [Charity Majors' blog](https://charity.wtf/)
- Technical blog: [OpenTelemetry blog](https://opentelemetry.io/blog/)
- Hands-on guide: [OpenTelemetry documentation](https://opentelemetry.io/docs/)
