---
title: Lead a cross-service consistency incident
theme: distributed-systems
difficulty: staff
type: troubleshooting
tags: [incident-management, recovery, reliability]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Lead a cross-service consistency incident

How should an incident leader respond when different services disagree about customer state?

## Answer guide

- Establish incident command, scope the invariant at risk, and stop or fence unsafe writes before attempting repair. Create a time-ordered evidence trail from immutable logs, database positions, event identifiers, and deployment history; name one authoritative source for each affected record.
- Split work into containment, customer impact, diagnosis, reconciliation, and communication tracks. Use dry runs and sampled verification for repairs, preserve originals, and document decisions so a second region or team does not make a conflicting correction.
- Fast manual updates without provenance can create more divergence. Stale dashboards, replayed events, and concurrent recovery jobs can overwrite fixes; avoid declaring recovery from availability alone until integrity checks and customer-visible outcomes are verified.

## References

- [Google SRE: managing incidents](https://sre.google/sre-book/managing-incidents/)
- Further reading (personal blog): [Aphyr: Jepsen](https://aphyr.com/tags/jepsen)

## What to learn next

- Official documentation: [Google SRE incident management](https://sre.google/sre-book/managing-incidents/)
- Manual or specification: [Google SRE: data integrity](https://sre.google/sre-book/data-integrity/)
- Maintainer or personal blog: [Aphyr's blog](https://aphyr.com/)
- Technical blog: [Google Cloud SRE](https://cloud.google.com/blog/products/devops-sre)
- Hands-on guide: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
