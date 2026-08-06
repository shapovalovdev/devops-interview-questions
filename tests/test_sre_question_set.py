"""Targeted acceptance checks for issue #63's SRE Question theme."""

from collections import Counter
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SRE = ROOT / "questions" / "sre"


def front_matter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    end = lines.index("---", 1)
    return dict(line.split(": ", 1) for line in lines[1:end] if ": " in line and not line.startswith("  "))


class SreQuestionSetTests(unittest.TestCase):
    def test_has_required_distribution_and_learning_links(self) -> None:
        questions = sorted(SRE.glob("*.md"))
        self.assertEqual(25, len(questions))
        difficulties = Counter(front_matter(path)["difficulty"] for path in questions)
        self.assertEqual({"junior": 5, "middle": 10, "senior": 5, "staff": 5}, difficulties)
        for question in questions:
            text = question.read_text(encoding="utf-8")
            self.assertEqual("sre", front_matter(question)["theme"])
            self.assertIn("## Answer guide", text)
            self.assertIn("## References", text)
            self.assertIn("Further reading (blog):", text)
            for category in ("Official documentation", "Manual or specification", "Maintainer or personal blog", "Technical blog", "Hands-on guide"):
                self.assertEqual(1, text.count(f"\n- {category}:"))


if __name__ == "__main__":
    unittest.main()
