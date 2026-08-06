---
title: Govern risky mitigations during a business-critical outage
theme: troubleshooting
difficulty: staff
type: scenario
tags: [troubleshooting, leadership, change-management, incident-response, reliability]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Govern risky mitigations during a business-critical outage
## Answer guide
- Make the trade-off explicit: current customer harm, expected mitigation benefit, blast radius, reversibility, data-integrity risk, and who has authority to accept it. Keep an incident commander independent from executive pressure where possible.
- Prefer actions that reduce load, isolate scope, or restore a known-good path before irreversible data changes. Require a named operator, observer, rollback trigger, and communication plan for any high-risk intervention.
- Document the decision and reassess as evidence changes. Emergency authority must not become a way to bypass security, audit, or customer commitments permanently; schedule a post-incident review of both outcome and decision process.
## References
- [Google SRE Book — Managing Incidents](https://sre.google/sre-book/managing-incidents/)
- [Google SRE Book — Emergency Response](https://sre.google/sre-book/emergency-response/)
- Further reading (blog): [John Allspaw — resilience](https://www.kitchensoap.com/)
## What to learn next
- Free book: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official guide: [NIST incident handling](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
- Official guide: [Google SRE incident management](https://sre.google/sre-book/managing-incidents/)
- Personal technical blog: [John Allspaw](https://www.kitchensoap.com/)
- Technical blog: [AWS Builders’ Library](https://aws.amazon.com/builders-library/)
