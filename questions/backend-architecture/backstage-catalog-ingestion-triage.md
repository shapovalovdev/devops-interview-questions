---
title: Diagnose why a service never appears in the Backstage catalog
theme: backend-architecture
difficulty: senior
type: troubleshooting
tags: [architecture, platform-engineering, troubleshooting, automation, governance, cba]
sources:
  - url: https://backstage.io/docs/features/software-catalog/life-of-an-entity/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://backstage.io/docs/features/software-catalog/external-integrations/
    source_type: official-docs
    verified_on: 2026-08-12
---

# Diagnose why a service never appears in the Backstage catalog

A team says they added a `catalog-info.yaml` to their repository a week ago and
their service still is not in the portal. Another team says their service showed
up but then vanished. How would you work out what happened in each case, and
what does the catalog actually do with an entity file?

## Answer guide

- Work backwards along the pipeline: is anything telling the catalog about this file at all, did the file get read, did processing succeed, and did the result survive stitching. Nothing appears unless an entity provider emits it — the two that ship by default cover user-registered locations and entries listed statically in `app-config` — so a `catalog-info.yaml` that nobody registered and no discovery provider scans is simply invisible, which explains the first team.
- The mechanism is a loop, not an import. A provider maintains its own set of entities and emits changes; unprocessed entities are picked up by registered processors that can rewrite them and emit further entities, relations, or errors; a stitching step then merges the processed entity with its relations and errors into the object the API and UI serve. Processing never deletes, it only creates or updates, and the whole thing is timestamp-driven and shared across catalog hosts, so a change is eventually consistent rather than immediate.
- Annotations are the contract that makes the rest work, and they are also where most silent breakage lives. Well-known annotations bind an entity to its source location, its documentation, and its external systems, and plugins read them to decide what to render; a typo in one produces an entity that exists but shows nothing useful. The disappearing service is usually the orphan path: when a parent entity stops emitting a child, the child is marked with `backstage.io/orphan` and, under the default strategy, removed — set `catalog.orphanStrategy: keep` only if you would rather keep stale records than lose them.
- Practical triage: check the entity's status field and the error table surfaced in the UI before reading logs, since validation and processor errors land there; confirm which provider claims the entity rather than assuming discovery covers the repository; and expect scale problems to look like staleness, because a provider that re-emits everything on each cycle grows slower and heavier until refreshes stop keeping up.

## References

- [Backstage: The Life of an Entity](https://backstage.io/docs/features/software-catalog/life-of-an-entity/)
- [Backstage: External integrations](https://backstage.io/docs/features/software-catalog/external-integrations/)
- Further reading (blog): [Backstage blog: scaling ingestion with incremental entity providers](https://backstage.io/blog/2023/01/31/incremental-entity-provider)

## What to learn next

- Official documentation: [Backstage: well-known annotations](https://backstage.io/docs/features/software-catalog/well-known-annotations/)
- Manual or specification: [Backstage: descriptor format](https://backstage.io/docs/features/software-catalog/descriptor-format/)
- Maintainer or personal blog: [Backstage Wrapped 2024](https://backstage.io/blog/2024/12/18/backstage-wrapped-2024)
- Technical blog: [The New York Times — migrating legacy services to a modern developer portal](https://backstage.io/blog/2025/08/08/migrating-legacy-services-to-a-modern-developer-portal)
- Hands-on guide: [Backstage: catalog configuration](https://backstage.io/docs/features/software-catalog/configuration/)
