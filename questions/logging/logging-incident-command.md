---
title: Use logs effectively during a cross-service incident
theme: logging
difficulty: staff
type: scenario
tags: [logging, incident-management, leadership, troubleshooting]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use logs effectively during a cross-service incident

How should an incident commander use a shared logging system during a major outage?

## Answer guide

- Establish a time-bounded hypothesis and a common correlation key, then delegate focused log investigation to named responders. Use saved searches and dashboards that show service, deployment, region, error class, and ingestion health; avoid having every responder run unbounded searches against production.
- Treat logs as one signal among metrics, traces, changes, and customer reports. Validate that an apparent absence of errors is not a collector outage, sampling policy, clock skew, permission problem, or query mistake. Preserve relevant queries and exports as incident artifacts.
- After mitigation, capture which fields, links, retention, permissions, or runbooks delayed diagnosis and feed those into platform work. Do not use an emergency broad-access grant as a permanent operating model; replace it with least-privilege incident roles and tested break-glass controls.

## References

- [Google SRE Book: managing incidents](https://sre.google/sre-book/managing-incidents/)
- Further reading (blog): [PagerDuty: incident commander training](https://response.pagerduty.com/training/incident_commander/)

## What to learn next

- Official documentation: [Google SRE incident management](https://sre.google/sre-book/managing-incidents/)
- Manual or specification: [NIST SP 800-61 incident response](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
- Maintainer or personal blog: [John Allspaw's writing](https://www.kitchensoap.com/)
- Technical blog: [PagerDuty incident commander training](https://response.pagerduty.com/training/incident_commander/)
- Hands-on guide: [Google SRE incident response workbook](https://sre.google/workbook/incident-response/)
