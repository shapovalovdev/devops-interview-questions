"""Validate every active Question against the repository content manifest."""

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
MANIFEST = ROOT / "config" / "content-manifest.json"
ALLOWED_DIFFICULTIES = {"junior", "middle", "senior", "staff"}
ALLOWED_TYPES = {"theory", "scenario", "troubleshooting"}


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def front_matter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "---", f"{path}: front matter must begin with ---"
    end = lines.index("---", 1)
    fields = {}
    for line in lines[1:end]:
        if not line or ": " not in line or line.startswith("  - ") or line.startswith("    "):
            continue
        key, value = line.split(": ", 1)
        fields[key] = value
    return fields


def primary_source_urls(content: str, path: Path) -> set[str]:
    """Return declared source URLs while enforcing complete source records.

    The intentionally small front-matter parser above reads scalar Question
    fields.  Source records are a YAML list, so validate them separately rather
    than accidentally treating a URL from an incomplete record as verified.
    """
    source_block = re.search(r"^sources:\n([\s\S]*?)(?=^[A-Za-z][\w-]*:|^---$)", content, re.MULTILINE)
    assert source_block, f"{path}: missing primary source metadata"
    records = re.findall(
        r"^  - url: (https://[^\s]+)\n"
        r"    source_type: (standard|official-docs|official-api)\n"
        r"    verified_on: (\d{4}-\d{2}-\d{2})$",
        source_block.group(1),
        re.MULTILINE,
    )
    assert records, f"{path}: every primary source requires URL, approved type, and ISO review date"
    return {url for url, _, _ in records}


def known_tags() -> set[str]:
    text = (ROOT / "TAGS.md").read_text(encoding="utf-8")
    return set(re.findall(r"`([a-z0-9-]+)`", text))


def certification_tags() -> set[str]:
    text = (ROOT / "TAGS.md").read_text(encoding="utf-8")
    section = text.split("## Certifications", 1)[-1]
    return set(re.findall(r"`([a-z0-9-]+)`", section))


def catalog_paths() -> list[str]:
    text = (ROOT / "assets/questions.js").read_text(encoding="utf-8")
    return re.findall(r'"?path"?\s*:\s*"([^"]+)"', text)


def roadmap_themes() -> set[str]:
    text = (ROOT / "ROADMAP_COVERAGE.md").read_text(encoding="utf-8")
    return set(re.findall(r"\|[^\n|]+\|\s*`([^`]+)`\s*\|", text))


def validate_question(path: Path, tags: set[str]) -> tuple[dict[str, str], set[str]]:
    fields = front_matter(path)
    required = {"title", "theme", "difficulty", "type", "tags"}
    assert required <= fields.keys(), f"{path}: missing required front-matter fields"
    assert fields["theme"] == path.parent.name, f"{path}: theme must match canonical folder"
    assert fields["difficulty"] in ALLOWED_DIFFICULTIES, f"{path}: invalid difficulty"
    assert fields["type"] in ALLOWED_TYPES, f"{path}: invalid Question type"
    question_tags = set(re.findall(r"[a-z0-9-]+", fields["tags"]))
    assert question_tags, f"{path}: requires at least one Tag"
    assert question_tags <= tags, f"{path}: uses a Tag missing from TAGS.md"

    content = path.read_text(encoding="utf-8")
    assert "## Answer guide" in content, f"{path}: missing answer guide"
    answer = content.split("## Answer guide", 1)[1].split("## References", 1)[0]
    answer_words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", answer)
    assert len(answer_words) >= 60, f"{path}: answer guide is too short for a full answer"
    assert len(re.findall(r"^- ", answer, re.MULTILINE)) >= 3, f"{path}: answer guide requires direct answer, constraints, and operational guidance"
    sources = primary_source_urls(content, path)
    assert "## References" in content, f"{path}: missing References section"
    assert re.search(r"^- \[.*\]\(https://", content, re.MULTILINE), f"{path}: requires a primary reference"
    assert re.search(r"^- Further reading \(blog\): .*\(https://", content, re.MULTILINE), f"{path}: requires a labeled complementary blog post"
    references = content.split("## References", 1)[1].split("## What to learn next", 1)[0]
    reference_urls = set(re.findall(r"\]\((https://[^)\s]+)\)", references))
    missing_primary_references = sources - reference_urls
    assert not missing_primary_references, (
        f"{path}: every declared primary source must appear in References; missing "
        f"{sorted(missing_primary_references)}"
    )
    return fields, question_tags


