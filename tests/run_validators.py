#!/usr/bin/env python3
"""Run every content validator, discovered rather than listed.

`.github/workflows/validate-questions.yml` used to name eight scripts one by
one in a shell block.  A new `tests/validate_*.py` therefore ran nowhere until
somebody remembered to edit the workflow, and nothing failed to remind them.

That is the same failure `tests/run_all_tests.py` was written for -- its
docstring records sixteen checks that were silently skipped -- and it is the
defect this repository's *Single source of truth* epic exists to remove: the
list of validators was stated in a workflow file **and** implied by the files on
disk, with nothing forcing the two to agree.

This module discovers them.  `tests/test_validator_discovery.py` proves the
discovered set matches the disk, so a validator cannot go unrun and this runner
cannot silently stop finding one.

**Flags belong to the validator that accepts them.**  Only the learning-resource
audit takes `--check-live`, and it says so itself through a module-level
`SUPPORTS_LIVE_CHECK`.  A table here naming which validator takes which flag
would be the listing problem again, one file further along.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"

#: The flag a validator opts into by declaring `SUPPORTS_LIVE_CHECK = True`.
LIVE_CHECK_FLAG = "--check-live"


def validators() -> list[Path]:
    """Every content validator on disk, in a stable order."""
    return sorted(TESTS.glob("validate_*.py"))


def load(path: Path) -> types.ModuleType:
    specification = importlib.util.spec_from_file_location(f"repo_validators.{path.stem}", path)
    assert specification and specification.loader, f"{path}: not importable"
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


def run(path: Path, *, live: bool) -> bool:
    """Run one validator's `main()`, returning whether it passed."""
    module = load(path)
    main = getattr(module, "main", None)
    if main is None:
        print(f"{path.name}: no main() to run", file=sys.stderr)
        return False

    argv = [path.name]
    if live and getattr(module, "SUPPORTS_LIVE_CHECK", False):
        argv.append(LIVE_CHECK_FLAG)

    original = sys.argv
    sys.argv = argv
    try:
        main()
    except AssertionError as error:
        print(f"{path.name}: {error}", file=sys.stderr)
        return False
    except SystemExit as exit_code:
        if exit_code.code not in (0, None):
            print(f"{path.name}: exited {exit_code.code}", file=sys.stderr)
            return False
    finally:
        sys.argv = original
    return True


def main() -> int:
    parser = argparse.ArgumentParser(prog="python tests/run_validators.py")
    parser.add_argument(
        LIVE_CHECK_FLAG,
        action="store_true",
        help="also perform the live link audit, for validators that support it",
    )
    arguments = parser.parse_args()

    found = validators()
    assert found, "tests/validate_*.py matched nothing; discovery is broken"

    failed = [path.name for path in found if not run(path, live=arguments.check_live)]
    if failed:
        print(f"\n{len(failed)} of {len(found)} validators failed: {', '.join(failed)}", file=sys.stderr)
        return 1
    print(f"Ran {len(found)} discovered validators: {', '.join(path.stem for path in found)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
