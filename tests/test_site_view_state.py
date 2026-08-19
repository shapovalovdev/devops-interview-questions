#!/usr/bin/env python3
"""Hold the site's view state to a single tagged union.

`assets/site.js` used to carry five independent variables -- `activeTheme`,
`activeCertification`, `activeCollection`, `activePath` (strings with an `'all'`
sentinel) and `activeLabs` (a boolean) -- for what the domain says is *one*
selection.  Visibility was then derived by boolean algebra over them:

    questionZone.hidden = Boolean(path) || activeLabs;
    pathView.hidden     = !path || activeLabs;
    labsView.hidden     = !activeLabs;

Nothing in the *types* prevented "a learning path is selected **and** the Labs
view is on".  In practice the invariant held: every handler reset its four
siblings by hand, and `readHash()` reparsed the whole URL on every hashchange.
Old and new render identically on hand-crafted mixed hashes such as
`#path=sre-track&labs`, which was verified before this change landed.

So this is not a bug fix.  What changed is where the invariant lives: it moved
from a convention repeated at five call sites -- which a sixth entry point could
silently forget -- into the shape of the value itself, where forgetting is not
expressible.

The URL layer had it right all along: `setHash()` has only ever written a
single key, so the published URL surface was already a tagged union while the
in-memory state pretended otherwise.

These checks are structural -- they read `assets/site.js` as text rather than
executing it, because the repository's browser-level behaviour is already
covered by `tests/site_check.py` under Playwright and this suite must stay
standard-library only.  Between the two, the union is checked for shape here
and for behaviour there.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_JS = ROOT / "assets" / "site.js"

#: The variables the union replaced. None may come back.
RETIRED_VARIABLES = (
    "activeTheme",
    "activeCertification",
    "activeCollection",
    "activePath",
    "activeLabs",
)

#: Every variant the union admits, and the hash key each maps to.
VARIANTS = ("all", "theme", "certification", "collection", "path", "labs")


def source() -> str:
    return SITE_JS.read_text(encoding="utf-8")


def code() -> str:
    """The source with comments stripped, so prose cannot satisfy a check."""
    text = re.sub(r"/\*.*?\*/", "", source(), flags=re.DOTALL)
    return "\n".join(re.sub(r"//.*$", "", line) for line in text.splitlines())


def test_the_five_variables_are_gone() -> None:
    body = code()
    survivors = [name for name in RETIRED_VARIABLES if re.search(rf"\b{name}\b", body)]
    assert not survivors, (
        f"assets/site.js still carries {survivors}. View state is one tagged union; "
        "a parallel variable makes the illegal combinations expressible again, and puts the\n"
        "invariant back where a new call site can forget it."
    )


def test_a_single_view_holds_the_selection() -> None:
    body = code()
    assert re.search(r"let view = \{ kind: 'all' \}", body), (
        "assets/site.js must hold view state in a single `view` value initialised to {kind:'all'}"
    )
    declarations = re.findall(r"^\s*let\s+(\w+)", body, re.MULTILINE)
    assert declarations == ["view"], (
        f"`view` should be the only mutable module-level binding; found {declarations}. "
        "A second one is where the next parallel state variable starts."
    )


def test_every_variant_is_constructed_somewhere() -> None:
    body = code()
    missing = [kind for kind in VARIANTS if f"kind: '{kind}'" not in body]
    assert not missing, f"no code constructs the {missing} view variant"


def test_visibility_switches_on_kind_and_never_combines_regions() -> None:
    """The three regions are mutually exclusive, so no expression may mix them."""
    body = code()
    for region, expected in (
        ("questionZone.hidden", "view.kind === 'path' || view.kind === 'labs'"),
        ("pathView.hidden", "!path"),
        ("labsView.hidden", "view.kind !== 'labs'"),
    ):
        match = re.search(rf"{re.escape(region)}\s*=\s*([^;]+);", body)
        assert match, f"{region} is no longer assigned in assets/site.js"
        actual = " ".join(match.group(1).split())
        assert actual == expected, (
            f"{region} is now `{actual}`, expected `{expected}`. Visibility must follow "
            "view.kind; combining a path check with a labs flag is the boolean soup this "
            "change removed."
        )


def test_no_handler_resets_sibling_state_by_hand() -> None:
    """A handler constructs a whole view; it never patches flags one by one."""
    body = code()
    resets = re.findall(r"=\s*'all'\s*;", body)
    assert not resets, (
        f"found {len(resets)} `= 'all'` assignments. Entering a view must construct it, not "
        "reset the other selections by hand. The old code was correct precisely because it\n"
        "never forgot; the point is that it had to remember."
    )


def test_the_published_url_surface_is_unchanged() -> None:
    """Shared links must keep working: the hash keys are a public contract."""
    body = code()
    for key in ("'theme'", "'certificate'", "'collection'", "'path'", "'labs'"):
        assert key in body, (
            f"hash key {key} disappeared from assets/site.js; existing shared links carry it"
        )


def main() -> None:
    test_the_five_variables_are_gone()
    test_a_single_view_holds_the_selection()
    test_every_variant_is_constructed_somewhere()
    test_visibility_switches_on_kind_and_never_combines_regions()
    test_no_handler_resets_sibling_state_by_hand()
    test_the_published_url_surface_is_unchanged()
    print(f"View state is one union over {len(VARIANTS)} variants; no parallel state remains.")


if __name__ == "__main__":
    main()
