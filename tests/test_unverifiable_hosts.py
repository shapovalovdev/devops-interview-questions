#!/usr/bin/env python3
"""Keep the unverifiable-host list small, evidenced, and freshly reviewed.

`docs/research/unverifiable-hosts.json` exempts a host from the broken-link
verdict, so it is the one place where the live gate stops protecting the
database. It exists because `csrc.nist.gov` answers GitHub-hosted runners with
`404` for documents that demonstrably exist, and no amount of retrying changes
that.

The danger is obvious: an exemption list is how a dead link hides. These checks
make that expensive rather than free — every entry must state its reason and its
evidence, must have been manually verified inside the review window, and the
list may not grow past a handful of hosts. A stale entry fails the build, which
forces someone to re-check the host rather than let the exemption drift.
"""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/research/unverifiable-hosts.json"
REQUIRED_FIELDS = ("host", "reason", "evidence", "verified_manually_on")


def registry() -> dict:
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_every_entry_carries_reason_and_evidence() -> None:
    for entry in registry()["hosts"]:
        missing = [field for field in REQUIRED_FIELDS if not str(entry.get(field, "")).strip()]
        assert not missing, f"{entry.get('host', '?')}: exemption needs {missing}"
        assert len(entry["evidence"]) >= 80, (
            f"{entry['host']}: evidence must describe what was actually observed, not assert a conclusion"
        )


def test_manual_verification_is_current() -> None:
    data = registry()
    window = timedelta(days=data["review_interval_days"])
    stale = []
    for entry in data["hosts"]:
        verified = date.fromisoformat(entry["verified_manually_on"])
        if date.today() - verified > window:
            stale.append(f"{entry['host']} (last verified {verified})")
    assert not stale, (
        "These hosts have not been re-verified inside the review window. Check by hand whether the "
        "URLs still resolve and whether the host has become checkable from CI, then update or remove "
        f"the entry:\n" + "\n".join(stale)
    )


def test_the_list_stays_small() -> None:
    data = registry()
    assert len(data["hosts"]) <= data["max_hosts"], (
        f"{len(data['hosts'])} exempted hosts exceeds the cap of {data['max_hosts']}. An exemption is a "
        "hole in the link gate, not a way to make a red build green."
    )


def main() -> None:
    test_every_entry_carries_reason_and_evidence()
    test_manual_verification_is_current()
    test_the_list_stays_small()
    hosts = registry()["hosts"]
    print(f"Validated {len(hosts)} unverifiable-host exemption(s): {', '.join(entry['host'] for entry in hosts)}.")


if __name__ == "__main__":
    main()
