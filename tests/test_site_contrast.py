#!/usr/bin/env python3
"""Hold every colour the website paints to its WCAG AA contrast floor.

The site shipped with `--ember: #f35d3e`, which is **2.89:1** against
`--paper`.  It was used for nine small-text roles, for `input:focus`, and as the
background of the primary session button under white text.  Normal text needs
4.5:1, large text and non-text indicators need 3:1, so every one of those uses
failed -- including the focus ring, which is the one thing a keyboard user
depends on.

Nothing caught it, because contrast is not visible in a diff and
`site_check.py` drives behaviour rather than colour.  This module computes the
ratios from `assets/site.css` itself, so the stylesheet cannot drift back.

Two rules keep it honest as the site grows:

* `PAIRINGS` records, for each rule that sets a colour, the surfaces that colour
  can actually sit on -- a card link is read on the card and again on the acid
  hover state, and both must clear the floor.
* `test_every_colour_declaration_is_checked` fails when the stylesheet sets a
  colour this table does not describe, so a new rule cannot slip past unmeasured.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STYLESHEET = ROOT / "assets" / "site.css"

#: WCAG 2.1 minimums. Large text is >=24px, or >=18.66px when bold.
NORMAL_TEXT = 4.5
LARGE_TEXT = 3.0
NON_TEXT = 3.0


def tokens() -> dict[str, str]:
    """The custom properties declared on `:root`."""
    block = re.search(r":root\s*\{([^}]*)\}", STYLESHEET.read_text(encoding="utf-8"))
    assert block, "assets/site.css no longer declares a :root token block"
    return dict(re.findall(r"(--[a-z-]+):\s*(#[0-9a-fA-F]{6})", block.group(1)))


def _channel(value: float) -> float:
    return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4


def luminance(colour: str) -> float:
    digits = colour.lstrip("#")
    red, green, blue = (_channel(int(digits[i : i + 2], 16) / 255) for i in (0, 2, 4))
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast(foreground: str, background: str) -> float:
    lighter, darker = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def resolve(value: str, palette: dict[str, str]) -> str:
    """A token reference, or a literal the stylesheet writes out."""
    reference = re.fullmatch(r"var\((--[a-z-]+)\)", value)
    if reference:
        assert reference.group(1) in palette, f"{value}: no such token"
        return palette[reference.group(1)]
    return {"white": "#ffffff"}.get(value, value)


#: selector -> (foreground, surfaces it is read on, minimum ratio)
#:
#: Surfaces are given as tokens where one exists.  The translucent card and
#: panel fills (`rgba(245,241,232,.68)`, `rgba(255,255,255,.35)`) composite over
#: `--paper` to something at least as light as `--paper`, so measuring against
#: `--paper` is the conservative choice for the dark text they carry.
PAIRINGS: dict[str, tuple[str, tuple[str, ...], float]] = {
    "body": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".eyebrow": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    "h1 em": ("var(--ember)", ("var(--paper)",), LARGE_TEXT),
    ".statusbar b": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    ".practice-entry": ("var(--ink)", ("var(--acid)",), NORMAL_TEXT),
    "input": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".filter-heading": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    ".filter-heading span": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    ".filter": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".filter:hover, .filter.active": ("var(--acid)", ("var(--ink)",), NORMAL_TEXT),
    ".result-line": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    ".card-top": ("var(--muted)", ("var(--paper)", "var(--acid)"), NORMAL_TEXT),
    ".tags": ("var(--muted)", ("var(--paper)", "var(--acid)"), NORMAL_TEXT),
    ".question-card a": ("var(--ink)", ("var(--paper)", "var(--acid)"), NORMAL_TEXT),
    ".question-card a b": ("var(--ember-text)", ("var(--paper)", "var(--acid)"), NORMAL_TEXT),
    ".filter-count": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    ".filter.active .filter-count, .filter:hover .filter-count": (
        "var(--acid)",
        ("var(--ink)",),
        NORMAL_TEXT,
    ),
    ".path-prerequisites": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    ".path-prerequisites a, .path-exit": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".path-exit b": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    ".step-index": ("var(--ember-text)", ("var(--paper)", "var(--acid)"), LARGE_TEXT),
    ".step-body h3 a": ("var(--ink)", ("var(--paper)", "var(--acid)"), NORMAL_TEXT),
    ".step-why": ("var(--muted)", ("var(--paper)", "var(--acid)"), NORMAL_TEXT),
    ".study-order-panel summary": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".study-order-count": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    ".study-order-toggle": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    ".study-order-note": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    ".lab-card a": ("var(--ink)", ("var(--paper)", "var(--acid)"), NORMAL_TEXT),
    ".lab-card a b": ("var(--ember-text)", ("var(--paper)", "var(--acid)"), NORMAL_TEXT),
    "footer": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    "footer a": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".back-link": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".session-primary, .deck-actions button, .deck-utility button": (
        "var(--ink)",
        ("var(--paper)",),
        NORMAL_TEXT,
    ),
    ".session-primary": ("white", ("var(--ember-text)",), NORMAL_TEXT),
    ".session-message": ("#a73320", ("var(--paper)",), NORMAL_TEXT),
    ".deck-status": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    ".deck-status strong": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    ".session-answer a": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".deck-utility": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
}

#: Indicators that are not text.  WCAG 1.4.11 holds these to 3:1 against what
#: sits next to them, which for an outline drawn with `outline-offset` is the
#: page ground rather than the control's own fill.
INDICATORS: dict[str, tuple[str, str]] = {
    "input:focus outline": ("var(--ember-text)", "var(--paper)"),
    ":focus-visible outline": ("var(--ember-text)", "var(--paper)"),
    "checkbox accent-color": ("var(--ember-text)", "var(--paper)"),
}


def colour_declarations() -> dict[str, str]:
    """Every rule in the stylesheet that sets `color`, as selector -> value.

    Matches `color:` only at a declaration boundary, so `accent-color` and
    `background-color` are not mistaken for text colour.
    """
    source = STYLESHEET.read_text(encoding="utf-8")
    source = re.sub(r"/\*.*?\*/", "", source, flags=re.DOTALL)
    found: dict[str, str] = {}
    for selector, body in re.findall(r"([^{}]+)\{([^}]*)\}", source):
        selector = " ".join(selector.split())
        if selector.startswith("@") or selector in {":root", "from", "to"}:
            continue
        declaration = re.search(r"(?:^|;)\s*color:\s*([^;}]+)", body)
        if declaration:
            found[selector] = declaration.group(1).strip()
    return found


def test_every_colour_declaration_is_checked() -> None:
    """A new coloured rule must be measured, not merely added."""
    declared = colour_declarations()
    unchecked = set(declared) - set(PAIRINGS)
    assert not unchecked, (
        "assets/site.css sets a colour these checks do not measure: "
        f"{sorted(unchecked)}. Add each to PAIRINGS with the surfaces it is read on."
    )

    stale = set(PAIRINGS) - set(declared)
    assert not stale, (
        f"PAIRINGS describes rules the stylesheet no longer has: {sorted(stale)}"
    )

    for selector, value in declared.items():
        expected = PAIRINGS[selector][0]
        assert value == expected, (
            f"{selector} now sets {value!r}; PAIRINGS still says {expected!r}. "
            "Update the table and re-check the ratio."
        )


def test_text_meets_the_contrast_floor() -> None:
    palette = tokens()
    failures = []
    for selector, (foreground, surfaces, minimum) in PAIRINGS.items():
        for surface in surfaces:
            ratio = contrast(resolve(foreground, palette), resolve(surface, palette))
            if ratio < minimum:
                failures.append(
                    f"  {selector}: {foreground} on {surface} is {ratio:.2f}:1, needs {minimum}:1"
                )
    assert not failures, "WCAG AA contrast failures in assets/site.css:\n" + "\n".join(failures)


def test_focus_and_other_indicators_meet_the_non_text_floor() -> None:
    palette = tokens()
    failures = []
    for name, (foreground, surface) in INDICATORS.items():
        ratio = contrast(resolve(foreground, palette), resolve(surface, palette))
        if ratio < NON_TEXT:
            failures.append(f"  {name}: {ratio:.2f}:1, needs {NON_TEXT}:1")
    assert not failures, (
        "Non-text contrast failures (WCAG 1.4.11) in assets/site.css:\n" + "\n".join(failures)
    )


def test_keyboard_focus_is_styled_and_motion_is_opt_in() -> None:
    """The controls draw their own backgrounds, so the default ring is not enough."""
    source = STYLESHEET.read_text(encoding="utf-8")
    for control in (".filter:focus-visible", ".practice-entry:focus-visible", "button:focus-visible"):
        assert control in source, f"assets/site.css must give {control} a visible focus indicator"

    assert "@media (prefers-reduced-motion: no-preference)" in source, (
        "the card entrance animation must be opt-in under prefers-reduced-motion: no-preference"
    )
    # The base rule is the one that lays the card out; the animation must not be on it.
    base = re.search(r"\.question-card \{([^}]*min-height[^}]*)\}", source)
    assert base, "assets/site.css no longer has a base .question-card rule"
    assert "animation" not in base.group(1), (
        "`.question-card` still animates unconditionally; move `animation: enter` inside the "
        "prefers-reduced-motion: no-preference block"
    )

    opt_in = re.search(
        r"@media \(prefers-reduced-motion: no-preference\) \{(.*?)\n\}", source, re.DOTALL
    )
    assert opt_in and "animation: enter" in opt_in.group(1), (
        "the card entrance animation must live inside the no-preference block"
    )


def main() -> None:
    test_every_colour_declaration_is_checked()
    test_text_meets_the_contrast_floor()
    test_focus_and_other_indicators_meet_the_non_text_floor()
    test_keyboard_focus_is_styled_and_motion_is_opt_in()
    print(
        f"Checked {len(PAIRINGS)} colour pairings and {len(INDICATORS)} indicators "
        "against WCAG AA."
    )


if __name__ == "__main__":
    main()
