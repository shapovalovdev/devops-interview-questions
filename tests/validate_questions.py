import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
ALLOWED_DIFFICULTIES = {"junior", "middle", "senior", "staff"}
ALLOWED_TYPES = {"theory", "scenario", "troubleshooting"}


def front_matter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "---", f"{path}: front matter must begin with ---"
    end = lines.index("---", 1)
    fields = {}
    for line in lines[1:end]:
        if not line or line.startswith("  - ") or line.startswith("    "):
            continue
        key, value = line.split(": ", 1)
        fields[key] = value
    return fields


def known_tags() -> set[str]:
    text = (ROOT / "TAGS.md").read_text(encoding="utf-8")
    return set(re.findall(r"`([a-z0-9-]+)`", text))


def catalog_paths() -> list[str]:
    text = (ROOT / "assets/questions.js").read_text(encoding="utf-8")
    return re.findall(r'path: "([^"]+)"', text)


def main() -> None:
    question_files = sorted(QUESTIONS.glob("*/*.md"))
    assert question_files, "No active Questions found"
    tags = known_tags()
    catalog = catalog_paths()
    assert len(catalog) == len(set(catalog)), "Website catalog contains duplicate paths"

    expected_catalog = set()
    for path in question_files:
        fields = front_matter(path)
        required = {"title", "theme", "difficulty", "type", "tags"}
        assert required <= fields.keys(), f"{path}: missing required front-matter fields"
        assert fields["theme"] == path.parent.name, f"{path}: theme must match canonical folder"
        assert fields["difficulty"] in ALLOWED_DIFFICULTIES, f"{path}: invalid difficulty"
        assert fields["type"] in ALLOWED_TYPES, f"{path}: invalid Question type"
        question_tags = re.findall(r"[a-z0-9-]+", fields["tags"])
        assert question_tags, f"{path}: requires at least one Tag"
        assert set(question_tags) <= tags, f"{path}: uses a Tag missing from TAGS.md"
        assert "## Answer guide" in path.read_text(encoding="utf-8"), f"{path}: missing answer guide"
        expected_catalog.add(path.relative_to(ROOT).with_suffix(".html").as_posix())

    assert set(catalog) == expected_catalog, "Website catalog must contain every active Question exactly once"
    print(f"Validated {len(question_files)} active Questions and {len(catalog)} website records.")


if __name__ == "__main__":
    main()
