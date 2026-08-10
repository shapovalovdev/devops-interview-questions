"""Permanent logging-resource repairs from hosted run 31375875314."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STALE = (
    "grafana.com/blog/2023/06/26/how-to-migrate-to-grafana-loki",
    "www.honeycomb.io/blog/observability-pipelines",
    "www.elastic.co/blog/introducing-elastic-common-schema",
)


def test_repaired_logging_resources_do_not_regress() -> None:
    text = "\n".join(path.read_text() for path in (ROOT / "questions/logging").glob("*.md"))
    assert all(url not in text for url in STALE)
