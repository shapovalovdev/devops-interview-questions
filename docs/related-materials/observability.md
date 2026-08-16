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
here knows whether it is succeeding.

1. [Define an SLI and SLO for an API](../../questions/observability/define-an-sli-and-slo.html)
    — Until a target exists, nothing in the Theme knows whether it is
    succeeding.
2. [Compare metrics, logs, and traces during an incident](../../questions/observability/three-observability-signals.html)
    — The signal map compares metrics, logs, and traces during an incident.
3. [Choose a counter, gauge, histogram, or summary](../../questions/observability/describe-metric-types.html)
    — Counter versus histogram decides whether tail behaviour is measurable at
    all.
4. [Explain a metrics time series and its labels](../../questions/observability/explain-time-series-labels.html)
    — Time-series anatomy shows what the metric types actually produce.
5. [Instrument a distributed trace for an API request](../../questions/observability/instrument-a-trace.html)
    — Instrumentation begins with one request traced end to end.
6. [Design trace sampling without losing incidents](../../questions/observability/design-telemetry-sampling.html)
    — Sampling design keeps tracing affordable without losing the incidents.
7. [Diagnose missing trace context across services](../../questions/observability/propagate-trace-context.html)
    — Missing trace context is the diagnosis the sampling tier must survive, and
    the bridge that correlates context back into logs.
8. [Measure and improve tail latency](../../questions/observability/measure-tail-latency.html)
    — Measurement deepens before alerting does: tails need histograms and traces
    in place first.
9. [Design a useful service dashboard](../../questions/observability/design-a-dashboard.html)
    — Useful dashboards make the measurements readable under pressure.
10. [Combine black-box and white-box monitoring](../../questions/observability/compare-blackbox-whitebox.html)
    — Black-box against white-box chooses the vantage point per question.
11. [Use recording rules for expensive PromQL](../../questions/observability/use-recording-rules.html)
    — Recording rules make expensive PromQL affordable at query time.
12. [Control metric-label cardinality](../../questions/observability/control-metric-cardinality.html)
    — Cardinality kept under control is the budget the rules and dashboards
    spend.
13. [Build an actionable production alert](../../questions/observability/build-an-actionable-alert.html)
    — The alerting arc opens with an alert an owner can actually act on.
14. [Reduce alert fatigue without hiding risk](../../questions/observability/investigate-alert-fatigue.html)
    — Reducing alert fatigue without hiding risk keeps the alerts trusted.
15. [Explain an SLO error-budget burn-rate alert](../../questions/observability/slo-burn-rate.html)
    — The burn-rate alert closes the loop back to the opening SLO.
16. [Operate a reliable telemetry collection pipeline](../../questions/observability/operate-a-telemetry-pipeline.html)
    — The platform tier opens with pipeline reliability, the substrate
    everything rode.
17. [Debug gaps in production telemetry](../../questions/observability/debug-telemetry-gaps.html)
    — Telemetry gaps are found before they are needed, not discovered
    mid-incident.
18. [Validate telemetry data quality after a release](../../questions/observability/validate-telemetry-data-quality.html)
    — Data-quality validation catches the release that silently broke the
    pipeline.
19. [Set telemetry retention and query-cost controls](../../questions/observability/set-observability-retention.html)
    — Retention and query-cost controls price the history the platform keeps.
20. [Govern telemetry cost across teams](../../questions/observability/govern-telemetry-cost.html)
    — Cost governance spends the retention decisions across every team.
21. [Design multi-tenant observability boundaries](../../questions/observability/design-multitenant-observability.html)
    — Tenant boundaries keep one team's data out of another's console.
22. [Design an incident evidence strategy](../../questions/observability/design-incident-evidence.html)
    — The evidence strategy makes incidents investigable after the fact.
23. [Investigate a failed request with Cilium Hubble](../../questions/observability/cilium-hubble-flow-observation.html)
    — Hubble covers the network blind spot the signal map left open.
24. [Establish an observability platform product](../../questions/observability/establish-observability-platform.html)
    — The observability platform as a product is the tier's synthesis.
25. [Govern an organization-wide SLO program](../../questions/observability/govern-an-slo-program.html)
    — The organization-wide SLO program is the Theme's close.
