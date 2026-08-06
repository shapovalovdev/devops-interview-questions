---
title: Choose between Git revert and reset for a bad change
theme: version-control
difficulty: middle
type: scenario
tags: [git, version-control, delivery, troubleshooting]
---

# Choose between Git revert and reset for a bad change

A defective commit is already on a shared branch. When should you create a revert rather than rewriting history with reset?

## Answer guide

- Revert creates a new commit that safely negates an earlier change on a shared history.
- Reset rewrites local history and is appropriate only before sharing or with explicit coordinated recovery.
- Consider downstream branches, deployments, and whether the reversal itself is safe.
