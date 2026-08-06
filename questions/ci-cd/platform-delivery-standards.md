---
title: Establish organization-wide delivery standards
theme: ci-cd
difficulty: staff
type: scenario
tags: [ci-cd, platform-engineering, governance, security, reliability]
sources:
  - url: https://slsa.dev/spec/v1.0/levels
    source_type: standard
    verified_on: 2026-08-06
---

# Establish organization-wide delivery standards

How would you set delivery standards that improve safety without centralizing every team’s release work?

## Answer guide

- Publish a paved path with versioned reusable workflows, artifact/provenance requirements, protected environments, baseline checks, and observable deployment events.
- Define policy outcomes and measurable service levels—lead time, change-failure rate, recovery time, gate reliability—then allow documented exceptions with expiry and accountable owners.
- Co-design standards with application and security teams, migrate incrementally, and preserve local autonomy for justified differences. A mandatory platform that is slower or less capable than bespoke scripts drives shadow pipelines.

## References

- [SLSA: Build security levels](https://slsa.dev/spec/v1.0/levels)
- [Further reading: GitHub Docs—reusable workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations)
