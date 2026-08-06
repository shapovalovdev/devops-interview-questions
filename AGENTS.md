# Repository guidance

## Autonomous task loop

For every implementation task:

1. Create or identify a dedicated GitHub issue with acceptance criteria, including automated-test coverage.
2. Spawn one dedicated subagent for that issue; do not mix unrelated Themes in one agent task.
3. Require the subagent to run local validation, push its commit, and report the CI run.
4. A coordinator agent checks finished subagents, validates the shared worktree and CI, closes only verified issues, and assigns the next queued issue immediately.

Keep a maximum of three implementation subagents active at once. Resolve shared catalog or validator conflicts centrally before assigning replacement work.

Every Question task must update or extend automated validation for its new behavior. A task is not complete until the repository test suite and GitHub Actions pass.

## Published site and completion report

The public database is published at `https://shapovalovdev.github.io/devops-interview-questions/`.

After every task finishes, post a completion comment on its GitHub issue containing:

- the GitHub Pages URL and the relevant Theme or certification page;
- the commit SHA or pull request;
- the successful GitHub Actions URL;
- Question count and verification status;
- any required human review state.

Keep every queued issue eligible for automatic assignment. The coordinator fills each available agent slot from the highest-priority unblocked issue.

## Agent skills

### Issue tracker

Issues live in this repository's GitHub Issues. See `docs/agents/issue-tracker.md`.

### Triage labels

Uses the standard five labels. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context repository using root `CONTEXT.md`. See `docs/agents/domain.md`.
