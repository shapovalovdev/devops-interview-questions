---
title: Design an incident evidence strategy
theme: observability
difficulty: staff
type: scenario
tags: [observability, incident-response, governance, security, prometheus, pca]
sources:
  - url: https://sre.google/workbook/incident-response/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design an incident evidence strategy

What observability standards let responders reconstruct a major incident without retaining every raw request forever?

## Answer guide

- Define the minimum evidence for critical journeys: user-impact SLIs, deploy/change history, bounded structured logs, sampled traces, dependency and infrastructure signals, and time-synchronized identity.
- Set retention tiers, access controls, redaction, audit trails, and legal holds according to data classification and incident-investigation needs.
- Exercise the design through incident simulations and postmortems: a responder should be able to answer what changed, who was affected, where the failure propagated, and which mitigation worked.
- Collecting all payloads is neither necessary nor safe. Missing change annotations, inconsistent clocks, and inaccessible telemetry can make a well-instrumented system effectively unverifiable.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Google SRE Workbook: Incident response](https://sre.google/workbook/incident-response/)
- [Further reading: OpenTelemetry security guidance](https://opentelemetry.io/docs/security/)
