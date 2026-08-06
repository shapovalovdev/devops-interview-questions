---
title: Make log timestamps useful in incident analysis
theme: logging
difficulty: middle
type: scenario
tags: [logging, time, debugging, incident-response]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc3339
    source_type: standard
    verified_on: 2026-08-06
---

# Make log timestamps useful in incident analysis

Why can a timeline built from distributed logs be wrong, and how would you improve it?

## Answer guide

- Record an event timestamp with timezone or UTC offset in a precise, documented format such as RFC 3339, and preserve a collector receive timestamp separately. Event time represents when the producer believes the event happened; receive time helps detect delay and reordering.
- Synchronize hosts using an appropriate time service and monitor clock offset. Even synchronized clocks have bounded error, virtual machines can pause, and daylight-saving local times make unqualified timestamps ambiguous; never infer strict causal order from close timestamps alone.
- Use trace context, sequence numbers, message identifiers, and monotonic durations to establish relationships across services. During an incident compare producer time, ingestion lag, and node health; a sudden skew can make a healthy dependency appear to have responded before a request began.

## References

- [RFC 3339: date and time on the Internet](https://www.rfc-editor.org/rfc/rfc3339)
- Further reading (blog): [Cloudflare engineering blog](https://blog.cloudflare.com/)

## What to learn next

- Official documentation: [systemd time synchronization](https://www.freedesktop.org/software/systemd/man/latest/systemd-timesyncd.service.html)
- Manual or specification: [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339)
- Maintainer or personal blog: [Paul Vixie's blog](https://www.vix.com/)
- Technical blog: [Cloudflare engineering blog](https://blog.cloudflare.com/)
- Hands-on guide: [Chrony documentation](https://chrony-project.org/documentation.html)
