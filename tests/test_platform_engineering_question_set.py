"""Focused acceptance checks for GitHub issue #80's platform-engineering Questions."""

import json
import re
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from theme_expectations import assert_meets_floor  # noqa: E402
from validate_learning_resources import load_manifest, resource_links  # noqa: E402
from validate_questions import known_tags, validate_question  # noqa: E402

THEME = "platform-engineering"
QUESTIONS = ROOT / "questions" / THEME

# Questions in neighbouring Themes that already own this ground. The
# platform-engineering Theme is allowed to reference them but must not restate
# them, so their exact prompts are reserved.
RESERVED_NEIGHBOUR_QUESTIONS = (
    "questions/backend-architecture/developer-portal-catalog-contract.md",
    "questions/backend-architecture/platform-boundary-strategy.md",
    "questions/sre/measure-platform-impact-with-dora.md",
    "questions/sre/define-sre-engagement-model.md",
)


def titles(paths) -> list[str]:
    found = []
    for path in paths:
        match = re.search(r"^title: (.+)$", Path(path).read_text(encoding="utf-8"), re.MULTILINE)
        assert match, f"{path}: missing title"
        found.append(match.group(1).strip())
    return found


def prompts(paths) -> list[str]:
    """Return the interrogative line that follows each Question's H1."""
    found = []
    for path in paths:
        text = Path(path).read_text(encoding="utf-8")
        body = text.split("\n# ", 1)[1].split("## Answer guide", 1)[0]
        prompt = " ".join(line.strip() for line in body.splitlines()[1:] if line.strip())
        assert prompt, f"{path}: missing Question prompt"
        found.append(prompt)
    return found


def test_platform_engineering_set_is_complete_and_source_verified() -> None:
    tags = known_tags()
    counts: Counter = Counter()
    for question in sorted(QUESTIONS.glob("*.md")):
        fields, _ = validate_question(question, tags)
        assert fields["theme"] == THEME
        counts[fields["difficulty"]] += 1
        assert len(resource_links(question.read_text(encoding="utf-8"), str(question))) == 5
    assert_meets_floor(THEME, counts)


def test_platform_engineering_related_materials_has_five_curated_links() -> None:
    related = ROOT / "docs" / "related-materials" / f"{THEME}.md"
    assert len(resource_links(related.read_text(encoding="utf-8"), str(related))) == 5


def test_every_platform_engineering_question_is_registered_for_the_link_audit() -> None:
    audited = {
        item["question"]
        for item in load_manifest()["audited_questions"]
        if item["question"].startswith(f"questions/{THEME}/")
    }
    expected = {path.relative_to(ROOT).as_posix() for path in QUESTIONS.glob("*.md")}
    assert audited == expected, f"{THEME}: link-audit manifest is out of step with the Question folder"


def test_platform_engineering_is_declared_complete_and_registered_in_the_catalog() -> None:
    manifest = json.loads((ROOT / "config" / "content-manifest.json").read_text(encoding="utf-8"))
    states = {theme["name"]: theme["state"] for theme in manifest["themes"]}
    assert states[THEME] == "complete", f"{THEME} must be declared complete once it meets the floor"

    catalog = (ROOT / "assets" / "questions.js").read_text(encoding="utf-8")
    for path in sorted(QUESTIONS.glob("*.md")):
        entry = path.relative_to(ROOT).with_suffix(".html").as_posix()
        assert f'"path": "{entry}"' in catalog, f"{entry} is missing from the website catalog"

    roadmap = (ROOT / "ROADMAP_COVERAGE.md").read_text(encoding="utf-8")
    assert f"`{THEME}`" in roadmap, f"{THEME} must appear in the roadmap coverage map"


def test_platform_engineering_covers_the_required_platform_decisions() -> None:
    """The numeric floor can be reached while covering only the easy half.

    Platform engineering interviews probe a specific set of decisions, so pin
    them: the paved road and its guardrails, the platform's product framing and
    its interface contract, the operational promises, and the organizational
    judgement calls that separate a senior answer from a staff one.
    """
    corpus = "\n".join(path.read_text(encoding="utf-8").lower() for path in sorted(QUESTIONS.glob("*.md")))
    for concept in (
        "paved road",
        "golden path",
        "guardrail",
        "escape hatch",
        "self-service",
        "safe defaults",
        "cognitive load",
        "deprecation",
        "error budget",
        "noisy neighbour",
        "blast radius",
        "build versus buy",
        "total cost of ownership",
        "toil",
        "voluntary",
        "mandate",
    ):
        assert concept in corpus, f"{THEME} does not cover {concept}"


def test_platform_engineering_does_not_restate_neighbouring_theme_questions() -> None:
    """The Theme must not duplicate the platform Questions that already exist.

    `backend-architecture` already owns the developer-portal catalog contract
    and the platform/product-service boundary, and `sre` already owns DORA-based
    platform impact measurement and the SRE engagement model. Restating any of
    them would publish two Questions with the same prompt on the same site.
    """
    for relative in RESERVED_NEIGHBOUR_QUESTIONS:
        assert (ROOT / relative).is_file(), f"reserved neighbour Question moved: {relative}"

    neighbours = {"sre", "backend-architecture", "chaos-engineering", "testing-strategy"}
    reserved_titles = set()
    for theme in neighbours:
        reserved_titles.update(titles(sorted((ROOT / "questions" / theme).glob("*.md"))))
    reserved_prompts = set(prompts(ROOT / relative for relative in RESERVED_NEIGHBOUR_QUESTIONS))

    mine = sorted(QUESTIONS.glob("*.md"))
    my_titles = titles(mine)
    my_prompts = prompts(mine)

    overlap = set(my_titles) & reserved_titles
    assert not overlap, f"{THEME} restates a neighbouring Theme's Question: {sorted(overlap)}"
    assert not set(my_prompts) & reserved_prompts, f"{THEME} restates a reserved neighbour prompt"
    assert len(set(my_titles)) == len(my_titles), f"{THEME}: duplicate Question titles"
    assert len(set(my_prompts)) == len(my_prompts), f"{THEME}: duplicate Question prompts"
