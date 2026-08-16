#!/usr/bin/env python3
"""Generate the static GitHub Pages Question catalog from Markdown front matter."""

import json
import re
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
CATALOG = ROOT / "assets" / "questions.js"
MANIFEST = ROOT / "config" / "content-manifest.json"
LEARNING_PATHS = ROOT / "config" / "learning-paths.json"
STUDY_ORDERS = ROOT / "config" / "study-orders.json"
RELATED_MATERIALS = ROOT / "docs" / "related-materials"
STUDY_ORDER_HEADER = re.compile(r"^## Suggested study order\s*$", re.MULTILINE)
NEXT_SECTION = re.compile(r"^## ", re.MULTILINE)
WRAP_WIDTH = 80


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


def _wrap(text: str, initial_indent: str = "", subsequent_indent: str = "") -> str:
    """Wrap prose to the pages' width without ever breaking a word or URL."""
    return textwrap.fill(
        text,
        width=WRAP_WIDTH,
        initial_indent=initial_indent,
        subsequent_indent=subsequent_indent,
        break_long_words=False,
        break_on_hyphens=False,
    )


def _wrap_item(position: int, link: str, why: str) -> str:
    """Wrap one ordered step, keeping the Question link a single unbroken atom."""
    marker = f"{position}."
    indent = " " * 4
    lines: list[str] = []
    current = marker
    for atom in [link, "—", *why.split()]:
        if current == marker or len(current) + 1 + len(atom) <= WRAP_WIDTH:
            current += f" {atom}"
        else:
            lines.append(current)
            current = indent + atom
    lines.append(current)
    return "\n".join(lines)


def study_order_section(theme: dict) -> str:
    """Render one Theme's study-order section from manifest data alone."""
    lines = [
        "## Suggested study order",
        "",
        _wrap(theme["note"]),
        "",
    ]
    for position, step in enumerate(theme["steps"], start=1):
        source = ROOT / step["question"]
        fields = front_matter(source)
        href = "../../" + source.relative_to(ROOT).with_suffix(".html").as_posix()
        link = f"[{fields['title']}]({href})"
        lines.append(_wrap_item(position, link, step["why"]))
    return "\n".join(lines) + "\n"


def rewrite_study_orders() -> int:
    """Regenerate every related-materials page's study-order section in place.

    The manifest is the only authority: the authored `note` opens the section
    and each ordered step renders as a link to its Question with its `why`.
    Everything outside the section is preserved byte for byte, and a page
    whose section already matches is left untouched.
    """
    declaration = json.loads(STUDY_ORDERS.read_text(encoding="utf-8"))
    rewritten = 0
    for theme in declaration["themes"]:
        page = RELATED_MATERIALS / f"{theme['theme']}.md"
        assert page.is_file(), f"{theme['theme']}: missing related-materials page {page}"
        text = page.read_text(encoding="utf-8")
        match = STUDY_ORDER_HEADER.search(text)
        assert match is not None, f"{page}: no '## Suggested study order' section to regenerate"
        rest = text[match.end():]
        following = NEXT_SECTION.search(rest)
        tail = "\n" + rest[following.start():] if following else ""
        generated = study_order_section(theme)
        if text[: match.start()] + generated + tail != text:
            page.write_text(text[: match.start()] + generated + tail, encoding="utf-8")
            rewritten += 1
    return rewritten


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
    rewritten = rewrite_study_orders()
    print(
        f"Generated {len(records)} catalog records, {len(paths)} learning paths, "
        f"{len(orders)} study orders, and rewrote {rewritten} study-order sections."
    )


if __name__ == "__main__":
    main()
