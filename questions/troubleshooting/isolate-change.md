---
title: Isolate a suspected change without guessing
theme: troubleshooting
difficulty: middle
type: troubleshooting
tags: [troubleshooting, deployment, debugging, change-management]
sources:
  - url: https://sre.google/sre-book/effective-troubleshooting/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Isolate a suspected change without guessing

## Answer guide

- Build a change list covering application releases, flags, infrastructure, certificates, dependencies, and traffic shifts; correlate each with the first reliable symptom rather than the first alert.
- Reproduce the difference in a safe cohort or compare a known-good instance with a failing one. Prefer a reversible rollback, feature-flag disablement, or traffic drain that tests the hypothesis without editing unrelated configuration.
- Record the result and stop if rollback worsens impact. A temporal correlation is not proof: delayed jobs, cache expiry, and an upstream incident can make a harmless deployment appear causal.

## References

- [Google SRE Book — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)
- [Google SRE Book — Release Engineering](https://sre.google/sre-book/release-engineering/)
- Further reading (blog): [Martin Fowler — Feature toggles](https://martinfowler.com/articles/feature-toggles.html)

## What to learn next

- Free book: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official guide: [Git documentation](https://git-scm.com/doc)
- Official guide: [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/)
- Personal technical blog: [Martin Fowler](https://martinfowler.com/)
- Technical blog: [LaunchDarkly blog](https://launchdarkly.com/blog/)
