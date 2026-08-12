---
title: Use shadow traffic safely
theme: testing-strategy
difficulty: staff
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://istio.io/latest/docs/tasks/traffic-management/mirroring/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://sre.google/sre-book/testing-reliability/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Use shadow traffic safely

You want to validate a rewritten pricing service against real traffic before it serves any user. How do you mirror production requests to it without the users noticing and without the shadow doing anything real?

## Answer guide

- Mirror at the proxy, fire-and-forget. Istio's mirroring sends a copy of the request to a second destination with the `-shadow` suffix appended to the Host header, and the response is discarded — the caller never waits for it and never sees its status or latency. `mirrorPercentage` controls the fraction copied, so you start at a few percent. The shadow deployment must be a separate workload from the primary, since mirroring to the same service just doubles its load.
- The hard part is side effects, and mirroring does nothing about them. Every write the shadow performs happens for real unless you prevent it: charges, emails, inventory decrements, outbound webhooks, analytics events, and rows in the shared database. Give the shadow its own datastore seeded from a snapshot, replace outbound integrations with fakes, and where a code path cannot be made read-only, gate it on a request-scoped shadow flag propagated as a header so the service itself knows it is not authoritative. Personal data reaching a less-hardened shadow is a real disclosure, not a test artifact.
- Getting value out requires comparison, which is a separate build. Log a normalised response from both the primary and the shadow keyed by request ID, diff them offline, and ignore fields that are legitimately non-deterministic — timestamps, generated IDs, ordering, floating-point formatting — or the diff is 100% mismatch and gets switched off in a week. Report the mismatch rate by endpoint and by response field, not as a single number, because the useful finding is almost always one field on one path.
- Costs and failure modes: shadowing doubles downstream load, so a shared dependency such as the database or an authentication service sees twice the traffic and the experiment can cause the incident it was meant to prevent; the shadow at capacity can back up the sidecar's connection pool even in fire-and-forget mode; mirrored traffic is representative only of what currently flows, so paths behind a flag or a seasonal peak stay untested; and a shadow that quietly shares a cache, queue, or feature-flag store with the primary is not a shadow at all.

## References

- [Istio — mirroring traffic to a second service](https://istio.io/latest/docs/tasks/traffic-management/mirroring/)
- [Google SRE Book — testing for reliability](https://sre.google/sre-book/testing-reliability/)
- Further reading (blog): [Martin Fowler — dark launching](https://martinfowler.com/bliki/DarkLaunching.html)

## What to learn next

- Official documentation: [Istio — traffic management concepts](https://istio.io/latest/docs/concepts/traffic-management/)
- Manual or specification: [Google SRE Book — testing for reliability](https://sre.google/sre-book/testing-reliability/)
- Maintainer or personal blog: [Martin Fowler — dark launching](https://martinfowler.com/bliki/DarkLaunching.html)
- Technical blog: [Honeycomb — testing in production, should you do it?](https://www.honeycomb.io/blog/testing-in-production)
- Hands-on guide: [Istio — mirroring traffic to a second service](https://istio.io/latest/docs/tasks/traffic-management/mirroring/)
