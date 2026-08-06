---
title: Explain syslog facilities and severity
theme: logging
difficulty: junior
type: theory
tags: [logging, linux, operations, troubleshooting]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc5424
    source_type: standard
    verified_on: 2026-08-06
---

# Explain syslog facilities and severity

What information do syslog facility and severity carry, and what should an operator not infer from them?

## Answer guide

- RFC 5424 identifies a message using a priority value formed from facility and severity. Facility groups the producer category, while severity expresses the sender's urgency scale. Receivers can route or retain records differently based on those fields.
- The fields are sender-supplied classifications, not proof of impact. Different applications often choose levels differently, and relays may rewrite, parse, or lose metadata. Preserve the raw record plus normalized fields when ingesting mixed legacy sources.
- Use a documented mapping for each managed producer and test it with a receiver. Transport security, queueing, timestamp accuracy, and rate limiting are separate design choices; an error-level record can still be delayed or dropped if the transport is unavailable.

## References

- [RFC 5424: the syslog protocol](https://www.rfc-editor.org/rfc/rfc5424)
- Further reading (blog): [Better Stack logging guides](https://betterstack.com/community/guides/logging/)

## What to learn next

- Official documentation: [systemd-journald service](https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html)
- Manual or specification: [RFC 5424](https://www.rfc-editor.org/rfc/rfc5424)
- Maintainer or personal blog: [rsyslog project site](https://www.rsyslog.com/)
- Technical blog: [Better Stack logging guides](https://betterstack.com/community/guides/logging/)
- Hands-on guide: [rsyslog documentation](https://www.rsyslog.com/doc/)
