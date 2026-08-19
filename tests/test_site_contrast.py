#!/usr/bin/env python3
"""Hold every colour the website paints to WCAG AA, in **both** themes.

The site shipped with `--ember: #f35d3e`, which is 2.89:1 against `--paper`.  It
was used for nine small-text roles, for `input:focus`, and as the background of
the primary session button under white text.  Every one of those failed,
including the focus ring, which is the one thing a keyboard user depends on.
Nothing caught it, because contrast is not visible in a diff and `site_check.py`
drives behaviour rather than colour.

The dark theme (#200) made two more things necessary.

**Both palettes are measured.**  A pairing that clears the floor on cream can
fail on the dark ground and the other way round, so every entry in `PAIRINGS` is
checked twice -- once against `:root`, once against the tokens redefined under
`@media (prefers-color-scheme: dark)`.

**Alpha is composited, not ignored.**  Most surfaces are translucent
(`--surface`, `--hover`, `--field`).  Measuring text against the token's own
rgba is meaningless; what a reader sees is the colour after it composites over
`--paper`, so that is what is measured.

`test_no_colour_is_defined_only_in_a_media_query` guards the classic
unreadable-dark-mode bug: a colour whose only definition sits inside the media
block never applies in the default state, so the page renders one theme's text
on the other theme's ground.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STYLESHEET = ROOT / "assets" / "site.css"

NORMAL_TEXT = 4.5
LARGE_TEXT = 3.0
NON_TEXT = 3.0

THEMES = ("light", "dark")


# --------------------------------------------------------------- the palettes


def _declarations(block: str) -> dict[str, str]:
    return {
        name: value.strip()
        for name, value in re.findall(r"(--[a-z-]+):\s*([^;]+);", block)
    }


def palettes() -> dict[str, dict[str, str]]:
    """The light palette from `:root`, and the dark one layered over it.

    Dark redefines tokens rather than restating the palette, so it is read as an
    overlay: anything it does not mention keeps its light value, which is what
    the cascade does too.
    """
    text = STYLESHEET.read_text(encoding="utf-8")
    light_block = re.search(r":root \{(.*?)\n\}", text, re.DOTALL)
    assert light_block, "assets/site.css no longer declares a bare :root block"

    dark_block = re.search(
        r"@media \(prefers-color-scheme: dark\) \{\s*:root \{(.*?)\n  \}", text, re.DOTALL
    )
    assert dark_block, "assets/site.css declares no dark palette"

    light = _declarations(light_block.group(1))
    dark = {**light, **_declarations(dark_block.group(1))}
    return {"light": light, "dark": dark}


# ------------------------------------------------------------------ the maths


def _channel(value: float) -> float:
    return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4


def _rgb(colour: str) -> tuple[int, int, int]:
    digits = colour.lstrip("#")
    return tuple(int(digits[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def luminance(colour: str) -> float:
    red, green, blue = (_channel(part / 255) for part in _rgb(colour))
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast(foreground: str, background: str) -> float:
    lighter, darker = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def composite(colour: str, ground: str) -> str:
    """Flatten a translucent token onto the ground it is painted over.

    A reader never sees `rgba(199, 242, 74, .14)`; they see what it becomes over
    `--paper`. Contrast has to be measured against that.
    """
    match = re.fullmatch(r"rgba\(\s*([\d.]+),\s*([\d.]+),\s*([\d.]+),\s*([\d.]*)\s*\)", colour)
    if not match:
        return colour
    red, green, blue, alpha = (float(part) for part in match.groups())
    base = _rgb(ground)
    blended = (
        round(channel * alpha + base[index] * (1 - alpha))
        for index, channel in enumerate((red, green, blue))
    )
    return "#%02x%02x%02x" % tuple(blended)


def resolve(value: str, palette: dict[str, str]) -> str:
    """A token reference or a literal, flattened onto the page ground."""
    reference = re.fullmatch(r"var\((--[a-z-]+)\)", value)
    ground = palette["--paper"]
    if reference:
        token = reference.group(1)
        assert token in palette, f"{value}: no such token"
        return composite(palette[token], ground)
    return composite(value, ground)


# ------------------------------------------------------------------ the table

#: selector -> (foreground, surfaces it is read on, minimum ratio)
#:
#: A rule that sets both a colour and a background states its own pairing --
#: `.question-card:hover` is the clearest case -- so its surface is that
#: background rather than the page ground.
PAIRINGS: dict[str, tuple[str, tuple[str, ...], float]] = {
    "body": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".eyebrow": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    "h1 em": ("var(--ember)", ("var(--paper)",), LARGE_TEXT),
    ".statusbar b": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    ".practice-entry": ("var(--on-acid)", ("var(--acid)",), NORMAL_TEXT),
    "input": ("var(--ink)", ("var(--field)",), NORMAL_TEXT),
    ".filter-heading": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    ".filter-heading span": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    ".filter": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".filter:hover, .filter.active": ("var(--on-invert)", ("var(--invert)",), NORMAL_TEXT),
    ".result-line": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    ".question-card:hover": ("var(--on-hover)", ("var(--hover)",), NORMAL_TEXT),
    ".card-top": ("var(--muted)", ("var(--surface)", "var(--hover)"), NORMAL_TEXT),
    ".tags": ("var(--muted)", ("var(--surface)", "var(--hover)"), NORMAL_TEXT),
    ".question-card a": ("var(--ink)", ("var(--surface)", "var(--hover)"), NORMAL_TEXT),
    ".question-card a b": ("var(--ember-text)", ("var(--surface)", "var(--hover)"), NORMAL_TEXT),
    ".filter-count": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    ".filter.active .filter-count, .filter:hover .filter-count": (
        "var(--on-invert)",
        ("var(--invert)",),
        NORMAL_TEXT,
    ),
    ".path-prerequisites": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    ".path-prerequisites a, .path-exit": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".path-exit b": ("var(--ember-text)", ("var(--paper)",), NORMAL_TEXT),
    ".path-step:hover": ("var(--on-hover)", ("var(--hover)",), NORMAL_TEXT),
    ".step-index": ("var(--ember-text)", ("var(--surface)", "var(--hover)"), LARGE_TEXT),
    ".step-body h3 a": ("var(--ink)", ("var(--surface)", "var(--hover)"), NORMAL_TEXT),
    ".step-why": ("var(--muted)", ("var(--surface)", "var(--hover)"), NORMAL_TEXT),
    ".study-order-panel summary": ("var(--ink)", ("var(--surface-raised)",), NORMAL_TEXT),
    ".study-order-count": ("var(--muted)", ("var(--surface-raised)",), NORMAL_TEXT),
    ".study-order-toggle": ("var(--ember-text)", ("var(--surface-raised)",), NORMAL_TEXT),
    ".study-order-note": ("var(--muted)", ("var(--surface-raised)",), NORMAL_TEXT),
    ".lab-card:hover": ("var(--on-hover)", ("var(--hover)",), NORMAL_TEXT),
    ".lab-card a": ("var(--ink)", ("var(--surface)", "var(--hover)"), NORMAL_TEXT),
    ".lab-card a b": ("var(--ember-text)", ("var(--surface)", "var(--hover)"), NORMAL_TEXT),
    "footer": ("var(--muted)", ("var(--paper)",), NORMAL_TEXT),
    "footer a": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".back-link": ("var(--ink)", ("var(--paper)",), NORMAL_TEXT),
    ".session-theme.selected": ("var(--on-hover)", ("var(--hover)",), NORMAL_TEXT),
    ".session-primary, .deck-actions button, .deck-utility button": (
        "var(--ink)",
        ("var(--surface-raised)",),
        NORMAL_TEXT,
    ),
    ".session-primary": ("var(--on-ember)", ("var(--ember-text)",), NORMAL_TEXT),
    ".session-message": ("var(--danger)", ("var(--surface-raised)",), NORMAL_TEXT),
    ".deck-status": ("var(--muted)", ("var(--surface-raised)",), NORMAL_TEXT),
    ".deck-status strong": ("var(--ember-text)", ("var(--surface-raised)",), NORMAL_TEXT),
    ".session-answer a": ("var(--ink)", ("var(--answer-wash)",), NORMAL_TEXT),
    ".deck-utility": ("var(--muted)", ("var(--surface-raised)",), NORMAL_TEXT),
}

#: Indicators that are not text. WCAG 1.4.11 holds these to 3:1 against what
#: sits next to them, which for an outline drawn with `outline-offset` is the
#: page ground rather than the control's own fill.
INDICATORS: dict[str, tuple[str, str]] = {
    "input:focus outline": ("var(--ember-text)", "var(--paper)"),
    ":focus-visible outline": ("var(--ember-text)", "var(--paper)"),
    "checkbox accent-color": ("var(--ember-text)", "var(--paper)"),
}


# ------------------------------------------------------------------ the rules


def colour_declarations() -> dict[str, str]:
    """Every rule that sets `color`, as selector -> value.

    Matches `color:` only at a declaration boundary, so `accent-color` and
    `background-color` are not mistaken for text colour. Token blocks and
    at-rules are skipped: they declare the palette rather than paint with it.
    """
    source = re.sub(r"/\*.*?\*/", "", STYLESHEET.read_text(encoding="utf-8"), flags=re.DOTALL)
    found: dict[str, str] = {}
    for selector, body in re.findall(r"([^{}]+)\{([^}]*)\}", source):
        selector = " ".join(selector.split())
        if selector.startswith("@") or selector.startswith(":root") or selector in {"from", "to"}:
            continue
        declaration = re.search(r"(?:^|;)\s*color:\s*([^;}]+)", body)
        if declaration:
            found[selector] = declaration.group(1).strip()
    return found


def test_every_colour_declaration_is_checked() -> None:
    declared = colour_declarations()
    unchecked = set(declared) - set(PAIRINGS)
    assert not unchecked, (
        "assets/site.css sets a colour these checks do not measure: "
        f"{sorted(unchecked)}. Add each to PAIRINGS with the surfaces it is read on."
    )
    stale = set(PAIRINGS) - set(declared)
    assert not stale, f"PAIRINGS describes rules the stylesheet no longer has: {sorted(stale)}"

    for selector, value in declared.items():
        expected = PAIRINGS[selector][0]
        assert value == expected, (
            f"{selector} now sets {value!r}; PAIRINGS still says {expected!r}. "
            "Update the table and re-check the ratio in both themes."
        )


def test_no_colour_is_defined_only_in_a_media_query() -> None:
    """The classic unreadable-dark-mode bug, refused.

    A token defined only inside `@media (prefers-color-scheme: dark)` is absent
    in the default state, so the page paints one theme's text on the other
    theme's ground. Every token the dark block redefines must already exist on
    bare `:root`.
    """
    light, dark = palettes()["light"], palettes()["dark"]
    orphans = sorted(set(dark) - set(light))
    assert not orphans, (
        f"these tokens exist only in the dark palette: {orphans}. Define each on bare :root "
        "as well, or the default (no `prefers-color-scheme`) state has no value for it."
    )


def test_no_rule_paints_a_raw_colour() -> None:
    """Literals cannot be re-themed, so every colour has to be a token."""
    source = re.sub(r"/\*.*?\*/", "", STYLESHEET.read_text(encoding="utf-8"), flags=re.DOTALL)
    body = source[source.index("* { box-sizing"):]
    literals = re.findall(r"rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8}\b|\bwhite\b|\bblack\b", body)
    assert not literals, (
        f"assets/site.css paints raw colours outside the palette: {sorted(set(literals))}. "
        "A literal keeps its light-theme value in dark mode."
    )


def test_text_meets_the_contrast_floor_in_both_themes() -> None:
    failures = []
    for theme, palette in palettes().items():
        for selector, (foreground, surfaces, minimum) in PAIRINGS.items():
            for surface in surfaces:
                ratio = contrast(resolve(foreground, palette), resolve(surface, palette))
                if ratio < minimum:
                    failures.append(
                        f"  [{theme}] {selector}: {foreground} on {surface} is "
                        f"{ratio:.2f}:1, needs {minimum}:1"
                    )
    assert not failures, "WCAG AA contrast failures in assets/site.css:\n" + "\n".join(failures)


def test_indicators_meet_the_non_text_floor_in_both_themes() -> None:
    failures = []
    for theme, palette in palettes().items():
        for name, (foreground, surface) in INDICATORS.items():
            ratio = contrast(resolve(foreground, palette), resolve(surface, palette))
            if ratio < NON_TEXT:
                failures.append(f"  [{theme}] {name}: {ratio:.2f}:1, needs {NON_TEXT}:1")
    assert not failures, (
        "Non-text contrast failures (WCAG 1.4.11) in assets/site.css:\n" + "\n".join(failures)
    )


def test_keyboard_focus_is_styled_and_motion_is_opt_in() -> None:
    source = STYLESHEET.read_text(encoding="utf-8")
    for control in (".filter:focus-visible", ".practice-entry:focus-visible", "button:focus-visible"):
        assert control in source, f"assets/site.css must give {control} a visible focus indicator"

    assert "@media (prefers-reduced-motion: no-preference)" in source, (
        "the card entrance animation must be opt-in under prefers-reduced-motion: no-preference"
    )
    base = re.search(r"\.question-card \{([^}]*min-height[^}]*)\}", source)
    assert base, "assets/site.css no longer has a base .question-card rule"
    assert "animation" not in base.group(1), (
        "`.question-card` still animates unconditionally; move `animation: enter` inside the "
        "prefers-reduced-motion: no-preference block"
    )


def test_the_browser_is_told_which_themes_exist() -> None:
    """`color-scheme` is what themes form controls, scrollbars, and the canvas.

    Without it the browser paints native widgets and the scrollbar for the
    light theme regardless, so a dark page grows a bright scrollbar and a white
    text caret. It is not a custom property, so it is read from the blocks
    directly rather than from the parsed palette.
    """
    text = STYLESHEET.read_text(encoding="utf-8")
    light = re.search(r":root \{(.*?)\n\}", text, re.DOTALL)
    dark = re.search(
        r"@media \(prefers-color-scheme: dark\) \{\s*:root \{(.*?)\n  \}", text, re.DOTALL
    )
    assert light and "color-scheme: light" in light.group(1), (
        ":root must declare `color-scheme: light`"
    )
    assert dark and "color-scheme: dark" in dark.group(1), (
        "the dark palette must declare `color-scheme: dark`, or the browser keeps painting "
        "native controls and the scrollbar light"
    )


def main() -> None:
    test_every_colour_declaration_is_checked()
    test_no_colour_is_defined_only_in_a_media_query()
    test_no_rule_paints_a_raw_colour()
    test_text_meets_the_contrast_floor_in_both_themes()
    test_indicators_meet_the_non_text_floor_in_both_themes()
    test_keyboard_focus_is_styled_and_motion_is_opt_in()
    test_the_browser_is_told_which_themes_exist()
    print(
        f"Checked {len(PAIRINGS)} colour pairings and {len(INDICATORS)} indicators "
        f"against WCAG AA in {len(THEMES)} themes."
    )


if __name__ == "__main__":
    main()
