# Procedure: push the local issue board to GitHub Issues

The GitHub Issues API returned 503s on 2026-08-17, so the queue for the Content API v1 epic was tracked in
this directory as version-controlled Markdown. This procedure moves it to real GitHub Issues once the API is
healthy again. It is written to be safe to run more than once.

Repository: `shapovalovdev/devops-interview-questions`.

## Steps

1. **Confirm the API is healthy.**

   ```bash
   gh api repos/shapovalovdev/devops-interview-questions --jq .full_name
   ```

   If this still fails with a 5xx, stop, change nothing, and report that the outage is ongoing.

2. **Read the board.** `README.md` in this directory is the index; every `0*.md` file is one issue — an H1
   title, a metadata table (Status, Label, Epic, Depends on, Branch), then the body.

3. **Check the milestone.** Milestone 10, `Content API v1`, should already exist:

   ```bash
   gh api repos/shapovalovdev/devops-interview-questions/milestones --jq '.[] | "\(.number) \(.title)"'
   ```

   Create it only if it is missing.

4. **Do not duplicate.** List existing issues and match on title before creating anything. If an issue
   already exists for a file, update that issue instead of opening a second one.

5. **Create one issue per file**, in numeric order, so the epic (`0000`) gets the lowest issue number.

   - Title: the file's H1, verbatim.
   - Body: the file's content, plus a line linking back to the source file on `main`.
   - Milestone: `Content API v1`.
   - Labels: the epic gets `enhancement` and `wayfinder:map`. Each slice gets `enhancement`, plus
     `ready-for-agent` only when its **Status** row says `ready-for-agent`.

   `gh issue create` resolves labels and milestones over GraphQL and can fail while REST is fine. On a
   GraphQL error, POST to `repos/shapovalovdev/devops-interview-questions/issues` with `gh api` instead.

6. **Rewrite the cross-references.** Once every issue exists, the local files' `Depends on` rows and the
   epic's slice table refer to `0001`–`0006`; replace them with the real issue numbers, in both the created
   GitHub issues and the Markdown files.

7. **Point the board at GitHub.** Update `README.md` here to link each row to its issue, and update the
   fallback note in `docs/agents/issue-tracker.md` to say the tracker is GitHub again. Update the epic
   reference in `AGENTS.md` and `CONTEXT.md` to the epic's issue URL.

8. **Commit on a branch and open a pull request** — do not push to `main` directly. Title it
   `Move the Content API v1 issue board to GitHub Issues`. Report in the PR body which issues were created,
   with their numbers and URLs.

## If the board has moved on

Statuses in these files change as agents finish work. Carry the current status across: an issue whose file
says `closed` should be created and then closed, with its completion report intact; one that says
`needs-review` gets the `needs-review` label. Never silently drop a completion report.
