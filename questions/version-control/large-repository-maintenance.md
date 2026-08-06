---
title: Keep a large Git repository operable
theme: version-control
difficulty: senior
type: scenario
tags: [git, version-control, performance, operations]
sources:
  - url: https://git-scm.com/docs/git-gc
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://git-scm.com/docs/git-maintenance
    source_type: official-docs
    verified_on: 2026-08-06
---

# Keep a large Git repository operable

What would you measure and change when a large repository becomes slow to clone, fetch, or inspect?

## Answer guide

- Measure clone, fetch, status, log, checkout, CI checkout, object count, pack size, and user-visible latency before changing workflow. Separate history size, large binary assets, path count, ref count, and network constraints because they require different remedies.
- Use supported maintenance, packing, commit-graph, partial-clone, sparse-checkout, or large-file mechanisms where they fit the repository and hosting platform. Test developer tooling and build scripts with each optimization.
- Establish ownership and budgets for generated artifacts, vendored dependencies, and binaries. Keep release artifacts in an artifact store rather than indefinitely adding them to normal source history when that meets retention requirements.
- Do not rewrite public history merely to reduce size without migration planning. It disrupts every clone, reference, automation integration, and audit record.

## References

- [Git documentation: git-gc](https://git-scm.com/docs/git-gc)
- [Git documentation: git-maintenance](https://git-scm.com/docs/git-maintenance)
- Further reading (blog): [GitHub Blog — improving Git performance](https://github.blog/open-source/git/)

## What to learn next

- Official documentation: [Git: git-maintenance](https://git-scm.com/docs/git-maintenance)
- Manual or specification: [Pro Git: maintenance and data recovery](https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery)
- Maintainer or personal blog: [Derrick Stolee's Git blog](https://stolee.dev/)
- Technical blog: [GitHub Blog — Git performance](https://github.blog/open-source/git/)
- Hands-on guide: [Git: partial clone](https://git-scm.com/docs/partial-clone)
