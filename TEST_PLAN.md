# Test plan

## Goal

Prevent invalid Questions from being published and ensure the website exposes every active Question through a working Pages-rendered URL.

## Definition of an active Question

Every `*.md` file under `questions/<theme>/` is an active Question. It must appear exactly once in the website catalog.

## Automated checks

`tests/validate_questions.py` runs on every push and pull request. It validates every active Question for:

- complete YAML front matter;
- allowed `difficulty` and Question type values;
- canonical Theme matching its parent folder;
- at least one normalized Tag, with every Tag present in `TAGS.md`;
- an answer guide;
- a full answer guide: at least three answer bullets and 60 words, covering the
  direct answer, constraints, and operational guidance;
- primary-source metadata (HTTPS URL, permitted source type, and ISO verification
  date), a supporting reference, and a separately labeled complementary blog
  article;
- exactly one matching entry in the website catalog, using a Pages-rendered `.html` URL.

`tests/site_check.py` loads the public website interface locally in a headless browser. It verifies catalog rendering, search, theme filtering, and that all card links target `.html` pages.

`tests/validate_learning_resources.py` validates the staged curated-learning
audit. For every Question in `docs/research/link-audit-manifest.json`, it
requires exactly five categorized, unique HTTPS resources in `## What to learn
next`, validates the matching Theme related-materials page, and follows every
unique URL in CI. `tests/test_validate_learning_resources.py` covers the parser
rules for the five-category schema and duplicate-link rejection. The staged
rollout and the path to global enforcement are recorded in
`docs/research/link-audit-rollout.md`.

`tests/validate_certification_question_workflow.py` validates the reusable certification workflow itself: its official-curriculum mapping, canonical-tag, original-content, source-and-blog, catalog, validation, CI, and issue-closure requirements; its issue template; and realistic workflow eval prompts.

`tests/validate_questions.py` also requires the PCA certification tag, PCA map, and at least 25 active Questions carrying the canonical `pca` tag. This prevents the PCA study path from silently disappearing during catalog or content changes.

## Delivery gate

The `Validate question database` GitHub Actions workflow runs both checks for pushes to `main` and pull requests. GitHub Pages continues to publish from `main`; repository branch protection can require this workflow before future merges.
