---
title: Design multi-tenant observability boundaries
theme: observability
difficulty: staff
type: scenario
tags: [observability, security, governance, platform-engineering, prometheus, pca]
sources:
  - url: https://opentelemetry.io/docs/security/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design multi-tenant observability boundaries

How would you give many teams observability access while preventing cross-tenant data exposure?

## Answer guide

- Establish tenant identity at collection and storage boundaries, then enforce authentication, authorization, query scoping, encryption, and audit logs in every telemetry backend.
- Separate shared platform signals from tenant data, define which resource attributes are trusted, and prevent clients from forging ownership labels that influence access decisions.
- Apply data classification, redaction, retention, and export controls consistently to logs, metrics, and traces; test isolation with representative queries and pipeline failures.
- Tenant labels alone are not authorization. Do not rely on dashboards to hide data while the raw query endpoint remains broad, and avoid putting secrets in attributes that cross trust boundaries.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [OpenTelemetry security](https://opentelemetry.io/docs/security/)
- [Further reading: OpenTelemetry context propagation security](https://opentelemetry.io/docs/concepts/context-propagation/)
