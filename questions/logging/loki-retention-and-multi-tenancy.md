---
title: Design Loki retention and multi-tenancy
theme: logging
difficulty: senior
type: scenario
tags: [logging, loki, grafana, multi-tenancy]
sources:
  - url: https://grafana.com/docs/loki/latest/operations/storage/retention/
    source_type: official-docs
    verified_on: 2026-08-17
  - url: https://grafana.com/docs/loki/latest/operations/multi-tenancy/
    source_type: official-docs
    verified_on: 2026-08-17
---

# Design Loki retention and multi-tenancy

You run one Loki cluster for three teams with different retention needs: platform logs for 30 days, application logs for 14 days, and a compliance tenant that must keep audit logs for a year. Design the retention and tenant isolation for this cluster.

## Answer guide

- Enable multi-tenancy (`auth_enabled: true`) and give each team its own tenant; every request then carries an `X-Scope-OrgID` header, and data, index entries, and storage prefixes are partitioned per tenant, so one team's queries, rate limits, and deletions cannot touch another's data.
- Retention is applied by the Compactor: run it as a singleton with `retention_enabled: true`, a persistent working directory for its marker files, and a `delete_request_store`; without the Compactor's retention explicitly enabled, logs live forever regardless of what the object store does.
- Set periods through `limits_config.retention_period` plus per-tenant overrides in a runtime overrides file: 720h for the platform tenant, 336h for applications, 8760h for audit, and use `retention_stream` selectors (label matchers only, minimum 24h) for finer splits such as shorter retention on debug-level streams. Retention changes are not retroactive, so agree on periods before ingestion, not after.
- Guard the object store: if you also configure bucket lifecycle rules as a cost safety net, scope them to per-tenant chunk prefixes only and set expiry longer than retention plus `retention_delete_delay` — a blanket age-based rule will delete index files and the cluster seed and corrupt the store. Finally, constrain tenant IDs (≤150 bytes, restricted character set, never `.` or `..`) and keep them short and stable so prefixes and overrides stay manageable.

## References

- [Log retention in Loki](https://grafana.com/docs/loki/latest/operations/storage/retention/)
- [Manage tenant isolation](https://grafana.com/docs/loki/latest/operations/multi-tenancy/)
- Further reading (blog): [How labels in Loki can make log queries faster and easier](https://grafana.com/blog/how-labels-in-loki-can-make-log-queries-faster-and-easier/)

## What to learn next

- Official documentation: [Log retention](https://grafana.com/docs/loki/latest/operations/storage/retention/)
- Manual or specification: [Manage tenant isolation](https://grafana.com/docs/loki/latest/operations/multi-tenancy/)
- Maintainer or personal blog: [Grafana Labs blog](https://grafana.com/blog/)
- Technical blog: [How labels in Loki can make log queries faster and easier](https://grafana.com/blog/how-labels-in-loki-can-make-log-queries-faster-and-easier/)
- Hands-on guide: [Send data to Loki and query it back](https://grafana.com/docs/loki/latest/send-data/)
