"""Parity and determinism gates for `scripts/build_site.py`.

The own-site builder must reproduce the GitHub Pages URL layout exactly: a
Question's `.html` href may not change because `window.questions` paths, the
generated study-order links (`../../questions/...`), and every lab
`questionHref` depend on it.  These checks build the site into a temporary
directory once and then assert catalog/link parity and a byte-identical
rebuild, so the whole suite stays fast enough for every push.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build_site.py"
CATALOG = ROOT / "assets" / "questions.js"
DOCS = ROOT / "docs"


def load_builder():
    spec = importlib.util.spec_from_file_location("repo_build_site", BUILDER)
    assert spec and spec.loader, "scripts/build_site.py must be importable"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def window(name: str) -> list[dict]:
    """Read one `window.<name>` array back out of the generated site catalog."""
    text = CATALOG.read_text(encoding="utf-8")
    match = re.search(rf"window\.{name} = (\[[\s\S]*?\]);", text)
    assert match, f"assets/questions.js must publish window.{name}"
    return json.loads(re.sub(r",(\s*\])", r"\1", match.group(1)))


def tree_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def build_into(directory: Path) -> None:
    load_builder().build(directory)


class OwnSiteBuildParity(unittest.TestCase):
    """The built tree must satisfy every published link the site data layer emits."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.scratch = Path(tempfile.mkdtemp(prefix="build-site-test-"))
        cls.site = cls.scratch / "site"
        build_into(cls.site)

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(cls.scratch, ignore_errors=True)

    def test_every_window_questions_path_exists_as_a_file(self) -> None:
        missing = [
            record["path"]
            for record in window("questions")
            if not (self.site / record["path"]).is_file()
        ]
        self.assertEqual(
            missing,
            [],
            "every window.questions path must exist in the build at the same URL",
        )

    def test_every_lab_question_href_resolves_within_the_build(self) -> None:
        hrefs = {record["questionHref"] for record in window("labs")}
        self.assertTrue(hrefs, "window.labs must publish at least one lab")
        missing = [href for href in sorted(hrefs) if not (self.site / href).is_file()]
        self.assertEqual(missing, [], "every lab questionHref must resolve to a built page")

    def test_every_generated_docs_link_resolves_within_the_build(self) -> None:
        """Related-materials and certification pages link Questions relatively.

        Every relative `href` the renderer emits inside a generated docs page
        must land on a file in the build: study-order `.html` links straight
        from the source, certification `.md` links rewritten by the builder.
        """
        href = re.compile(r'<a href="([^"]+)"')
        checked = 0
        failures: list[str] = []
        for page in sorted((self.site / "docs").rglob("*.html")):
            base = page.parent
            for url in href.findall(page.read_text(encoding="utf-8")):
                if "://" in url or url.startswith(("#", "mailto:")):
                    continue
                checked += 1
                target = (base / url.split("#", 1)[0]).resolve()
                if not target.is_file():
                    failures.append(f"{page.relative_to(self.site)}: {url}")
        self.assertTrue(checked > 100, "the docs corpus must exercise its relative links")
        self.assertEqual(failures[:10], [], f"unresolved relative links ({len(failures)} total)")

    def test_static_root_pages_and_assets_are_copied_verbatim(self) -> None:
        for name in ("index.html", "404.html", "session.html"):
            self.assertTrue((self.site / name).is_file(), f"{name} must be copied as-is")
            self.assertEqual(
                (self.site / name).read_bytes(),
                (ROOT / name).read_bytes(),
                f"{name} must be byte-identical to the repository file",
            )
        for asset in sorted((ROOT / "assets").rglob("*")):
            if asset.is_file():
                built = self.site / "assets" / asset.relative_to(ROOT / "assets")
                self.assertEqual(built.read_bytes(), asset.read_bytes(), f"{built} must be verbatim")

    def test_rebuilding_produces_a_byte_identical_tree(self) -> None:
        second = self.scratch / "site-again"
        build_into(second)
        self.assertEqual(
            tree_hashes(self.site),
            tree_hashes(second),
            "building twice must produce identical trees",
        )


if __name__ == "__main__":
    unittest.main()
