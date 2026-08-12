---
title: Make platform documentation discoverable
theme: platform-engineering
difficulty: junior
type: theory
tags: [platform-engineering, documentation, backstage, developer-experience]
sources:
  - url: https://backstage.io/docs/features/techdocs/
    source_type: official-docs
    verified_on: 2026-08-11
---

# Make platform documentation discoverable

Where should platform documentation live so that developers actually find it at the moment they need it?

## Answer guide

- Documentation that a developer has to remember to go and look for has already failed. The rule that works is: docs live next to the thing they describe, are built from that repository, and are surfaced in the same place the developer is already standing. Backstage TechDocs implements exactly this docs-like-code pattern — Markdown lives in the component's own repository with an `mkdocs.yml`, a build step turns it into a site, and it is rendered inside the catalog entry for that component.
- The mechanism has three parts: authoring in the source repository so a change and its documentation move in the same pull request; a generator and a storage location, which TechDocs supports as either local build-on-demand or a CI-built bundle in object storage; and an entity annotation (`backstage.io/techdocs-ref`) that binds the built docs to the catalog entry so search and the component page can reach them. Recommended production setup is the CI-built variant, because building on demand puts generator toolchains and repository credentials in the request path.
- Constraints: discoverability is search plus entry points, not a table of contents. Give every capability one canonical page, make the error messages and CLI output print the URL of the page that explains them, and keep a single owner annotation so a reader knows who to ask. Docs need the same deprecation discipline as code; an accurate page and a stale page that both rank in search are worse than one page.
- Failure modes: three sources of truth — a wiki, a README, and a Slack pin — that disagree; docs that describe the happy path and none of the failure output a developer actually sees; a docs build that fails silently in CI so the published page quietly freezes at last month's content; permissions that make the page unreachable for the contractors who need it most; and screenshots of a UI that changed two releases ago.

## References

- [Backstage TechDocs](https://backstage.io/docs/features/techdocs/)
- Further reading (blog): [Backstage blog](https://backstage.io/blog)

## What to learn next

- Official documentation: [Backstage TechDocs](https://backstage.io/docs/features/techdocs/)
- Manual or specification: [Backstage catalog descriptor format](https://backstage.io/docs/features/software-catalog/descriptor-format)
- Maintainer or personal blog: [Charity Majors — charity.wtf](https://charity.wtf/)
- Technical blog: [Backstage blog](https://backstage.io/blog)
- Hands-on guide: [Backstage getting started](https://backstage.io/docs/getting-started/)
