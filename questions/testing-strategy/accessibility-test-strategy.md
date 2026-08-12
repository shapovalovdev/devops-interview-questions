---
title: Design accessibility testing strategy
theme: testing-strategy
difficulty: junior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://www.w3.org/TR/WCAG22/
    source_type: standard
    verified_on: 2026-08-10
  - url: https://www.w3.org/WAI/standards-guidelines/wcag/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Design accessibility testing strategy

Your checkout flow scores 100 in Lighthouse's accessibility audit and legal has asked for evidence that it meets WCAG 2.2 AA. What can automated tooling actually prove, and what has to be tested another way?

## Answer guide

- Automated rule engines — axe-core, which drives Lighthouse's accessibility category, plus Pa11y or the Playwright axe integration — detect the machine-checkable subset of WCAG: missing `alt` attributes, controls with no accessible name, text contrast below the 4.5:1 ratio required for body copy at AA, duplicate `id` values, and invalid ARIA role and attribute combinations. Published estimates for how much of WCAG that subset represents range from about a third to Deque's claim of 57% for axe. Either way a clean run means no detected violations, not conformance.
- The remainder are judgements a rule cannot make: whether `alt` text conveys the image's purpose, whether focus order follows reading order, whether a custom widget's keyboard behaviour matches the ARIA pattern it claims, whether an inline error is announced, and whether the criteria new in 2.2 hold — 2.4.11 Focus Not Obscured, 2.5.8 Target Size (Minimum) at 24 by 24 CSS pixels, 3.3.7 Redundant Entry. Cover those with a keyboard-only pass, a screen-reader pass on the pairings you support (NVDA with Firefox, VoiceOver with Safari, JAWS with Chrome), and a 200% zoom and 320 CSS pixel reflow check.
- Wire the scan into CI against the critical journeys with a zero-new-violations gate over a recorded baseline, and run it on the rendered DOM after interaction — scanning the initial page misses modal dialogs, expanded menus, and validation states, which is where most real failures live. Keep the manual passes as a per-release checklist that feeds a WCAG 2.2 AA conformance record; a score is not evidence, an accessibility conformance report naming criteria, pass or fail, and method is.
- Failure modes worth naming: an axe run over a static build passing while the live single-page app is unusable with a keyboard; contrast rules skipped because the text sits on an image or gradient the tool refuses to sample; ARIA bolted on to silence a rule, so `role="button"` on a `div` with no `tabindex` or key handler trades a reported violation for a real one; and treating bug reports from disabled users as edge cases when they are the highest-value signal the programme produces.

## References

- [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C WAI — WCAG standards and guidelines overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
- Further reading (blog): [web.dev — Learn Accessibility course](https://web.dev/learn/accessibility)

## What to learn next

- Official documentation: [W3C WAI — WCAG standards and guidelines overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
- Manual or specification: [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- Maintainer or personal blog: [Manuel Matuzovic — building the most inaccessible site possible with a perfect Lighthouse score](https://www.matuzo.at/blog/building-the-most-inaccessible-site-possible-with-a-perfect-lighthouse-score/)
- Technical blog: [web.dev — Learn Accessibility course](https://web.dev/learn/accessibility)
- Hands-on guide: [web.dev — how to do an accessibility review](https://web.dev/articles/how-to-review)
