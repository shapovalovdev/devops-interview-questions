---
title: Establish impact before changing a failing service
theme: troubleshooting
difficulty: junior
type: troubleshooting
tags: [troubleshooting, incident-response, monitoring, reliability]
sources:
  - url: https://sre.google/sre-book/effective-troubleshooting/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Establish impact before changing a failing service

## Answer guide

- Start with the user-visible symptom: identify the affected journey, error rate, latency, regions, start time, and whether the alert is an observation or merely a detector failure. Record a baseline before making a change.
- Compare a known-good scope with a failing scope and inspect recent deploys, configuration, dependency health, and resource saturation. Form one falsifiable hypothesis at a time; changing several variables destroys the evidence.
- Mitigate reversible, high-confidence causes first and state the expected result and rollback. If customers are affected or investigation crosses teams, declare an incident, preserve timestamps and logs, and keep stakeholders informed.

## References

- [Google SRE Book — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)
- [Google SRE Book — Managing Incidents](https://sre.google/sre-book/managing-incidents/)
- Further reading (blog): [Brendan Gregg — Linux performance](https://www.brendangregg.com/linuxperf.html)

## What to learn next

- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [Google SRE — Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/)
- Hands-on guide: [Google SRE — Postmortems](https://sre.google/sre-book/postmortem-culture/)
- Maintainer or personal blog: [Brendan Gregg’s blog](https://www.brendangregg.com/blog/)
- Technical blog: [Red Hat Enable Sysadmin](https://www.redhat.com/en/blog/channel/enable-sysadmin)
