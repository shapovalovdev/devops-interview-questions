# Version Control: related materials

Use the Git manual pages and direct References in each Question for factual
claims. These five resources give a practical learning path for recovering from
bad changes without confusing a shared-history recovery with a local rewrite.

## What to learn next

- Official documentation: [Git documentation](https://git-scm.com/doc)
- Manual or specification: [Git: git-revisions](https://git-scm.com/docs/gitrevisions)
- Maintainer or personal blog: [Julia Evans — confusing Git terminology](https://jvns.ca/blog/2023/11/01/confusing-git-terminology/)
- Technical blog: [GitHub Blog — undo almost anything with Git](https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/)
- Hands-on guide: [Learn Git Branching](https://learngitbranching.js.org/)

## Legal free books

- [Pro Git](https://git-scm.com/book/en/v2) is published online by the Git
  project under the Creative Commons Attribution Non Commercial Share Alike
  3.0 license. Its history-rewriting and recovery chapters are especially
  useful after working through the reset and revert manuals.

## Suggested study order

First learn how commits, references, and the working tree relate. Practice
reset and revert on a disposable repository, then use the Git manual to decide
whether a shared branch needs an additive revert or an explicitly coordinated
history rewrite.
