# PCA coverage map

This map aligns original practice Questions with the current [Prometheus Certified
Associate (PCA) curriculum](https://training.linuxfoundation.org/certification/prometheus-certified-associate/)
and the [CNCF PCA curriculum](https://github.com/cncf/curriculum/tree/master/pca).
It is a study map, not a reproduction of real, confidential, or leaked exam content.
The Linux Foundation curriculum was reviewed on 2026-08-06. It listed PCA as a
beginner certification and the five domains below; check the official page before
studying because curriculum and product behavior can change.

Every mapped Question is original, carries the canonical `pca` tag, has a full
answer guide, structured primary-source metadata, and a separately labelled
complementary technical blog post. The map deliberately reuses canonical files
instead of copying fundamentals into a PCA-only folder.

| Official domain | Weight | Canonical practice Questions tagged `pca` |
| --- | ---: | --- |
| Observability Concepts | 18% | [Compare metrics, logs, and traces during an incident](../../questions/observability/three-observability-signals.md); [Choose useful application log levels](../../questions/observability/choose-log-levels.md); [Instrument a distributed trace for an API request](../../questions/observability/instrument-a-trace.md); [Explain a metrics time series and its labels](../../questions/observability/explain-time-series-labels.md); [Define an SLI and SLO for an API](../../questions/observability/define-an-sli-and-slo.md) |
| Prometheus Fundamentals | 20% | [Explain a metrics time series and its labels](../../questions/observability/explain-time-series-labels.md); [Control metric-label cardinality](../../questions/observability/control-metric-cardinality.md); [Operate a reliable telemetry collection pipeline](../../questions/observability/operate-a-telemetry-pipeline.md); [Debug gaps in production telemetry](../../questions/observability/debug-telemetry-gaps.md); [Validate telemetry data quality after a release](../../questions/observability/validate-telemetry-data-quality.md) |
| PromQL | 28% | [Use recording rules for expensive PromQL](../../questions/observability/use-recording-rules.md); [Choose a counter, gauge, histogram, or summary](../../questions/observability/describe-metric-types.md); [Measure and improve tail latency](../../questions/observability/measure-tail-latency.md); [Control metric-label cardinality](../../questions/observability/control-metric-cardinality.md); [Set telemetry retention and query-cost controls](../../questions/observability/set-observability-retention.md) |
| Instrumentation and Exporters | 16% | [Choose a counter, gauge, histogram, or summary](../../questions/observability/describe-metric-types.md); [Control metric-label cardinality](../../questions/observability/control-metric-cardinality.md); [Operate a reliable telemetry collection pipeline](../../questions/observability/operate-a-telemetry-pipeline.md); [Debug gaps in production telemetry](../../questions/observability/debug-telemetry-gaps.md); [Establish an observability platform product](../../questions/observability/establish-observability-platform.md) |
| Alerting and Dashboarding | 18% | [Build an actionable production alert](../../questions/observability/build-an-actionable-alert.md); [Reduce alert fatigue without hiding risk](../../questions/observability/investigate-alert-fatigue.md); [Explain an SLO error-budget burn-rate alert](../../questions/observability/slo-burn-rate.md); [Design a useful service dashboard](../../questions/observability/design-a-dashboard.md); [Govern an organization-wide SLO program](../../questions/observability/govern-an-slo-program.md) |

The remaining tagged Questions provide cross-domain practice for production
evidence, multi-tenancy, telemetry sampling, trace context, cost governance,
and operating-model trade-offs. They are intentionally supplementary rather
than a claim that the PCA exam contains those exact prompts.
