# Contributing questions

1. Write an original question or a substantive paraphrase; never copy source text verbatim.
2. Place the file in exactly one canonical folder under `questions/`.
3. Use the front-matter schema below and tags from [`TAGS.md`](./TAGS.md).
4. Include a short answer guide focused on concepts rather than one tool-specific command.
5. Add follow-ups only when they probe a meaningfully deeper skill.

```yaml
---
title: Short, specific question title
theme: canonical-theme
difficulty: junior | middle | senior | staff
type: theory | scenario | troubleshooting
tags: [normalized-tag, another-tag]
---
```

`staff` is a first-class difficulty, not an extension of `senior`: it marks a
Question about cross-system design, reliability, cost-risk trade-offs, or
technical leadership rather than isolated tool knowledge. Every canonical Theme's
Coverage target requires staff-level Questions, so leaving the band out is a
coverage gap rather than a stylistic choice.

## Running the checks

Everything below runs in CI on every pull request. Run it locally first.

The content and site checks are **standard-library only** and need no
installation — `tests/test_api_dependency_separation.py` enforces that, so
`tests/run_all_tests.py` and `scripts/build_site.py` must keep working with
nothing installed:

```bash
python tests/validate_content_manifest.py
python tests/validate_certification_question_workflow.py
python tests/validate_questions.py
python tests/validate_labs.py
python tests/test_theme_coverage_policy.py
python tests/validate_learning_resources.py --check-live
python tests/run_all_tests.py
python -m contentdb.drift
```

The Content API suite needs the service and test dependencies. Install them into
a virtual environment so they stay out of the standard-library checks:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip -r requirements-dev.txt

pytest --cov=api --cov=contentdb --cov-branch --cov-fail-under=95
```

Without those dependencies `pytest` fails while importing
`tests/api/conftest.py` with `ModuleNotFoundError: No module named 'fastapi'`.
That is the expected result outside the virtual environment, not a broken
checkout.

The website check additionally needs a headless browser:

```bash
python -m pip install playwright && python -m playwright install --with-deps chromium
python tests/site_check.py
```
