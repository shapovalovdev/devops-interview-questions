#!/usr/bin/env python3
"""A validator on disk must be a validator that runs.

The workflow used to name eight scripts one by one, so the set of validators
was stated in `.github/workflows/validate-questions.yml` **and** implied by the
files in `tests/`, with nothing forcing the two to agree. A new
`tests/validate_*.py` ran nowhere until somebody remembered the workflow.

`tests/run_validators.py` discovers them instead. These checks are what stop
discovery from quietly breaking -- a glob that stops matching, or a workflow
that starts naming scripts again, would both leave a validator unrun while CI
stayed green.
"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests.run_validators import LIVE_CHECK_FLAG, validators  # noqa: E402

WORKFLOW = ROOT / ".github" / "workflows" / "validate-questions.yml"


class ValidatorDiscoveryTests(unittest.TestCase):
    def test_discovery_finds_every_validator_on_disk(self) -> None:
        """The set the runner sees is the set that exists."""
        on_disk = sorted(path.name for path in (ROOT / "tests").glob("validate_*.py"))
        discovered = sorted(path.name for path in validators())
        self.assertEqual(on_disk, discovered)
        self.assertTrue(discovered, "there must be validators to discover")

    def test_every_validator_has_a_main_to_run(self) -> None:
        """Discovery is worth nothing if a discovered file cannot be run."""
        from tests.run_validators import load

        for path in validators():
            with self.subTest(validator=path.name):
                module = load(path)
                self.assertTrue(
                    callable(getattr(module, "main", None)),
                    f"{path.name} is discovered but has no main(); it would be reported as a "
                    "failure on every run",
                )

    def test_the_workflow_calls_the_runner_and_names_no_validator(self) -> None:
        """The listing must not come back.

        This is the check that matters. Discovery working is not enough: if
        somebody adds `python tests/validate_new_thing.py` back into the
        workflow, the set is stated in two places again and they can drift.
        """
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("tests/run_validators.py", workflow, "the workflow must call the runner")

        named = re.findall(r"python tests/(validate_\w+\.py)", workflow)
        self.assertEqual(
            [],
            named,
            f"the workflow names validators individually: {named}. Discovery already runs them; "
            "naming one here means the set is stated twice.",
        )

    def test_the_live_check_flag_is_owned_by_the_validator_that_takes_it(self) -> None:
        """Only the learning-resource audit accepts --check-live, and it says so."""
        from tests.run_validators import load

        declaring = [
            path.name for path in validators() if getattr(load(path), "SUPPORTS_LIVE_CHECK", False)
        ]
        self.assertEqual(["validate_learning_resources.py"], declaring)

        for path in validators():
            source = path.read_text(encoding="utf-8")
            accepts = LIVE_CHECK_FLAG in source
            declares = path.name in declaring
            with self.subTest(validator=path.name):
                self.assertEqual(
                    accepts,
                    declares,
                    f"{path.name}: accepting {LIVE_CHECK_FLAG} and declaring SUPPORTS_LIVE_CHECK "
                    "must agree, or the runner will pass a flag the validator rejects, or "
                    "withhold one it needs",
                )

    def test_the_workflow_does_not_rerun_what_run_all_tests_already_runs(self) -> None:
        """`test_*.py` files belong to the other runner, and were run twice.

        `run_all_tests.py` globs `tests/test_*.py`, so naming any of them in the
        workflow as well ran them a second time -- three of the eight entries
        were doing exactly that.
        """
        workflow = WORKFLOW.read_text(encoding="utf-8")
        duplicated = re.findall(r"python tests/(test_\w+\.py)", workflow)
        self.assertEqual(
            [],
            duplicated,
            f"the workflow names test modules run_all_tests.py already discovers: {duplicated}",
        )


if __name__ == "__main__":
    unittest.main()
