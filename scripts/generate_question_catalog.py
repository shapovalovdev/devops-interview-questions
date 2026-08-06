#!/usr/bin/env python3
"""Generate the static GitHub Pages Question catalog from Markdown front matter."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
CATALOG = ROOT / "assets" / "questions.js"


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


def main() -> None:
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
    CATALOG.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {len(records)} catalog records.")


if __name__ == "__main__":
    main()
