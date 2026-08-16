#!/usr/bin/env python3
"""Generate the static GitHub Pages Question catalog from Markdown front matter."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
CATALOG = ROOT / "assets" / "questions.js"
MANIFEST = ROOT / "config" / "content-manifest.json"
LEARNING_PATHS = ROOT / "config" / "learning-paths.json"
STUDY_ORDERS = ROOT / "config" / "study-orders.json"


def front_matter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "---", f"{path}: front matter must begin with ---"
    end = lines.index("---", 1)
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key] = value
    return fields


def learning_paths() -> list[dict]:
    """Resolve `config/learning-paths.json` into ordered, renderable steps.

    Ordering belongs to the path, not to the Question, so a step is resolved
    here rather than read from Question front matter.  The rendered link is
    published as `href` on purpose: `path` is the Question catalog's own key and
    reusing it would make a step look like a duplicate Question record.
    """
    declaration = json.loads(LEARNING_PATHS.read_text(encoding="utf-8"))
    resolved = []
    for path in declaration["paths"]:
        steps = []
        for step in path["steps"]:
            source = ROOT / step["question"]
            assert source.is_file(), f"{path['slug']}: missing Question {step['question']}"
            fields = front_matter(source)
            steps.append(
                {
                    "title": fields["title"],
                    "theme": fields["theme"],
                    "difficulty": fields["difficulty"],
                    "href": source.relative_to(ROOT).with_suffix(".html").as_posix(),
                    "why": step["why"],
                }
            )
        resolved.append(
            {
                "slug": path["slug"],
                "title": path["title"],
                "audience": path["audience"],
                "prerequisites": path["prerequisites"],
                "steps": steps,
            }
        )
    return resolved


def study_orders() -> list[dict]:
    """Resolve `config/study-orders.json` into ordered, renderable steps.

    A study order is the within-Theme sequence, so it is published per Theme
    beside the cross-Theme `learningPaths`.  Steps resolve to catalog records
    the same way path steps do: the manifest owns the order, the Question owns
    the metadata, and the rendered link is `href` to avoid colliding with the
    catalog's `path` key.
    """
    declaration = json.loads(STUDY_ORDERS.read_text(encoding="utf-8"))
    resolved = []
    for theme in declaration["themes"]:
        steps = []
        for step in theme["steps"]:
            source = ROOT / step["question"]
            assert source.is_file(), f"{theme['theme']}: missing Question {step['question']}"
            fields = front_matter(source)
            steps.append(
                {
                    "title": fields["title"],
                    "theme": fields["theme"],
                    "difficulty": fields["difficulty"],
                    "href": source.relative_to(ROOT).with_suffix(".html").as_posix(),
                    "why": step["why"],
                }
            )
        resolved.append(
            {
                "theme": theme["theme"],
                "note": theme["note"],
                "steps": steps,
            }
        )
    return resolved


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = []
    for path in sorted(QUESTIONS.glob("*/*.md")):
        fields = front_matter(path)
        tags = re.findall(r"[a-z0-9-]+", fields["tags"])
        records.append(
            {
                "title": fields["title"],
                "theme": fields["theme"],
                "difficulty": fields["difficulty"],
                "type": fields["type"],
                "tags": tags,
                "path": path.relative_to(ROOT).with_suffix(".html").as_posix(),
            }
        )

    lines = ["window.questions = ["]
    for record in records:
        lines.append(f"  {json.dumps(record, ensure_ascii=False)},")
    lines.append("];\n")
    lines.append("window.certifications = [")
    for certification in manifest["certifications"]:
        lines.append(
            "  "
            + json.dumps(
                {
                    "tag": certification["tag"],
                    "map": certification["map"],
                    "minimumQuestions": certification["minimum_questions"],
                },
                ensure_ascii=False,
            )
            + ","
        )
    lines.append("];\n")
    paths = learning_paths()
    lines.append("window.learningPaths = " + json.dumps(paths, ensure_ascii=False, indent=2) + ";\n")
    orders = study_orders()
    lines.append("window.studyOrders = " + json.dumps(orders, ensure_ascii=False, indent=2) + ";\n")
    CATALOG.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {len(records)} catalog records, {len(paths)} learning paths, and {len(orders)} study orders.")


if __name__ == "__main__":
    main()
