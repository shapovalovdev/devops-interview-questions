#!/usr/bin/env python3
"""Run every check in `tests/` and fail loudly if any of them is a no-op.

The suite mixes three shapes: `unittest.TestCase` classes, bare pytest-style
`test_*` functions, and script-style modules with a `main()`.  Invoking each file
with `python tests/test_x.py` only executes whatever its `__main__` block calls,
so a module of bare `test_*` functions — or a script-style module whose block
calls just `main()` — exits 0 having asserted nothing.  Sixteen checks were
silently skipped that way.

This harness imports every module and runs all three shapes explicitly, so a test
counts only when it actually executes.
"""

from __future__ import annotations

import importlib.util
import inspect
import sys
import traceback
import types
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"
SELF = Path(__file__).name


def load(path: Path) -> types.ModuleType:
    spec = importlib.util.spec_from_file_location(f"repo_tests.{path.stem}", path)
    assert spec and spec.loader, f"{path}: not importable"
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def checks(module: types.ModuleType) -> list[tuple[str, object]]:
    """Every runnable check in a module: TestCase classes, test functions, main()."""
    found: list[tuple[str, object]] = []
    for name, value in vars(module).items():
        if isinstance(value, type) and issubclass(value, unittest.TestCase):
            found.append((name, value))
        elif name.startswith("test_") and inspect.isfunction(value) and value.__module__ == module.__name__:
            found.append((name, value))
    main = getattr(module, "main", None)
    if inspect.isfunction(main) and main.__module__ == module.__name__:
        found.append(("main", main))
    return found


def run(name: str, check: object) -> bool:
    if isinstance(check, type):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(check)
        result = unittest.TextTestRunner(stream=sys.stdout, verbosity=0).run(suite)
        return result.wasSuccessful()
    try:
        check()  # type: ignore[operator]
    except Exception:  # noqa: BLE001 - a failed check must not stop the suite
        traceback.print_exc()
        return False
    return True


def main() -> int:
    paths = sorted(path for path in TESTS.glob("test_*.py") if path.name != SELF)
    assert paths, "no tests found"
    executed = 0
    failures: list[str] = []
    for path in paths:
        module = load(path)
        found = checks(module)
        assert found, f"{path.name}: defines no runnable check"
        for name, check in found:
            executed += 1
            if not run(name, check):
                failures.append(f"{path.name}::{name}")

    print(f"Ran {executed} checks across {len(paths)} test modules.")
    if failures:
        print(f"FAILED {len(failures)}: {', '.join(failures)}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
