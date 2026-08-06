# OTCA coverage map

This map aligns original canonical practice Questions with the public
[OpenTelemetry Certified Associate (OTCA) program page](https://training.linuxfoundation.org/certification/opentelemetry-certified-associate-otca/)
and the CNCF's public [OTCA curriculum outline](https://github.com/cncf/curriculum/tree/master/otca).
Both sources were reviewed on 2026-08-06. This is a study map, **not** a
reproduction of exam questions, confidential material, leaked content, or a
promise of exam coverage. Check the Linux Foundation program page before using
the map: it is the current public authority for exam domains and weights.

The current Linux Foundation page publishes four domains: Fundamentals of
Observability (18%), the OpenTelemetry API and SDK (46%), the OpenTelemetry
Collector (26%), and Maintaining and Debugging Observability Pipelines (10%).
The CNCF repository's public OTCA outline presents the same subject area as
five equal topical groupings (Fundamentals, Instrumentation & SDKs, Metrics,
Traces, and Logs & Exporters). This map uses the current four-domain weighting
while making each of those five topical areas discoverable through the linked
canonical Questions.

Every linked Question is an original learning prompt. Its own Markdown file,
not this certification map, provides its answer guide, primary-source metadata,
and complementary technical blog reading. Questions remain in their canonical
`observability` or `logging` Theme so the database does not duplicate material
into an OTCA-only folder.

## Official domain mapping

| Current official domain and published competencies | Weight | Canonical original practice Questions | Coverage decision |
| --- | ---: | --- | --- |
| Fundamentals of Observability: telemetry data, semantic conventions, instrumentation, analysis and outcomes | 18% | [Compare metrics, logs, and traces during an incident](../../questions/observability/three-observability-signals.md); [Establish an observability platform product](../../questions/observability/establish-observability-platform.md); [Validate telemetry data quality after a release](../../questions/observability/validate-telemetry-data-quality.md); [Choose fields for a log data model](../../questions/logging/log-data-model.md) | Covered by shared signal, semantic-convention, instrumentation-contract, and outcome-validation Questions. |
| The OpenTelemetry API and SDK: data model; composability and extension; configuration; tracing, metrics, and logs; SDK pipelines; context propagation; agents | 46% | [Instrument a distributed trace for an API request](../../questions/observability/instrument-a-trace.md); [Diagnose missing trace context across services](../../questions/observability/propagate-trace-context.md); [Design trace sampling without losing incidents](../../questions/observability/design-telemetry-sampling.md); [Control metric-label cardinality](../../questions/observability/control-metric-cardinality.md); [Choose fields for a log data model](../../questions/logging/log-data-model.md); [Design structured logs for request correlation](../../questions/logging/structured-log-correlation.md) | Covered across the three signals. The Questions deliberately distinguish data-model contracts, bounded metric dimensions, SDK instrumentation, propagation, sampling, and correlation instead of inventing language-specific exam prompts. |
| The OpenTelemetry Collector: configuration, deployment, scaling, pipelines, and transforming data | 26% | [Operate a reliable telemetry collection pipeline](../../questions/observability/operate-a-telemetry-pipeline.md); [Debug gaps in production telemetry](../../questions/observability/debug-telemetry-gaps.md); [Enrich Kubernetes logs without destroying provenance](../../questions/logging/kubernetes-log-enrichment.md); [Design collector buffering and backpressure](../../questions/logging/collector-buffering.md); [Define an SLO for a log delivery pipeline](../../questions/logging/log-pipeline-slo.md) | Covered by canonical pipeline, resiliency, resource-enrichment, buffering, and operational-SLO Questions. Product-specific deployment commands are intentionally excluded because the program map is not an exam reconstruction. |
| Maintaining and Debugging Observability Pipelines: context propagation, debugging pipelines, error handling, and schema management | 10% | [Diagnose missing trace context across services](../../questions/observability/propagate-trace-context.md); [Debug gaps in production telemetry](../../questions/observability/debug-telemetry-gaps.md); [Evolve a log schema without breaking consumers](../../questions/logging/schema-evolution.md); [Correlate trace context with logs](../../questions/logging/trace-log-correlation.md); [Define an SLO for a log delivery pipeline](../../questions/logging/log-pipeline-slo.md) | Covered by shared diagnostic, error-boundary, schema-compatibility, correlation, and delivery-evidence Questions. |

## Gap decision

No new Question is added in this pass. The public OTCA competencies are already
covered at useful operational depth by the canonical Questions above. Adding an
OTCA-only prompt for an SDK, collector, metric, trace, or log topic would repeat
an existing Question rather than close a genuine gap. This decision should be
revisited if the public curriculum adds a distinct competency that is not
represented by the linked material.

## Focused verification plan and evidence

`tests/test_otca_curriculum_map.py` provides a narrow regression gate for this
map. It verifies the two official curriculum URLs, the current four-domain
weights, the explicit no-exam-material statement, and that every mapped
canonical Markdown file exists and carries structured primary-source metadata,
an answer guide, references, and a labelled complementary blog. The test also
requires every mapped filename to be linked by this document.

The focused check was run locally with:

```sh
python tests/test_otca_curriculum_map.py
```

The coordinator must run the repository-wide content validator and site check,
then use GitHub Actions as the final publication gate.

## Atomic central integration handoff

Do not expose an OTCA study filter until these shared changes are made together:

1. Add `otca` to the certification vocabulary in `TAGS.md`.
2. Add `{"tag": "otca", "map": "docs/certifications/otca.md", "minimum_questions": 16}` to `config/content-manifest.json`.
3. Apply the `otca` tag only to the 16 canonical Questions linked above after a
   final source-quality review; do not tag a file merely because it is in the
   `observability` or `logging` Theme.
4. Regenerate `assets/questions.js` so each tagged Markdown Question appears
   exactly once as a Pages-rendered `.html` catalog record.
5. Run the focused map check, the full validator, `tests/site_check.py`, and
   successful GitHub Actions before closing the issue.

This preserves the one-canonical-Question policy and prevents the public site
from overstating OTCA study coverage.
