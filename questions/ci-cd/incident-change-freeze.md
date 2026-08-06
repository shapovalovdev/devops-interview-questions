---
title: Decide whether to freeze deployments during an incident
theme: ci-cd
difficulty: senior
type: scenario
tags: [ci-cd, incident-response, deployment, reliability]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Decide whether to freeze deployments during an incident

When should an incident commander pause deployments, and when may a change continue?

## Answer guide

- Pause nonessential changes when they complicate diagnosis, add risk, or affect the impacted dependency; record the freeze scope and the person who can lift it.
- Allow a narrowly scoped, reviewed mitigation or rollback when its expected benefit outweighs its risk, with observability and a backout path.
- A blanket freeze can delay urgent remediation and accumulate risky changes. Keep an exception process, capture timeline evidence, and reassess as the incident hypothesis and blast radius change.

## References

- [Google SRE Book: Managing incidents](https://sre.google/sre-book/managing-incidents/)
- [Further reading: Google SRE Workbook—canarying releases](https://sre.google/workbook/canarying-releases/)
