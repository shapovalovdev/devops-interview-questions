"""The standard-library boundary the epic draws around the Content API.

FastAPI, Pydantic, uvicorn, and httpx are confined to the API service and its
tests. Two things must keep working in an interpreter where none of them can be
imported:

- `scripts/build_site.py`, because the static site is published from a runtime
  that installs nothing; and
- `api/store.py`, because slice 1 is building the Content store as a
  standard-library-only package and it has to satisfy the `Store` protocol
  without importing the API's serialization layer.

Both are checked in a subprocess with a meta-path finder that refuses every
third-party import, so the check does not depend on what happens to be
installed on the machine running it. This module lives at the top of `tests/`
on purpose: `tests/run_all_tests.py` globs `tests/test_*.py` non-recursively,
so it runs here, in the dependency-free suite, rather than beside the API tests
that need FastAPI.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BLOCKED_MODULES = ("fastapi", "pydantic", "pydantic_core", "starlette", "uvicorn", "httpx", "pytest", "yaml")

BLOCKER = """
import importlib.abc
import sys


class Blocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in BLOCKED:
            raise ImportError(f"third-party package is blocked: {fullname}")
        return None


sys.meta_path.insert(0, Blocker())
"""

BUILD_SITE = """
import runpy

sys.argv = ["build_site.py", "--output", OUTPUT]
runpy.run_path(BUILD_SCRIPT, run_name="__main__")
"""

IMPORT_STORE = """
import api.store

query = api.store.QuestionQuery(theme="linux")
page = api.store.Page(items=[{"id": "linux/x"}], total=1)
assert query.sort == "id", query.sort
assert page.total == 1
print("api.store imported with every third-party package blocked")
"""


def blocked_run(body: str, **names: object) -> subprocess.CompletedProcess[str]:
    """Run `body` in a subprocess where no third-party import can succeed."""
    preamble = f"BLOCKED = {BLOCKED_MODULES!r}\n"
    preamble += "".join(f"{key} = {value!r}\n" for key, value in names.items())
    return subprocess.run(
        [sys.executable, "-c", preamble + BLOCKER + body],
        capture_output=True,
        text=True,
        cwd=ROOT,
        timeout=300,
    )


class ThirdPartyImportBlockerTest(unittest.TestCase):
    def test_build_site_runs_with_third_party_imports_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as output:
            completed = blocked_run(
                BUILD_SITE,
                OUTPUT=output,
                BUILD_SCRIPT=str(ROOT / "scripts" / "build_site.py"),
            )
        self.assertEqual(
            completed.returncode,
            0,
            f"build_site.py failed with third-party imports blocked:\n{completed.stderr}",
        )
        self.assertIn("Rendered", completed.stdout)

    def test_the_store_seam_imports_with_third_party_imports_blocked(self) -> None:
        """`contentdb` must be able to implement this protocol without the API's stack."""
        completed = blocked_run(IMPORT_STORE)
        self.assertEqual(
            completed.returncode,
            0,
            "api/store.py must stay standard-library only so the Content store can "
            f"implement the Store protocol:\n{completed.stderr}",
        )
        self.assertIn("api.store imported", completed.stdout)


if __name__ == "__main__":
    unittest.main()
