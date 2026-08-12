---
title: Retire a platform capability
theme: platform-engineering
difficulty: middle
type: scenario
tags: [platform-engineering, deprecation, migration, adoption]
sources:
  - url: https://cloud.google.com/apis/design/compatibility
    source_type: official-docs
    verified_on: 2026-08-11
---

# Retire a platform capability

The platform's old build service has twelve remaining users and costs a quarter of the team's time. How do you retire it?

## Answer guide

- Retirement is a migration project with a shutdown date attached, and it fails when the date is announced before the destination exists. Sequence it: build and prove the replacement, migrate a friendly user and write down every surprise, publish a dated deprecation notice with the exact removal date, stop new signups on the same day, migrate the remaining users with the platform team doing the work rather than filing tickets, then disable and finally delete. Announcing a removal date while the replacement is still missing a feature twelve users depend on converts a migration into an escalation.
- Give the notice teeth by making the old path progressively less attractive without breaking it: warnings in the CLI output and build logs, the capability hidden from the catalog and templates, a weekly report of remaining consumers by owner, and — near the end — brownouts, short deliberate outages announced in advance that surface the consumers who never read email. The compatibility guidance behind stable API surfaces is the same principle at the field level: removing surface is a breaking change, so it needs a version boundary and notice, not a quiet delete.
- Constraints: you need an accurate consumer list, which means usage telemetry on the old capability before you start, not a wiki page of who you think uses it. Budget the migration effort as platform work in the roadmap; twelve migrations at two days each is real capacity. Keep the data and audit obligations in view — an old build service may hold artefacts someone is legally required to retain past the shutdown.
- Failure modes: deleting the capability while an artefact, credential or DNS name it created is still referenced elsewhere; the last two consumers being the ones with no capacity and the most political weight, so the date slips indefinitely and the "deprecated" system runs for three more years; brownouts run without notice during a business-critical window; and turning off the service but leaving its infrastructure running, so the cost saving never materialises.

## References

- [Google API design guide — compatibility](https://cloud.google.com/apis/design/compatibility)
- Further reading (blog): [GitHub blog](https://github.blog/)

## What to learn next

- Official documentation: [Google API design guide — compatibility](https://cloud.google.com/apis/design/compatibility)
- Manual or specification: [Semantic Versioning 2.0.0](https://semver.org/)
- Maintainer or personal blog: [Matthew Skelton — blog](https://blog.matthewskelton.net/)
- Technical blog: [GitHub blog](https://github.blog/)
- Hands-on guide: [Backstage — adopting Backstage](https://backstage.io/docs/overview/adopting)
