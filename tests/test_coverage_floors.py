#!/usr/bin/env python3
"""The coverage floors must be stated once, and must describe real modules.

Decision #192 chose per-module floors. The risk in that choice is not the
mechanism, it is the bookkeeping: floors in a config file, a threshold on a
pytest command line, and a set of modules that can quietly stop matching the
code. Any two of those disagreeing is this epic's defect wearing a new hat.

So these checks hold three things:

* the floors are declared in `config/coverage-floors.json` and **nowhere else**
  -- in particular no workflow passes `--cov-fail-under`;
* every module named there is one the suite actually measures;
* `pytest.ini` collects every contentdb test module, because a module that is
  not collected is coverage that is not measured. That was not hypothetical:
  `tests/test_contentdb_drift.py` was written, passed, and did not reach the
  gate, so `contentdb/drift.py` still reported 87.5%.
"""

from __future__ import annotations

import configparser
import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

FLOORS = ROOT / "config" / "coverage-floors.json"
PYTEST_INI = ROOT / "pytest.ini"
WORKFLOWS = ROOT / ".github" / "workflows"
PACKAGES = ("api", "contentdb")


def floors() -> dict:
    return json.loads(FLOORS.read_text(encoding="utf-8"))


class CoverageFloorsTests(unittest.TestCase):
    def test_the_floors_file_is_shaped_as_the_checker_expects(self) -> None:
        data = floors()
        for key in ("version", "policy", "default", "total", "modules", "exceptions_rationale"):
            self.assertIn(key, data, f"config/coverage-floors.json needs {key}")
        self.assertGreater(len(data["policy"]), 200, "the policy must explain the choice, not label it")
        self.assertGreaterEqual(data["total"], 95.0, "the total floor may not fall below the old flat gate")

    def test_every_exception_is_a_real_module_with_a_reason(self) -> None:
        """A floor below the default is a debt, so it has to be justified."""
        data = floors()
        for module, floor in data["modules"].items():
            with self.subTest(module=module):
                self.assertTrue(
                    (ROOT / module).is_file(),
                    f"{module} has a declared floor but does not exist",
                )
                self.assertLess(
                    floor,
                    data["default"],
                    f"{module} is at or above the default floor; delete the override rather than "
                    "restating the default",
                )
                self.assertIn(
                    module,
                    data["exceptions_rationale"],
                    f"{module} is below the default floor with no reason recorded",
                )
                self.assertGreater(len(data["exceptions_rationale"][module]), 40)

    def test_no_rationale_describes_a_module_without_a_floor(self) -> None:
        data = floors()
        orphans = sorted(set(data["exceptions_rationale"]) - set(data["modules"]))
        self.assertEqual([], orphans, f"rationale for modules with no floor: {orphans}")

    def test_no_workflow_states_a_coverage_threshold(self) -> None:
        """The floor lives in one file. A command-line threshold is a second copy."""
        offenders = []
        for workflow in sorted(WORKFLOWS.glob("*.yml")):
            # Strip comment lines first. The workflow explains *why* it does not
            # pass the flag, and a naive scan matches that explanation -- which
            # is what the first version of this test did.
            body = "\n".join(
                line for line in workflow.read_text(encoding="utf-8").splitlines()
                if not line.lstrip().startswith("#")
            )
            for match in re.finditer(r"--cov-fail-under[= ]\S+", body):
                offenders.append(f"{workflow.name}: {match.group(0)}")
        self.assertEqual(
            [],
            offenders,
            f"a workflow states a coverage threshold: {offenders}. Floors belong in "
            "config/coverage-floors.json, which tests/check_coverage_floors.py reads.",
        )

    def test_a_workflow_actually_runs_the_floor_check(self) -> None:
        """Declaring floors nothing enforces would be worse than a flat gate."""
        ran = [
            workflow.name
            for workflow in sorted(WORKFLOWS.glob("*.yml"))
            if "check_coverage_floors.py" in workflow.read_text(encoding="utf-8")
        ]
        self.assertTrue(ran, "no workflow runs tests/check_coverage_floors.py")

    def test_pytest_collects_every_contentdb_test_module(self) -> None:
        """A module pytest does not collect is coverage the gate cannot see.

        `testpaths` used to name each contentdb module by hand, and
        `tests/test_contentdb_drift.py` was simply left out -- its tests passed
        under run_all_tests.py while drift.py still reported 87.5% to the gate.
        """
        parser = configparser.ConfigParser()
        parser.read(PYTEST_INI)
        testpaths = parser["pytest"]["testpaths"].split()

        on_disk = {path.name for path in (ROOT / "tests").glob("test_contentdb_*.py")}
        self.assertTrue(on_disk, "there are contentdb test modules to collect")

        collected = set()
        for entry in testpaths:
            for path in ROOT.glob(entry):
                if path.name.startswith("test_contentdb_"):
                    collected.add(path.name)

        self.assertEqual(
            on_disk,
            collected,
            f"pytest.ini does not collect every contentdb test module. Missing: "
            f"{sorted(on_disk - collected)}. Use a glob rather than a hand-written list.",
        )


if __name__ == "__main__":
    unittest.main()
