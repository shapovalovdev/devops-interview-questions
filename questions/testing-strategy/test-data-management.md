---
title: Manage test data safely
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/122/final
    source_type: standard
    verified_on: 2026-08-10
  - url: https://postgresql-anonymizer.readthedocs.io/en/stable/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Manage test data safely

How should a team make this testing strategy decision?

## Answer guide

- Define the user-facing risk and select evidence that represents it without making every change wait on slow, unrelated systems.
- Keep dependencies, data ownership, and environment isolation explicit so results are reproducible and failures are diagnosable.
- Balance test cost, feedback speed, and release confidence; combine automated checks with reviews and operational signals.
- Reassess after incidents and architecture changes because an uncontrolled test boundary can become a source of false confidence.

## References

- [NIST SP 800-122 — protecting the confidentiality of personally identifiable information](https://csrc.nist.gov/pubs/sp/800/122/final)
- [PostgreSQL Anonymizer documentation](https://postgresql-anonymizer.readthedocs.io/en/stable/)
- Further reading (blog): [Thoughtworks Technology Radar — production data in test environments](https://www.thoughtworks.com/radar/techniques/production-data-in-test-environments)

## What to learn next

- Official documentation: [PostgreSQL Anonymizer documentation](https://postgresql-anonymizer.readthedocs.io/en/stable/)
- Manual or specification: [NIST SP 800-122 — protecting the confidentiality of personally identifiable information](https://csrc.nist.gov/pubs/sp/800/122/final)
- Maintainer or personal blog: [Vladimir Khorikov — how to assert database state](https://enterprisecraftsmanship.com/posts/how-to-assert-database-state/)
- Technical blog: [Thoughtworks Technology Radar — production data in test environments](https://www.thoughtworks.com/radar/techniques/production-data-in-test-environments)
- Hands-on guide: [DORA — test data management capability](https://dora.dev/capabilities/test-data-management/)
