# Issue tracker: GitHub

Issues for this repository live as GitHub issues. Use the `gh` CLI for issue creation, reading, comments, labels, and closure.

Create ready work as GitHub issues and infer the repository from the configured Git remote.

## Local fallback

When the GitHub API is unavailable, the queue lives in [`docs/issues/`](../issues/README.md) as version-controlled Markdown, one file per issue, with a **Status** row the coordinator moves and a completion report appended on finish. It is the tracker of record while it is in use; push the files up as real issues once the API returns, keeping the numbering.
