"""Guard the reusable certification-question workflow against accidental regression."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "certification-question-workflow" / "SKILL.md"
EVALS = ROOT / "skills" / "certification-question-workflow" / "evals" / "evals.json"
ISSUE_TEMPLATE = ROOT / "skills" / "certification-question-workflow" / "references" / "issue-template.md"


def main() -> None:
    assert SKILL.is_file(), "certification workflow skill is required"
    assert EVALS.is_file(), "certification workflow evals are required"
    assert ISSUE_TEMPLATE.is_file(), "certification issue template is required"

    text = SKILL.read_text(encoding="utf-8")
    required = [
        "name: certification-question-workflow",
        "official curriculum",
        "canonical Theme",
        "original practice Questions",
        "question-verifier",
        "complementary technical blog post",
        "assets/questions.js",
        "tests/validate_questions.py",
        "GitHub Actions",
        "Close the issue only",
    ]
    missing = [phrase for phrase in required if phrase not in text]
    assert not missing, f"certification workflow is missing: {', '.join(missing)}"
    assert "confidential" in text and "never reproduces" in text, "exam-content safeguard is required"
    assert '"evals"' in EVALS.read_text(encoding="utf-8"), "workflow needs realistic eval prompts"
    print("Validated certification-question-workflow skill, issue template, and eval prompts.")


if __name__ == "__main__":
    main()
