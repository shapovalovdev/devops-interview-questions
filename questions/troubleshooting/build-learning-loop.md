---
title: Build a learning loop from production troubleshooting
theme: troubleshooting
difficulty: staff
type: scenario
tags: [troubleshooting, leadership, automation, reliability, runbooks]
sources:
  - url: https://sre.google/sre-book/postmortem-culture/
    source_type: official-docs
    verified_on: 2026-08-06
---
# Build a learning loop from production troubleshooting
## Answer guide
- Capture observed facts, decision rationale, successful and failed mitigations, and system conditions in a reviewable record. Separate accountability for system improvements from blame for human actions under uncertainty.
- Convert repeated diagnostic work into tested runbooks, automated checks, safer defaults, and training scenarios. Review links and ownership regularly so a runbook does not become an unsafe historical artifact.
- Track whether changes reduce recurrence and time to recovery across representative incidents. Do not automate a flawed workaround or measure learning only by meeting attendance; evidence of improved reliability is the desired outcome.
## References
- [Google SRE Book — Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- [Google SRE Book — Eliminating Toil](https://sre.google/sre-book/eliminating-toil/)
- Further reading (blog): [Jesse Robbins — resilient operations](https://www.jesserobbins.com/)
## What to learn next
- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [Google SRE workbook](https://sre.google/workbook/table-of-contents/)
- Hands-on guide: [NIST incident handling](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
- Maintainer or personal blog: [Jesse Robbins](https://www.jesserobbins.com/)
- Technical blog: [Gremlin blog](https://www.gremlin.com/blog/)
