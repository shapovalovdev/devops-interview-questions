# Repository guidance

## Autonomous task loop

For every implementation task, create a dedicated GitHub issue with testable acceptance criteria, then spawn exactly one dedicated subagent to work it. Require that agent to add or update automated tests, run local validation, push its commit, and report the CI result.

The coordinator validates finished agents, integrates shared changes, closes verified issues, and immediately assigns the next queued issue. Keep no more than three implementation agents active. Resolve shared catalog and validator changes centrally before replacing an agent.

No task is complete until repository validation and GitHub Actions pass.

## Published site and completion report

The public database is published at `https://shapovalovdev.github.io/devops-interview-questions/`.

After each task, comment on its GitHub issue with the Pages URL, relevant Theme or certification link, commit or pull request, successful CI URL, Question count, verification result, and any required human-review state. The coordinator assigns the highest-priority unblocked queued issue whenever an agent slot becomes free.

## Agent skills

### Issue tracker

Issues live in this repository's GitHub Issues. See `docs/agents/issue-tracker.md`.

### Triage labels

Uses the standard five labels. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context repository using root `CONTEXT.md`. See `docs/agents/domain.md`.
