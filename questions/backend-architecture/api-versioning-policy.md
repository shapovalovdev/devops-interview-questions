---
title: Govern API versioning and deprecation
theme: backend-architecture
difficulty: senior
type: scenario
tags: [http, change-management, dependencies]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc9110
    source_type: standard
    verified_on: 2026-08-06
---

# Govern API versioning and deprecation

How do you evolve a public backend API without surprising existing clients?

## Answer guide

- Prefer additive, backward-compatible changes and document the compatibility contract: fields, defaults, error behavior, pagination, and semantic changes. Version only when an incompatible change is necessary, using one consistently supported mechanism.
- Publish a deprecation notice, a migration guide, an end-of-support date, and usage telemetry by client and version. Provide contract tests, sandbox coverage, and a support escalation path before enforcement.
- Removing a field because first-party clients no longer use it can break unknown integrations. Long-lived versions create maintenance and security cost; measure adoption, rehearse shutdown, and preserve a rollback decision for the migration.

## References

- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110)
- Further reading (blog): [Stripe API release process](https://stripe.com/blog/introducing-stripes-new-api-release-process)

## What to learn next

- Official documentation: [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- Manual or specification: [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110)
- Maintainer or personal blog: [Martin Fowler's blog](https://martinfowler.com/)
- Technical blog: [Stripe engineering](https://stripe.com/blog/engineering)
- Hands-on guide: [OpenAPI learning](https://learn.openapis.org/)
