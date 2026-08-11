---
title: Run a platform-wide incident
theme: platform-engineering
difficulty: middle
type: troubleshooting
tags: [platform-engineering, incident-response, blast-radius, multi-tenancy]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: standard
    verified_on: 2026-08-11
---

# Run a platform-wide incident

The platform's control plane is down and forty product teams are affected at once. How do you run this incident?

## Answer guide

- Run it with the standard incident roles — an incident commander who does not debug, an operations lead who does, and a communications lead — but add the thing that makes a platform incident different: a single, authoritative status channel that the affected teams subscribe to instead of forty parallel conversations. Your first communication should state what is broken, what still works, and what teams should *not* do, because forty teams independently retrying, redeploying, or rolling back will generate a second incident on top of the first.
- Technically, the first question is whether the data plane survives the control plane. A platform whose failure only stops *changes* — no new deploys, no new provisioning — is in a far better position than one where running workloads depend on the platform to keep serving. Establish that boundary in the first minutes and say it out loud, because it determines whether this is a delivery outage or a customer-facing one. Then work the blast radius: which capabilities are degraded, which tenants are affected, and whether the failure is spreading through a shared dependency such as the identity provider, the registry, or the secret store.
- Constraints: your own tooling may be inside the blast radius, so the incident process needs an out-of-band path — a status page and chat channel that do not depend on the platform, and a documented break-glass route that lets an operator reach the underlying provider directly. Debug hooks matter as much as fixes here: hold the failing state long enough to capture evidence when you can, because a control plane restarted immediately loses the reason it failed. Note also that recovery is not the moment the control plane returns; it is the moment the backlog of queued reconciliations has drained without a thundering-herd second outage.
- Failure modes: an incident commander drawn into debugging so nobody is tracking the forty stakeholders; silence, which teams fill with their own speculative remediation; a fix applied to all tenants at once with no canary because "it is already broken"; restoring the control plane and letting every queued deploy fire simultaneously; and a postmortem that treats it as one team's outage rather than examining why a single component could take out every consumer.

## References

- [Google SRE book — managing incidents](https://sre.google/sre-book/managing-incidents/)
- Further reading (blog): [Slack engineering blog](https://slack.engineering/)

## What to learn next

- Official documentation: [Google SRE book — managing incidents](https://sre.google/sre-book/managing-incidents/)
- Manual or specification: [Google SRE workbook — incident response](https://sre.google/workbook/incident-response/)
- Maintainer or personal blog: [Charity Majors — charity.wtf](https://charity.wtf/)
- Technical blog: [Slack engineering blog](https://slack.engineering/)
- Hands-on guide: [AWS Builders' Library — workload isolation using shuffle sharding](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding/)
