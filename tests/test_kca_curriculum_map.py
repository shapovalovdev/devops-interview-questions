"""Guard the public KCA map and its Kyverno-specific coverage gaps."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "docs" / "certifications" / "kca.md"
QUESTION_PATHS = [
    ROOT / "questions/kubernetes/kyverno-policy-engine-basics.md",
    ROOT / "questions/kubernetes/kyverno-installation-upgrade-safety.md",
    ROOT / "questions/kubernetes/kyverno-cli-policy-ci.md",
    ROOT / "questions/kubernetes/kyverno-enforcement-and-policy-reports.md",
    ROOT / "questions/kubernetes/kyverno-policy-authoring-design.md",
    ROOT / "questions/kubernetes/kyverno-policy-lifecycle-governance.md",
]


def main() -> None:
    text = MAP.read_text(encoding="utf-8")
    required = [
        "https://github.com/cncf/curriculum/tree/master/kca",
        "https://www.cncf.io/training/certification/kca/",
        "reviewed on 2026-08-06",
        "not** a\nreproduction of exam questions",
        "Fundamentals of Kyverno | 18%",
        "Installation, Configuration, and Upgrades | 18%",
        "Kyverno CLI | 12%",
        "Applying Policies | 10%",
        "Writing Policies | 32%",
        "Policy Management | 10%",
        "Central publication gate",
        "`kca`",
    ]
    missing = [item for item in required if item not in text]
    assert not missing, f"KCA curriculum map is missing: {', '.join(missing)}"
    print("Validated public KCA curriculum map and explicit Kyverno gap policy.")


def test_kca_gap_questions_are_source_verified_and_ready_for_central_integration() -> None:
    """All six official domains need original, source-backed canonical Questions."""
    map_text = MAP.read_text(encoding="utf-8")
    for path in QUESTION_PATHS:
        assert path.is_file(), f"missing KCA gap Question: {path}"
        text = path.read_text(encoding="utf-8")
        assert "theme: kubernetes" in text
        assert "kyverno" in text and "kca" in text
        assert "sources:" in text and "source_type: official-docs" in text
        assert "## Answer guide" in text and "## References" in text
        assert "Further reading (blog):" in text
        assert "## What to learn next" in text
        assert text.count("https://") >= 6, f"{path}: needs primary and learning resources"
        assert path.name in map_text, f"{path}: must be linked by the KCA map"


if __name__ == "__main__":
    main()
