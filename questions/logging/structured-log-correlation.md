---
title: Design structured logs for request correlation
theme: logging
difficulty: middle
type: scenario
tags: [logging, observability, debugging, incident-response]
---

# Design structured logs for request correlation

Which fields should a service emit so an operator can follow one failed request across multiple components?

## Answer guide

- Emit a stable request or trace identifier and propagate it downstream.
- Include timestamp, severity, service identity, operation, and useful non-secret context.
- Use structured fields rather than parsing free-form messages; avoid credentials and personal data.
