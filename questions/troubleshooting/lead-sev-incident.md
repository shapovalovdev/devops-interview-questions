---
title: Lead a severe incident without uncontrolled changes
theme: troubleshooting
difficulty: senior
type: scenario
tags: [troubleshooting, incident-response, leadership, reliability, change-management]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Lead a severe incident without uncontrolled changes
## Answer guide
- Declare the incident early, set a clear incident commander, operations lead, communications lead, and shared state document. State customer impact, objective, current hypothesis, and the decision authority for production changes.
- Assign bounded investigations and require proposals to include expected outcome, risk, rollback, and evidence. Keep all mutations with the operations team; parallel “just looking” changes make causality and recovery harder.
- Stabilize service before root cause, communicate at a predictable cadence, and perform explicit handoff. Preserve an evidence-backed timeline for a blameless postmortem with owners for follow-up safeguards.
## References
- [Google SRE Book — Managing Incidents](https://sre.google/sre-book/managing-incidents/)
- [Google SRE Book — Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- Further reading (blog): [John Allspaw — incident response](https://www.kitchensoap.com/)
## What to learn next
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [FEMA incident command](https://www.fema.gov/emergency-managers/nims/components)
- Hands-on guide: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
- Maintainer or personal blog: [John Allspaw](https://www.kitchensoap.com/)
- Technical blog: [PagerDuty incident response](https://www.pagerduty.com/resources/learn/)
