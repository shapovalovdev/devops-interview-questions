---
title: Verify recovery rather than trusting a green deployment
theme: troubleshooting
difficulty: junior
type: troubleshooting
tags: [troubleshooting, monitoring, reliability, deployment]
sources:
  - url: https://sre.google/sre-book/monitoring-distributed-systems/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Verify recovery rather than trusting a green deployment

## Answer guide

- Define recovery using externally visible success, not process liveness: check representative requests, availability, latency, correctness, queues, and downstream error rates over a meaningful observation window.
- Compare the recovered cohort with an unaffected control and watch for retry storms, cache warm-up, delayed jobs, or slowly filling resources. Deployment success only shows that the control plane accepted a change.
- Remove temporary mitigations deliberately and update the incident timeline with evidence. If the signal is ambiguous, keep the incident active and assign a bounded follow-up rather than declaring success because a dashboard briefly turned green.

## References

- [Google SRE Book — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Google SRE Book — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- Further reading (blog): [Cloudflare — July 2020 outage postmortem](https://blog.cloudflare.com/cloudflare-outage-on-july-17-2020/)

## What to learn next

- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [Prometheus query basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- Hands-on guide: [OpenTelemetry metrics](https://opentelemetry.io/docs/concepts/signals/metrics/)
- Maintainer or personal blog: [Charity Majors](https://charity.wtf/)
- Technical blog: [Cloudflare — July 2020 outage postmortem](https://blog.cloudflare.com/cloudflare-outage-on-july-17-2020/)
