---
title: Define a production log-level policy
theme: logging
difficulty: junior
type: theory
tags: [logging, observability, debugging, operations]
sources:
  - url: https://opentelemetry.io/docs/specs/otel/logs/data-model/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define a production log-level policy

How should a team use log severity levels in a production service?

## Answer guide

- Define levels by operator action, not by how alarming a programmer feels: debug is normally disabled diagnostic detail, info records expected state changes, warn signals an unexpected but recovered condition, and error records a failed operation requiring investigation. Document examples so services do not use levels inconsistently.
- Keep the default production level high enough that normal traffic is affordable, then enable scoped diagnostic logging for a service, tenant, request, or short interval during investigation. A global debug switch can expose secrets and overwhelm collectors precisely when the system is stressed.
- Treat severity as queryable data. Preserve the original severity and a normalized level in the pipeline, alert on symptom metrics rather than raw error volume alone, and test the policy with a deliberate failure. Rate-limit repetitive errors and retain enough context for the first occurrence.

## References

- [OpenTelemetry log data model: severity fields](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- Further reading (personal blog): [Charity Majors on logs and events](https://charity.wtf/2019/02/05/logs-vs-structured-events/)

## What to learn next

- Official documentation: [OpenTelemetry log data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- Manual or specification: [RFC 5424 syslog severity](https://www.rfc-editor.org/rfc/rfc5424)
- Maintainer or personal blog: [Charity Majors' writing](https://charity.wtf/)
- Technical blog: [Google Cloud logging severity](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)
- Hands-on guide: [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)
