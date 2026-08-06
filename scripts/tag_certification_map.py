#!/usr/bin/env python3
"""Apply a certification tag to Question links declared in a certification map."""

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    tag = sys.argv[1]
    mapping = ROOT / "docs" / "certifications" / f"{tag}.md"
    paths = sorted(
        {
            ROOT / match
            for match in re.findall(r"\]\(\.\./\.\./(questions/[^)]+\.md)\)", mapping.read_text())
        }
    )
    for path in paths:
        text = path.read_text()
        tags = re.search(r"^tags: \[([^]]+)\]$", text, re.MULTILINE)
        assert tags, f"{path}: missing inline tags"
        values = [value.strip() for value in tags.group(1).split(",")]
        if tag not in values:
            values.append(tag)
            text = text[: tags.start(1)] + ", ".join(values) + text[tags.end(1) :]
            path.write_text(text)
    print(f"Tagged {len(paths)} Questions with {tag}.")


if __name__ == "__main__":
    main()
