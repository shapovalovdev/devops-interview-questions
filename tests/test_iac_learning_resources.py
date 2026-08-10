from pathlib import Path


def test_iac_slice_has_learning_resources() -> None:
    for name in ("explicit-dependencies.md", "for-each-versus-count.md", "iac-change-risk-management.md", "iac-drift-governance.md"):
        assert "## What to learn next" in (Path("questions/infrastructure-as-code") / name).read_text()
