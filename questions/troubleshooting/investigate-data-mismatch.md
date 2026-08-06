---
title: Investigate a production data mismatch safely
theme: troubleshooting
difficulty: middle
type: troubleshooting
tags: [troubleshooting, databases, recovery, reliability, incident-response]
sources:
  - url: https://sre.google/sre-book/data-integrity/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Investigate a production data mismatch safely

## Answer guide

- Define the expected invariant, affected records, source of truth, and evidence of incorrect reads or writes. Preserve audit trails and take a consistent backup or snapshot according to the datastore’s documented procedure before attempting repair.
- Determine whether the mismatch is display lag, replication delay, an idempotency failure, schema interpretation, or actual corruption. Reconcile from authoritative events with a reviewed, bounded job rather than ad-hoc production edits.
- Validate repaired data with independent checks and monitor for recurrence. Avoid destructive cleanup, replaying non-idempotent messages, or restoring broad backups without understanding concurrent legitimate writes.

## References

- [Google SRE Book — Data Integrity](https://sre.google/sre-book/data-integrity/)
- [Google SRE Book — Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- Further reading (blog): [Jepsen analyses](https://jepsen.io/analyses)

## What to learn next

- Free book: [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- Official guide: [PostgreSQL backup documentation](https://www.postgresql.org/docs/current/backup.html)
- Official guide: [Kafka delivery semantics](https://kafka.apache.org/documentation/#semantics)
- Personal technical blog: [Jepsen](https://aphyr.com/)
- Technical blog: [Cockroach Labs blog](https://www.cockroachlabs.com/blog/)
