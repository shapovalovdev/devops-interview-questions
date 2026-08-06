# Repository guidance

## Autonomous task loop

For every implementation task, create a dedicated GitHub issue with testable acceptance criteria, then spawn exactly one dedicated subagent to work it. Require that agent to add or update automated tests, run local validation, push its commit, and report the CI result.

The coordinator validates finished agents, integrates shared changes, closes verified issues, and immediately assigns the next queued issue. Keep no more than three implementation agents active. Resolve shared catalog and validator changes centrally before replacing an agent.

No task is complete until repository validation and GitHub Actions pass.

## Agent skills

### Issue tracker

Issues live in this repository's GitHub Issues. See `docs/agents/issue-tracker.md`.

### Triage labels

Uses the standard five labels. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context repository using root `CONTEXT.md`. See `docs/agents/domain.md`.
