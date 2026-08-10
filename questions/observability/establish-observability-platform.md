---
title: Establish an observability platform product
theme: observability
difficulty: staff
type: scenario
tags: [observability, platform-engineering, governance, reliability, prometheus, pca, cnpe, cnpa, otca]
sources:
  - url: https://opentelemetry.io/docs/what-is-opentelemetry/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish an observability platform product

How would you build a shared observability platform without forcing every team into identical service instrumentation?

## Answer guide

- Offer a paved path: supported SDKs, collectors, semantic conventions, dashboards, alert templates, access controls, and self-service onboarding with an explicit service contract.
- Standardize cross-cutting resource identity and correlation while allowing teams to add bounded domain attributes and service-specific SLIs.
- Govern platform reliability, cost allocation, privacy, data retention, and breaking schema changes as product concerns, with published ownership and adoption measures.
- A centrally imposed schema with no escape hatch blocks delivery; unlimited team customization makes correlation and cost control impossible. Version conventions and provide a migration path.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [OpenTelemetry: What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/)
- [Further reading: OpenTelemetry semantic conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/)

## What to learn next

- Official documentation: [What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/)
- Manual or specification: [Google SRE Book — free online edition](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Pete Hodgson — domain-oriented observability](https://martinfowler.com/articles/domain-oriented-observability.html)
- Technical blog: [CNCF Blog](https://www.cncf.io/blog/)
- Hands-on guide: [OpenTelemetry Demo application](https://opentelemetry.io/docs/demo/)
