---
title: Manage an architecture decision portfolio
theme: backend-architecture
difficulty: staff
type: theory
tags: [governance, leadership, change-management]
sources:
  - url: https://adr.github.io/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Manage an architecture decision portfolio

How does a staff engineer keep consequential backend decisions discoverable and revisable?

## Answer guide

- Record decisions with context, options, chosen trade-offs, owner, affected interfaces, expected measures, and review trigger. Link them to code, operational runbooks, migrations, and deprecation dates so teams can discover why a constraint exists.
- Maintain a portfolio view for cross-cutting risks such as data stores, identity, regional dependencies, and unsupported versions. Schedule reviews when assumptions, cost, scale, regulations, or incident evidence change.
- Documentation that is never revisited becomes misleading architecture folklore, while a heavyweight committee delays delivery. Keep records short and decision-focused, then verify decisions through delivery metrics, failure drills, and consumer feedback.

## References

- [Architecture decision records](https://adr.github.io/)
- Further reading (personal blog): [Michael Nygard: ADRs](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

## What to learn next

- Official documentation: [ADR documentation](https://adr.github.io/)
- Manual or specification: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
- Maintainer or personal blog: [Martin Fowler's blog](https://martinfowler.com/)
- Technical blog: [Thoughtworks Insights](https://www.thoughtworks.com/insights)
- Hands-on guide: [MADR documentation](https://adr.github.io/madr/)