def main() -> None:
    manifest = load_manifest()
    policy = manifest["theme_policy"]
    target = policy["target_question_count"]
    expected_distribution = policy["difficulty_distribution"]
    theme_by_name = {theme["name"]: theme for theme in manifest["themes"]}
    certifications = {certification["tag"]: certification for certification in manifest["certifications"]}
    question_files = sorted(QUESTIONS.glob("*/*.md"))
    assert question_files, "No active Questions found"
    tags = known_tags()
    catalog = catalog_paths()
    assert len(catalog) == len(set(catalog)), "Website catalog contains duplicate paths"
    assert certification_tags() == set(certifications), "TAGS.md certification tags must exactly match the content manifest"
    assert roadmap_themes() <= set(theme_by_name), "Every ROADMAP_COVERAGE Theme must be declared in the content manifest"

    actual_directories = {path.name for path in QUESTIONS.iterdir() if path.is_dir()}
    assert actual_directories <= set(theme_by_name), "Every Question folder must be declared in the content manifest"

    expected_catalog = set()
    difficulties = {name: Counter() for name in theme_by_name}
    certification_counts = Counter()
    for path in question_files:
        fields, question_tags = validate_question(path, tags)
        theme = fields["theme"]
        assert theme in theme_by_name, f"{path}: undeclared canonical Theme {theme}"
        assert theme_by_name[theme]["state"] != "planned", f"{path}: planned Themes cannot contain active Questions"
        difficulties[theme][fields["difficulty"]] += 1
        certification_counts.update(question_tags & set(certifications))
        expected_catalog.add(path.relative_to(ROOT).with_suffix(".html").as_posix())

    assert set(catalog) == expected_catalog, "Website catalog must contain every active Question exactly once"
    for name, theme in theme_by_name.items():
        counts = difficulties[name]
        total = sum(counts.values())
        if theme["state"] == "complete":
            assert total == target, f"{name} must contain exactly {target} Questions, got {total}"
            assert dict(counts) == expected_distribution, f"{name} must contain {expected_distribution}, got {dict(counts)}"
        elif theme["state"] == "in-progress":
            assert total > 0, f"{name} is in-progress but has no active Questions"
            # In-progress Themes may contain additive certification coverage. The
            # canonical 25-question core is still tracked by the Theme issue;
            # extensions remain visible instead of being discarded to satisfy a
            # superficial count cap.
        else:
            assert total == 0, f"{name} is planned but already contains active Questions"

    advanced_runtime_tags = {"cgroups", "pid-1", "namespaces", "process-isolation", "capabilities", "seccomp", "rootless", "filesystem"}
    advanced_questions = "\n".join(
        path.read_text(encoding="utf-8") for path in QUESTIONS.joinpath("advanced-containers").glob("*.md")
    )
    for tag in advanced_runtime_tags:
        assert re.search(rf"tags: \[[^\]]*\b{re.escape(tag)}\b", advanced_questions), (
            f"advanced-containers must explicitly cover {tag}"
        )

    for tag, certification in certifications.items():
        assert tag in tags, f"{tag} certification tag must be documented in TAGS.md"
        assert (ROOT / certification["map"]).is_file(), f"{tag} certification map is required"
        minimum = certification["minimum_questions"]
        assert certification_counts[tag] >= minimum, (
            f"{tag} requires at least {minimum} mapped Questions, got {certification_counts[tag]}"
        )
    print(f"Validated {len(question_files)} active Questions and {len(catalog)} website records.")


if __name__ == "__main__":
    main()
