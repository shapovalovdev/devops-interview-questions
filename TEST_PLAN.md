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

`config/content-manifest.json` is the single coverage contract. The CI validator
checks that every canonical Theme is declared, tracks its delivery state, and
enforces the exact 25-Question `5 junior / 10 middle / 5 senior / 5 staff`
mix for complete Themes. In-progress Themes may never exceed that target or
any difficulty allocation; overlapping Questions must be retired or reassigned
before the Theme is marked complete. Planned Themes cannot contain active
Questions. The same manifest declares every published certification tag, its
curriculum map, and its minimum mapped Question count. Certification IDs are
for tags and maps, never canonical Theme folders.

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

Certification-map invariants additionally require the published CCA curriculum map and at least 20 active Questions carrying the documented `cca` tag.

`tests/test_ckne_curriculum_map.py` guards the public CKNE development-program
map: official source and review date, all five published weighted domains,
original-content boundary, and explicit gap policy. CKNE is not activated in the
content manifest until its two remaining unique objectives and their catalog
entries are integrated together with the certification tag.

`tests/test_cnpe_curriculum_map.py` guards the CNPE public curriculum map: the
two official sources, all five weighted domains, the original-content boundary,
and the explicit no-duplicate decision. It also verifies that every mapped
canonical Question exists and retains source metadata, References, and a
complementary technical blog. CNPE remains unpublished as a filter until the
coordinator atomically integrates its tag, manifest entry, and catalog records.

`tests/test_cnpa_curriculum_map.py` guards the CNPA public curriculum map: its
official Linux Foundation source and six weighted domains, original-content
boundary, direct IDP/DORA gap policy, and source-verified canonical links. CNPA
is not activated as a filter until the coordinator atomically integrates its
tag, manifest entry, and catalog records.

The manifest currently includes the PCA and CAPA study paths, along with the
other published certification maps. Adding a certification requires one
manifest entry, a documented tag, a curriculum map, and mapped Questions;
otherwise CI fails.

## Delivery gate

The `Validate question database` GitHub Actions workflow runs the manifest,
content, certification-workflow, and website checks for pushes to `main` and
pull requests. GitHub Pages continues to publish from `main`; repository branch
protection can require this workflow before future merges.
