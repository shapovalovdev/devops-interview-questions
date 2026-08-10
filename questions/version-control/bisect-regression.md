---
title: Use git bisect to find a regression
theme: version-control
difficulty: middle
type: troubleshooting
tags: [git, version-control, troubleshooting, debugging]
sources:
  - url: https://git-scm.com/docs/git-bisect
    source_type: official-docs
    verified_on: 2026-08-06
---

# Use git bisect to find a regression

How do you use `git bisect` to find the change that introduced a reproducible regression?

## Answer guide

- Start with a known bad commit and a known good ancestor, then let `git bisect` select midpoint commits. Mark each tested revision good or bad until Git identifies a candidate first bad commit.
- Automate the test with `git bisect run` when it returns reliable status codes, but first make the environment deterministic: pin dependencies, isolate external services, and define what an inconclusive or unbuildable revision means.
- Inspect the candidate's full change and surrounding commits, reproduce it again, and run the normal test and review path. Bisect identifies a boundary in history, not necessarily the entire root cause.
- Avoid using flaky end-to-end tests as a binary oracle. Skipped or unreliable revisions can mislead the search and should be documented or handled with a smaller deterministic test.

## References

- [Git documentation: git-bisect](https://git-scm.com/docs/git-bisect)
- Further reading (blog): [GitHub Blog — Git tips](https://github.blog/open-source/git/)

## What to learn next

- Official documentation: [Git: git-bisect](https://git-scm.com/docs/git-bisect)
- Manual or specification: [Pro Git: debugging with Git](https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git)
- Maintainer or personal blog: [Julia Evans — Git tips](https://jvns.ca/)
- Technical blog: [GitHub Blog — Git workflow](https://github.blog/open-source/git/)
- Hands-on guide: [Git: git-bisect run](https://git-scm.com/docs/git-bisect#Documentation/git-bisect.txt-run)
