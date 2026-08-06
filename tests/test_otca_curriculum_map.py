"""Guard the public OTCA curriculum map without reproducing exam material."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "docs" / "certifications" / "otca.md"
QUESTION_PATHS = [
    ROOT / "questions/observability/three-observability-signals.md",
    ROOT / "questions/observability/establish-observability-platform.md",
    ROOT / "questions/observability/validate-telemetry-data-quality.md",
    ROOT / "questions/logging/log-data-model.md",
    ROOT / "questions/observability/instrument-a-trace.md",
    ROOT / "questions/observability/propagate-trace-context.md",
    ROOT / "questions/observability/design-telemetry-sampling.md",
    ROOT / "questions/observability/control-metric-cardinality.md",
    ROOT / "questions/logging/structured-log-correlation.md",
    ROOT / "questions/observability/operate-a-telemetry-pipeline.md",
    ROOT / "questions/observability/debug-telemetry-gaps.md",
    ROOT / "questions/logging/kubernetes-log-enrichment.md",
    ROOT / "questions/logging/collector-buffering.md",
    ROOT / "questions/logging/log-pipeline-slo.md",
    ROOT / "questions/logging/schema-evolution.md",
    ROOT / "questions/logging/trace-log-correlation.md",
]


def main() -> None:
    text = MAP.read_text(encoding="utf-8")
    required = [
        "https://training.linuxfoundation.org/certification/opentelemetry-certified-associate-otca/",
        "https://github.com/cncf/curriculum/tree/master/otca",
        "reviewed on 2026-08-06",
        "not** a\nreproduction of exam questions",
        "Fundamentals of Observability: telemetry data",
        "| 18% |",
        "The OpenTelemetry API and SDK: data model",
        "| 46% |",
        "The OpenTelemetry Collector: configuration",
        "| 26% |",
        "Maintaining and Debugging Observability Pipelines: context propagation",
        "| 10% |",
        "No new Question is added in this pass.",
        "Atomic central integration handoff",
        "`otca`",
    ]
    missing = [item for item in required if item not in text]
    assert not missing, f"OTCA curriculum map is missing: {', '.join(missing)}"
    print("Validated public OTCA curriculum map and no-duplicate gap decision.")


def test_otca_mapped_questions_are_source_verified_before_central_tagging() -> None:
    """Each mapped canonical Question must be ready for an OTCA tag review."""
    map_text = MAP.read_text(encoding="utf-8")
    for path in QUESTION_PATHS:
        assert path.is_file(), f"missing OTCA-mapped Question: {path}"
        text = path.read_text(encoding="utf-8")
        assert "sources:" in text, f"{path}: missing structured source metadata"
        assert "source_type:" in text, f"{path}: missing source type"
        assert "verified_on:" in text, f"{path}: missing verification date"
        assert "## Answer guide" in text and "## References" in text
        assert "Further reading (blog):" in text, f"{path}: missing complementary blog"
        assert path.name in map_text, f"{path}: must be linked by the OTCA map"


if __name__ == "__main__":
    main()
