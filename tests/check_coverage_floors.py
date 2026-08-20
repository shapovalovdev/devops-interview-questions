#!/usr/bin/env python3
"""Hold each module to its own coverage floor, declared in exactly one place.

Decision #192 chose per-module floors over one repository-wide number. With a
single flat floor the gate fails for whoever pushes next rather than for whoever
regressed: the next agent to touch `ingest.py` inherits `corpus.py`'s debt,
discovers it at push time, and either writes unrelated tests or is blocked.

The floors live in `config/coverage-floors.json` and nowhere else. In
particular the pytest invocation carries **no** `--cov-fail-under`: that flag
would state the repository floor a second time, on a command line, where it
could disagree with the file. This epic exists to remove exactly that shape, so
the gate cannot be built out of it.

Run after pytest has written a coverage JSON report:

    pytest --cov=api --cov=contentdb --cov-branch --cov-report=json:coverage.json
    python tests/check_coverage_floors.py coverage.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FLOORS = ROOT / "config" / "coverage-floors.json"


def load_floors() -> dict:
    assert FLOORS.is_file(), f"{FLOORS.relative_to(ROOT)} is required"
    return json.loads(FLOORS.read_text(encoding="utf-8"))


def floor_for(module: str, floors: dict) -> float:
    return float(floors["modules"].get(module, floors["default"]))


def shortfalls(report: dict, floors: dict) -> list[str]:
    """Every module below its own floor, and the total below the total floor."""
    failures = []
    for module, measured in sorted(report["files"].items()):
        covered = measured["summary"]["percent_covered"]
        floor = floor_for(module, floors)
        if covered + 0.05 < floor:
            failures.append(f"{module}: {covered:.1f}% is below its floor of {floor:.1f}%")

    total = report["totals"]["percent_covered"]
    if total + 0.05 < float(floors["total"]):
        failures.append(f"TOTAL: {total:.2f}% is below the total floor of {floors['total']:.1f}%")
    return failures


def undeclared_modules(report: dict, floors: dict) -> list[str]:
    """Declared exceptions that no longer name a measured module.

    A stale entry is a floor nobody is held to, and it hides the fact that the
    module it named is gone or renamed.
    """
    return sorted(set(floors["modules"]) - set(report["files"]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python tests/check_coverage_floors.py")
    parser.add_argument("report", type=Path, help="the coverage JSON report pytest wrote")
    arguments = parser.parse_args(argv)

    if not arguments.report.is_file():
        print(f"no coverage report at {arguments.report}", file=sys.stderr)
        return 1

    report = json.loads(arguments.report.read_text(encoding="utf-8"))
    floors = load_floors()

    stale = undeclared_modules(report, floors)
    if stale:
        print(
            f"config/coverage-floors.json names modules that were not measured: {stale}. "
            "Remove the entry, or check the module was not renamed.",
            file=sys.stderr,
        )
        return 1

    failures = shortfalls(report, floors)
    if failures:
        print("Coverage below the declared floors:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        print(
            "\nFloors are in config/coverage-floors.json. Raising one is welcome; "
            "lowering one needs a reason in the commit that does it.",
            file=sys.stderr,
        )
        return 1

    total = report["totals"]["percent_covered"]
    print(
        f"Coverage meets every floor: {len(report['files'])} modules, "
        f"total {total:.2f}% against a floor of {floors['total']:.1f}%."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
