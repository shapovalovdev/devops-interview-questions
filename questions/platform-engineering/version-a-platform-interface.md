---
title: Version a platform interface
theme: platform-engineering
difficulty: middle
type: scenario
tags: [platform-engineering, api-versioning, internal-developer-platform, change-management]
sources:
  - url: https://kubernetes.io/docs/reference/using-api/deprecation-policy/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Version a platform interface

Your platform's workload abstraction needs a field renamed and a default changed. How do you version the interface so eighty consuming teams are not broken?

## Answer guide

- Version the schema, not the implementation, and make the version explicit in every declaration teams write. Kubernetes shows the working model: an API is identified by group and version, an object is stored once but served at every supported version through conversion, and stability tiers (alpha, beta, GA) carry different promises. Adopt the same shape for a platform CRD or workload file — `platform.example.com/v1beta1` — so a team can read its own manifest and know what guarantees apply.
- Rename with an additive, two-sided migration rather than an edit. Add the new field alongside the old one, have the platform accept both and write both for a full release cycle, emit a deprecation warning naming the manifest and the replacement, migrate consumers, then remove the old field only in a new version. A default change is the harder case: pin existing workloads to the old default explicitly at the moment you change it, so the new default applies to new workloads and no running service silently changes behaviour on the next reconcile.
- Constraints from the Kubernetes deprecation policy are the right floor to borrow: a GA API version may not be removed within a major release and gets long notice; beta gets three releases or nine months, whichever is longer; alpha may go at any time. A field, once GA, cannot change meaning without a version bump, and a released version must never be made more restrictive — a manifest that validated yesterday must still validate today.
- Failure modes: "we'll just update everyone's YAML for them", which works until a team has a generated or vendored copy; a version bump that changes semantics while keeping the field name, so a valid manifest quietly does something different; supporting so many concurrent versions that the conversion code becomes the platform's largest liability; deprecation warnings written to a log nobody reads instead of surfaced in the tool the developer runs; and beta APIs that everyone treats as permanent because they were never removed.

## References

- [Kubernetes deprecation policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/)
- Further reading (blog): [Kubernetes blog](https://kubernetes.io/blog/)

## What to learn next

- Official documentation: [Kubernetes deprecation policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/)
- Manual or specification: [Google API design guide — versioning](https://cloud.google.com/apis/design/versioning)
- Maintainer or personal blog: [Gregor Hohpe — The Architect Elevator](https://architectelevator.com/blog/)
- Technical blog: [Kubernetes blog](https://kubernetes.io/blog/)
- Hands-on guide: [Kubernetes API concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/)
