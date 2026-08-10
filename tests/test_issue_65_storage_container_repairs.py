"""Permanent Storage/Containers resource repairs from hosted run 31375875314."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STALE = (
    "nvmexpress.org/specification/nvm-express-over-fabrics-specification",
    "www.linux-nfs.org/",
    "www.lizrice.com/containers-from-scratch",
)


def test_repaired_storage_and_container_resources_do_not_regress() -> None:
    text = "\n".join(path.read_text() for theme in ("network-storage", "processes") for path in (ROOT / "questions" / theme).glob("*.md"))
    assert all(url not in text for url in STALE)
