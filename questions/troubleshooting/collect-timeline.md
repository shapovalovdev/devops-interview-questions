---
title: Build an incident timeline from reliable evidence
theme: troubleshooting
difficulty: junior
type: scenario
tags: [troubleshooting, logs, monitoring, incident-response]
sources:
  - url: https://sre.google/sre-book/managing-incidents/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Build an incident timeline from reliable evidence

## Answer guide

- Capture when users first saw impact, alert firing, deployments, configuration changes, dependency events, mitigations, and recovery. Mark each entry as observed evidence or a hypothesis so later analysis does not turn guesses into facts.
- Normalize clocks and include source identifiers, query links, and relevant request or trace IDs. Distributed systems can emit events late or with skew, so sequence evidence conservatively rather than assuming a log order proves causality.
- Keep the timeline in a shared incident document and appoint one person to maintain it during a broad event. It supports handoff and rollback decisions; preserve immutable audit records before retention removes them.

## References

- [Google SRE Book — Managing Incidents](https://sre.google/sre-book/managing-incidents/)
- [Google SRE Book — Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- Further reading (blog): [Charity Majors — Observability](https://charity.wtf/)

## What to learn next

- Manual or specification: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official documentation: [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/)
- Hands-on guide: [RFC 3339 timestamps](https://www.rfc-editor.org/rfc/rfc3339)
- Maintainer or personal blog: [Charity Majors](https://charity.wtf/)
- Technical blog: [Honeycomb blog](https://www.honeycomb.io/blog)
