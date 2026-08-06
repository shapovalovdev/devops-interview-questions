---
name: certification-question-workflow
description: Build, review, or extend CNCF and Linux Foundation certification coverage in this DevOps Question database. Use whenever a user asks to add certification Questions, map a certification curriculum, fill certification coverage gaps, or prepare a certification issue for publication. It coordinates official-curriculum research, canonical certification tags, original practice Questions, question-verifier source and blog requirements, catalog integration, automated validation, CI, and GitHub issue lifecycle.
---

# Certification Question Workflow

Use this workflow to create ethical, maintainable certification study coverage. It produces original practice Questions mapped to the current official curriculum; it never reproduces real, leaked, confidential, or copyrighted exam questions.

Read these before making changes:

1. Root `CONTEXT.md` for Question, Theme, Tag, and certification-tag terminology.
2. `AGENTS.md` and `docs/agents/` for the required issue and subagent workflow.
3. `skills/question-verifier/SKILL.md` and `docs/research/source-policy.md` for answer and source standards.

## Intake and issue contract

For each certification program, identify or create one GitHub issue. Its acceptance criteria must state:

- the official program name and canonical short tag;
- the official curriculum URL and the date it was reviewed;
- every official domain or objective that needs coverage;
- whether each objective is covered by an existing Question, needs a new canonical Question, or needs a certification-specific Question because its task framing or required depth differs materially;
- original-content policy, `question-verifier` compliance, catalog integration, automated validation, CI, and closure conditions.

Label actionable work `ready-for-agent`. Keep review-gated work open and label it according to the repository triage vocabulary. Do not close an issue only because Markdown files were written.

## Map the official curriculum

1. Research the current official certification page using web/MCP tools. Prefer the program owner (CNCF, Linux Foundation, Kubernetes, or the named upstream project). Record the source URL, review date, and stated version or curriculum revision when available.
2. Create or update `docs/certifications/<program>.md`. State plainly that the map contains original practice material and is not an exam-content reproduction.
3. Create a table with each official domain/objective, its official weighting when published, and links to mapped Questions.
4. Recheck the official source immediately before final CI when the task took more than one day or when the program is marked changing/upcoming.

## Model Questions without duplication

Each Question has one canonical Theme folder. Use certification tags to make shared fundamentals appear in multiple study paths.

- Add a certification-specific Question only when the program requires substantially different scenario framing, operational scope, command/task context, or depth.
- Never clone the text of a shared Question merely to give it another certification tag.
- Keep Questions original or substantively paraphrased. Treat interview repositories, course notes, and practice tests as coverage inspiration only, never as text to copy or factual authority.
- Preserve the Theme progression: five junior, ten middle, five senior, and five staff-level Questions when completing a Theme target. Staff-level Questions should require system-wide design, risk/cost trade-offs, reliability strategy, or technical leadership.

## Add and verify Question files

For every new or materially revised Question:

1. Place it at `questions/<canonical-theme>/<slug>.md` and set front matter matching the folder Theme.
2. Add normalized Tags, including the certification tag and only relevant technical tags documented in `TAGS.md`.
3. Run the `question-verifier` workflow one Question at a time. Its full-answer standard requires a direct answer, mechanism, constraints or version caveats, and failure modes or trade-offs.
4. Include official/standards primary-source metadata with an HTTPS URL, permitted `source_type`, and ISO `verified_on` date.
5. Add a `## References` section containing a descriptive primary link and a separately labeled complementary technical blog post. The blog improves learning context; it is not factual proof.
6. Update existing shared Questions instead of creating near-duplicates when that is enough to map the new curriculum.

## Integrate discovery and enforce coverage

1. Add each active Question exactly once to `assets/questions.js`, using its Pages-rendered `.html` path.
2. Document the certification tag in `TAGS.md`.
3. Update the certification map with only canonical paths that actually carry the certification tag.
4. Extend `tests/validate_questions.py` whenever the program needs a durable invariant, such as a map file, tag existence, or a minimum mapped-Question count. Do not add a count that is unrelated to an official objective map.
5. Extend `TEST_PLAN.md` whenever the validation behavior changes.

## Validate, publish, and close

Run the repository checks locally:

```bash
python tests/validate_certification_question_workflow.py
python tests/validate_questions.py
python tests/site_check.py
```

Then commit only the task's changes, push the branch, and capture the GitHub Actions run that validates the commit. The coordinator resolves shared catalog or validator conflicts before replacing an agent.

Close the issue only after all of the following are true:

- the curriculum map is current and linked to official material;
- every mapped Question is original, tagged, source-verified, and has complementary reading;
- every active Question is discoverable in the website catalog;
- local validation and GitHub Actions pass; and
- the issue has a concise completion comment with the map, test/CI evidence, and any user-review status.

If the task is review-gated, publish the Questions but keep the issue open and explicitly state what the reviewer must inspect.

## Handoff report

Report the program, official curriculum source and review date, mapped/added Question count, canonical Themes affected, validation commands, CI run URL, and whether the issue was closed or intentionally left for review.
