# Codex coordinator loop

The Codex coordinator is the repository's active-session work dispatcher. It keeps the Question delivery queue moving without using GitHub Actions to spawn agents.

## Cadence

While the Codex session is active, the coordinator checks the work queue at least every 10 minutes and whenever an agent reports completion. It must:

1. inspect active subagents and their completion reports;
2. validate the shared worktree, relevant automated tests, and GitHub Actions state;
3. integrate safe, verified changes and resolve shared catalog or validator conflicts centrally;
4. post the required GitHub issue completion report and close only genuinely complete issues;
5. assign the highest-priority unblocked `ready-for-agent` issue to each available subagent slot.

The coordinator may run at most three implementation subagents at once. Each implementation task still requires one dedicated GitHub issue, one dedicated subagent, automated-test coverage, source verification, and a published Pages result.

## Boundary with GitHub Actions

GitHub Actions is a validator and publisher only. The `Coordinator health check` workflow can report repository health, but it must not attempt to create or dispatch Codex subagents. Agent assignment requires an active Codex session.

This means the 10-minute cadence is ready and enforced by the active Codex coordinator, but it is not a persistent unattended service after the session ends. To continue autonomously later, start or resume a Codex session and instruct it to run the coordinator loop.
