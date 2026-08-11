---
title: Attribute and reduce logging cost safely
theme: logging
difficulty: senior
type: scenario
tags: [logging, cost-optimization, capacity-planning, governance]
sources:
  - url: https://grafana.com/docs/loki/latest/get-started/labels/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Attribute and reduce logging cost safely

How would you reduce an unexpectedly large logging bill without losing incident evidence?

## Answer guide

- Attribute volume, indexed cardinality, retention, query scans, and egress to service, environment, tenant, and event class. Inspect the largest contributors before changing global sampling: a new debug loop, stack trace storm, or uncontrolled label often explains the majority.
- Reduce unnecessary detail at the source, deduplicate or rate-limit repetitive events, lower retention for low-value classes, and move rarely queried data to an archive when retrieval is tested. Preserve security and audit obligations and make every reduction visible as a policy change.
- Do not use broad deletion or sampling as the first response to an incident. It can erase the very evidence needed to diagnose the source. Establish budgets and alerts for ingestion and query cost, then validate that the remaining events still support key runbooks.

## References

- [Loki label best practices](https://grafana.com/docs/loki/latest/get-started/labels/)
- Further reading (blog): [Grafana: cost-efficient Loki log queries](https://grafana.com/blog/grafana-labs-acquires-logline/)

## What to learn next

- Official documentation: [Loki labels](https://grafana.com/docs/loki/latest/get-started/labels/)
- Manual or specification: [NIST SP 800-92 Rev. 1 (initial public draft) — guide to computer security log management](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd)
- Maintainer or personal blog: [Charity Majors' writing](https://charity.wtf/)
- Technical blog: [Grafana: cost-efficient Loki log queries](https://grafana.com/blog/grafana-labs-acquires-logline/)
- Hands-on guide: [Loki retention configuration](https://grafana.com/docs/loki/latest/operations/storage/retention/)
