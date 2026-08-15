# Repository guidance

## Epic and release gate

Implementation work is only dispatched against a live epic and its release. The epic [Complete the learning-path catalog](https://github.com/shapovalovdev/devops-interview-questions/issues/120) and milestone [Learning paths v1](https://github.com/shapovalovdev/devops-interview-questions/milestone/1) closed 2026-08-15 — **there is no active epic; do not dispatch implementation work** until the next epic and milestone are charted with wayfinder and recorded in `CONTEXT.md` and here. Rules:

- Do not assign implementation work on an issue outside the current milestone; chart a new epic and milestone first (wayfinder, with the repository owner).
- When the milestone closes, stop dispatching until a new epic and release are charted and recorded in `CONTEXT.md` and here.
- Update both this section and `CONTEXT.md`'s "Goal and current epic" whenever the epic or release changes.

## Autonomous task loop

For every implementation task:

1. Create or identify a dedicated GitHub issue with acceptance criteria, including automated-test coverage.
2. Spawn one dedicated subagent for that issue; do not mix unrelated Themes in one agent task.
3. Require the subagent to run local validation, push its commit, and report the CI run.
4. A coordinator agent checks finished subagents, validates the shared worktree and CI, closes only verified issues, and assigns the next queued issue immediately.

Keep a maximum of three implementation subagents active at once. Resolve shared catalog or validator conflicts centrally before assigning replacement work.

The active-session cadence and GitHub Actions boundary are defined in [Codex coordinator loop](docs/agents/codex-coordinator-loop.md). The coordinator checks status at least every 10 minutes while the Codex session is active; Actions validates and publishes but never spawns agents.

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
