---
title: Design reliable multi-team incident handoffs
theme: troubleshooting
difficulty: staff
type: scenario
tags: [troubleshooting, leadership, incident-management, runbooks, reliability]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Design reliable multi-team incident handoffs
## Answer guide
- Require an explicit transfer of incident command with acknowledged ownership, current impact, timeline, hypotheses, completed and pending actions, risks, and the next decision point. Keep a durable shared state document independent of the affected service.
- Define interfaces between product, platform, vendor, security, and communications teams, including who can change which systems. Use periodic summaries so new responders can become useful without replaying every chat message.
- Exercise handoffs during simulations and measure information loss or duplicated work. Rotations and time zones are operational constraints; an informal “someone is watching it” handoff creates hidden gaps in authority and coverage.
## References
- [Google SRE Book — Managing Incidents](https://sre.google/sre-book/managing-incidents/)
- [Google SRE Book — Communication and Collaboration](https://sre.google/sre-book/communication-and-collaboration/)
- Further reading (blog): [John Allspaw — coordination](https://www.kitchensoap.com/)
## What to learn next
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [FEMA NIMS](https://www.fema.gov/emergency-managers/nims)
- Hands-on guide: [Google SRE incident management](https://sre.google/sre-book/managing-incidents/)
- Maintainer or personal blog: [John Allspaw](https://www.kitchensoap.com/)
- Technical blog: [PagerDuty resources](https://www.pagerduty.com/resources/learn/)
