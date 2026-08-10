from pathlib import Path


def test_iac_slice_has_learning_resources() -> None:
    for name in ("explicit-dependencies.md", "for-each-versus-count.md", "iac-change-risk-management.md", "iac-drift-governance.md", "iac-module-product-strategy.md", "iac-platform-guardrails.md", "iac-state-ownership-model.md", "import-existing-infrastructure.md", "infrastructure-drift.md", "input-variables-and-validation.md", "local-values-and-data-sources.md", "module-interface-design.md", "multi-environment-isolation.md"):
        assert "## What to learn next" in (Path("questions/infrastructure-as-code") / name).read_text()
