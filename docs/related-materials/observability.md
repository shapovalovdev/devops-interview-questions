# Observability related materials

These resources complement the Observability Theme's Question-level references.
They are a curated starting point for metrics and PromQL, service level
objectives and alerting, distributed tracing, and telemetry collection
pipelines; check each one against the collection agent, storage backend, and
query language actually in use before applying its advice.

## What to learn next

- Official documentation: [Prometheus documentation](https://prometheus.io/docs/introduction/overview/)
- Manual or specification: [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/)
- Maintainer or personal blog: [Brian Brazil — Robust Perception monitoring blog](https://www.robustperception.io/blog/)
- Technical blog: [Grafana Labs engineering blog](https://grafana.com/blog/)
- Hands-on guide: [OpenTelemetry Demo application](https://opentelemetry.io/docs/demo/)

## Suggested study order

Define an SLI and an SLO before touching a tool: until a target exists, nothing
here knows whether it is succeeding. The signal map follows — metrics, logs,
and traces compared during an incident — then metric types and time-series
anatomy, because counter-versus-histogram decides whether tail behaviour is
measurable at all. Instrumentation comes third: a distributed trace for one
request, sampling design, the missing-trace-context diagnosis, and trace
context correlated back into logs. Measurement deepens before alerting does:
tail latency, useful dashboards, black-box against white-box, recording rules
for expensive PromQL, and cardinality kept under control. With signals and
measurements in hand, take the alerting arc — building an actionable alert,
reducing fatigue without hiding risk, and the burn-rate alert that closes the
loop back to the opening SLO. The platform tier is last: pipeline reliability,
telemetry gaps and data-quality validation, retention and query-cost controls,
cost governance, tenant boundaries, incident evidence strategy, Hubble for the
network blind spot, the observability platform as a product, and the
organization-wide SLO program.
