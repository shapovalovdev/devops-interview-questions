# Logging: related materials

Use these resources alongside the Logging Questions. They are selected for the platform's common data model, operational pipeline design, and safe investigation practices.

## What to learn next

- Official documentation: [OpenTelemetry logging](https://opentelemetry.io/docs/specs/otel/logs/)
- Manual or specification: [RFC 5424: syslog protocol](https://www.rfc-editor.org/rfc/rfc5424)
- Maintainer or personal blog: [Charity Majors' writing](https://charity.wtf/)
- Technical blog: [Grafana: concise guide to Loki labels](https://grafana.com/blog/the-concise-guide-to-grafana-loki-everything-you-need-to-know-about-labels/)
- Hands-on guide: [Fluent Bit manual](https://docs.fluentbit.io/manual/)

## Suggested study order

Begin where container logs begin: why services write to standard streams, what
syslog facilities and severity mean, and how structured logs with request
correlation turn streams into evidence. Design the data model next — field
choices, the log-level policy, multiline exception parsing, rotation without
duplicate or missing events, timestamps that survive incident analysis —
because the pipeline questions are about moving and protecting that model. The
platform tier follows: collector buffering and backpressure, a
delivery-pipeline SLO, schema evolution without breaking consumers, and the
slow expensive query that poor field design writes. Then the duties that
outrank features: keeping secrets out of logs and privacy by design, with
retention, cost attribution and reduction, tenant isolation, and log integrity
for investigations beside them. Finish with use and strategy — correlating
trace context with logs, reading logs across services mid-incident, then the
migration from fragmented logging, ownership boundaries, and the
organization-wide platform decision.
