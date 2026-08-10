"""Permanent process-resource repairs from hosted run 31375875314."""
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STALE = (
    "0pointer.net/blog/projects/journal.html",
    "jvns.ca/blog/2020/10/20/what-even-is-a-file-descriptor",
    "jvns.ca/blog/2023/08/07/group-2-environment-variables",
    "tldp.org/LDP/abs/html/signals.html",
)


def test_repaired_process_learning_urls_do_not_regress() -> None:
    text = "\n".join(path.read_text() for path in (ROOT / "questions/processes").glob("*.md"))
    assert all(url not in text for url in STALE)
