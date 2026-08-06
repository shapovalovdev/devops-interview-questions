---
title: Reduce recurring incidents across a platform portfolio
theme: troubleshooting
difficulty: staff
type: scenario
tags: [troubleshooting, leadership, reliability, capacity-planning, automation]
sources:
  - url: https://sre.google/sre-book/postmortem-culture/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Reduce recurring incidents across a platform portfolio
## Answer guide
- Group incidents by mechanism and customer impact, not by the team that happened to receive the page. Quantify recurrence, toil, error-budget spend, and shared dependencies to choose investments with portfolio-level leverage.
- Turn accepted actions into owned, time-bound reliability work: guardrails, capacity models, tests, migration plans, and removal of unsafe manual paths. Verify effectiveness through drills and production outcomes rather than closing actions on document completion.
- Balance standardization with product context and publish decisions so teams can reuse them. Avoid vanity counts of postmortems or alerts closed; those can conceal unreported incidents and shift risk to less visible services.
## References
- [Google SRE Book — Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- [Google SRE Book — Eliminating Toil](https://sre.google/sre-book/eliminating-toil/)
- Further reading (blog): [Charity Majors — operational learning](https://charity.wtf/)
## What to learn next
- Free book: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official guide: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
- Official guide: [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- Personal technical blog: [Charity Majors](https://charity.wtf/)
- Technical blog: [Google Cloud reliability](https://cloud.google.com/blog/products/devops-sre)
