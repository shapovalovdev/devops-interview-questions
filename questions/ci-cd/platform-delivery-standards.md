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

- Further reading (blog): [Complementary ci cd practice article](https://github.blog/enterprise-software/ci-cd/continuous-deployment-with-github-actions/)
- [SLSA: Build security levels](https://slsa.dev/spec/v1.0/levels)
- [Further reading: GitHub Docs—reusable workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations)

## What to learn next

- Official documentation: [GitHub Actions reusable workflows](https://docs.github.com/en/actions/how-tos/sharing-automations/reusing-workflows)
- Manual or specification: [SLSA specification](https://slsa.dev/spec/v1.0/)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [GitHub Blog — CI/CD](https://github.blog/enterprise-software/ci-cd/)
- Hands-on guide: [Practical guide](https://docs.github.com/en/actions/tutorials/create-actions)
