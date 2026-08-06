# <Program> certification coverage

## Goal

Map the current official <Program> curriculum to original practice Questions in the public DevOps Question database.

## Acceptance criteria

- [ ] Record the official curriculum URL, review date, and available version/revision in `docs/certifications/<program>.md`.
- [ ] Map every published domain or objective to canonical Question links and record official weightings where published.
- [ ] Use the `<program>` Tag on every mapped Question; reuse canonical shared Questions and add a distinct Question only for genuinely different framing or depth.
- [ ] Ensure every added or revised Question meets `question-verifier`: original prompt, full answer guide, primary-source metadata, descriptive primary reference, and labeled complementary blog post.
- [ ] Add every active Question once to `assets/questions.js` using the rendered `.html` path and document the Tag in `TAGS.md`.
- [ ] Add or extend durable certification validation and `TEST_PLAN.md` where needed.
- [ ] Pass `python tests/validate_certification_question_workflow.py`, `python tests/validate_questions.py`, `python tests/site_check.py`, and GitHub Actions.
- [ ] Comment with map and CI evidence; close only when all checks pass. Keep review-gated work open with explicit review instructions.

## Content policy

Questions are original practice material. Do not reproduce real, leaked, confidential, or copyrighted exam content.
