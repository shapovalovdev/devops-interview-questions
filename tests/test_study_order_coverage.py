"""Every related-materials page must ship within-Theme reading guidance.

The "Suggested study order" section of a related-materials page is generated
from `config/study-orders.json` by `scripts/generate_question_catalog.py`, so
the set stays complete by construction: a new Theme cannot publish its
related-materials page without a study-order section, and the section must
actually guide rather than act as a one-line stub.  The byte-level contract
with the manifest is defended by `test_study_order_generation.py`; these
checks keep the reader-facing floor.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELATED = ROOT / "docs" / "related-materials"
HEADER = re.compile(r"^## Suggested study order\s*$", re.MULTILINE)


class StudyOrderCoverage(unittest.TestCase):
    def test_every_related_materials_page_carries_the_section(self) -> None:
        pages = sorted(RELATED.glob("*.md"))
        self.assertTrue(pages, "docs/related-materials/ contains no pages")
        missing = [
            page.name
            for page in pages
            if HEADER.search(page.read_text(encoding="utf-8")) is None
        ]
        self.assertEqual(
            missing,
            [],
            "related-materials pages without a '## Suggested study order' section: "
            f"{missing}",
        )

    def test_the_section_appears_once_and_offers_real_guidance(self) -> None:
        for page in sorted(RELATED.glob("*.md")):
            with self.subTest(page=page.name):
                text = page.read_text(encoding="utf-8")
                self.assertEqual(
                    len(HEADER.findall(text)),
                    1,
                    "the study-order header appears more than once",
                )
                match = HEADER.search(text)
                assert match is not None
                body = text[match.end():].strip()
                self.assertGreaterEqual(
                    len(body.split()),
                    25,
                    "the study-order section must name Questions or concepts in a "
                    "deliberate order, not a stub",
                )


if __name__ == "__main__":
    unittest.main()
