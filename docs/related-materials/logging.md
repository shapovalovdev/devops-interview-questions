# Logging: related materials

Use these resources alongside the Logging Questions. They are selected for the platform's common data model, operational pipeline design, and safe investigation practices.

## What to learn next

- Official documentation: [OpenTelemetry logging](https://opentelemetry.io/docs/specs/otel/logs/)
- Manual or specification: [RFC 5424: syslog protocol](https://www.rfc-editor.org/rfc/rfc5424)
- Maintainer or personal blog: [Charity Majors' writing](https://charity.wtf/)
- Technical blog: [Grafana: concise guide to Loki labels](https://grafana.com/blog/the-concise-guide-to-grafana-loki-everything-you-need-to-know-about-labels/)
- Hands-on guide: [Fluent Bit manual](https://docs.fluentbit.io/manual/)

## Suggested study order

Streams before data model, data model before pipeline, pipeline before duties
and strategy — the pipeline questions are about moving and protecting the model.

1. [Explain why containers log to standard streams](../../questions/logging/stdout-in-containers.html)
    — The Theme begins where container logs begin: standard streams as the
    platform contract.
2. [Explain syslog facilities and severity](../../questions/logging/syslog-basics.html)
    — Facilities and severity are the vocabulary those streams inherit from
    syslog.
3. [Design structured logs for request correlation](../../questions/logging/structured-log-correlation.html)
    — Structured logs with request correlation turn raw streams into evidence.
4. [Convert journald and Flask logs to structured JSON](../../questions/logging/structured-logging-json-format.html)
    — Converting journald and Flask output to structured JSON makes the
    correlation fields above machine-readable instead of grep-dependent.
5. [Choose fields for a log data model](../../questions/logging/log-data-model.html)
    — The data model decides what the pipeline will even be able to answer.
6. [Define a production log-level policy](../../questions/logging/log-level-policy.html)
    — The level policy keeps volume honest before the model grows unwieldy.
7. [Parse multiline exception logs safely](../../questions/logging/multiline-log-parsing.html)
    — Multiline exceptions parse safely or the model's best evidence corrupts
    itself.
8. [Handle log rotation without duplicate or missing events](../../questions/logging/rotation-and-tailers.html)
    — Rotation without duplicate or missing events keeps the stream continuous.
9. [Make log timestamps useful in incident analysis](../../questions/logging/timestamp-correctness.html)
    — Timestamps that survive incident analysis are the model's spine.
10. [Design collector buffering and backpressure](../../questions/logging/collector-buffering.html)
    — The platform tier opens with buffering and backpressure, the pipeline's
    shock absorbers.
11. [Define an SLO for a log delivery pipeline](../../questions/logging/log-pipeline-slo.html)
    — The delivery SLO promises exactly what the buffering tier made possible.
12. [Evolve a log schema without breaking consumers](../../questions/logging/schema-evolution.html)
    — Evolving the schema without breaking consumers keeps those promises across
    versions.
13. [Diagnose a slow expensive log query](../../questions/logging/log-query-performance.html)
    — The slow expensive query is the bill that poor field design writes.
14. [Select and filter log streams with LogQL](../../questions/logging/logql-stream-filtering-basics.html)
    — LogQL stream selectors and line filters are the query vocabulary the
    performance tier above is judged against.
15. [Explain Loki architecture and label design](../../questions/logging/loki-architecture-and-label-design.html)
    — The Loki pipeline and its label model explain why stream selection, not
    index tuning, drives most query cost.
16. [Prevent secrets from entering logs](../../questions/logging/secret-redaction.html)
    — The duties open with keeping secrets out of logs, which outranks any
    feature.
17. [Govern logging with privacy by design](../../questions/logging/privacy-by-design.html)
    — Privacy by design governs the whole pipeline rather than filtering at the
    end.
18. [Define a log retention policy](../../questions/logging/log-retention-policy.html)
    — Retention decides what the platform keeps and what it owes regulators.
19. [Attribute and reduce logging cost safely](../../questions/logging/log-cost-attribution.html)
    — Cost attribution prices the volume the levels and retention allowed.
20. [Isolate tenants in a shared logging platform](../../questions/logging/tenant-isolation.html)
    — Tenant isolation keeps one customer's evidence away from another's eyes.
21. [Preserve log integrity for an investigation](../../questions/logging/log-forensics-integrity.html)
    — Integrity for investigations is the duty tier's own close.
22. [Correlate trace context with logs](../../questions/logging/trace-log-correlation.html)
    — Use opens with trace context correlated back into logs.
23. [Use logs effectively during a cross-service incident](../../questions/logging/logging-incident-command.html)
    — Reading logs across services mid-incident is the use case everything above
    served.
24. [Migrate a company from fragmented logging to a common platform](../../questions/logging/logging-migration.html)
    — The strategy tier opens with migrating off fragmented logging.
25. [Define ownership boundaries for a logging service](../../questions/logging/logging-service-ownership.html)
    — Ownership boundaries decide who actually runs the platform the migration
    built.
26. [Set a platform strategy for organization-wide logging](../../questions/logging/organization-logging-platform.html)
    — The organization-wide platform decision closes the Theme at fleet scale.
27. [Compare Loki and ELK for log platform cost](../../questions/logging/loki-vs-elk-tradeoffs.html)
    — The Loki-versus-ELK cost comparison prices the two dominant log platform
    models before committing to one.
28. [Explain VictoriaMetrics next to Prometheus](../../questions/logging/victoriametrics-vs-prometheus.html)
    — The VictoriaMetrics comparison extends the build-versus-adopt decision to
    the metrics backend beside the log platform.
29. [Design Loki retention and multi-tenancy](../../questions/logging/loki-retention-and-multi-tenancy.html)
    — Retention and multi-tenancy design turns the platform choice into
    enforceable per-team data boundaries and lifetimes.
