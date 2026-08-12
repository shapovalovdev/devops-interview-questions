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

Someone proposes restoring last night's production database into the staging environment so tests run against realistic data. What has to be true before that is acceptable, and what would you do instead?

## Answer guide

- A production restore moves personal data into an environment with different controls, and it is the access model that fails first: staging typically grants read access to every engineer, logs queries verbosely, has weaker retention rules, and is backed up to somewhere nobody has inventoried. Under NIST SP 800-122's framing you owe the same protection to the PII regardless of which system holds it, so the copy inherits every obligation of production — access control, breach reporting, deletion requests — while having none of production's controls. That is the fact that decides the proposal.
- The workable version is a de-identified extract produced by an owned, repeatable job, not a hand-cleaned dump. PostgreSQL Anonymizer applies masking rules declared on the columns themselves — static masking that rewrites the table in place, dynamic masking that shows masked values to a restricted role, and generalisation for quasi-identifiers — so the rules live with the schema and a new column defaults to being unmasked loudly rather than leaking quietly. Run it inside the production trust boundary and export only the masked result, since anonymising after the copy has already landed in staging means the raw data was there.
- Masking is weaker than it looks: a birth date plus a postcode plus a gender re-identifies a large share of a population, so masking direct identifiers while keeping the quasi-identifiers intact is not de-identification. Referential integrity has to survive the transformation or joins break and the data stops being realistic, which means a deterministic, keyed pseudonym per subject rather than an independent random value per table. And free-text columns — support tickets, addresses, notes — are the ones no column rule catches; usually they are dropped rather than masked.
- Prefer synthetic data generated from the schema and a factory for most testing, since it is cheap, shareable, and safe, and reserve masked extracts for the cases that genuinely need production's shape — volume, cardinality, and skew for performance work, and long-tail records for migration testing. Failure modes: a masking job that skips a newly added column because the rule set was not updated; a subset copy that breaks foreign keys and hides bugs behind missing rows; and an extract with no expiry, so a copy from two years ago is still sitting in a bucket when the breach happens.

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
