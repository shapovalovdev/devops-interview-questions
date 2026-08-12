---
title: Produce a reproducible Backstage backend image from its Yarn workspace
theme: ci-cd
difficulty: middle
type: scenario
tags: [ci-cd, containers, docker, build-cache, delivery, platform-engineering, cba]
sources:
  - url: https://backstage.io/docs/deployment/docker
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://backstage.io/docs/tooling/cli/build-system/
    source_type: official-docs
    verified_on: 2026-08-12
---

# Produce a reproducible Backstage backend image from its Yarn workspace

Your team runs a Backstage developer portal that a single engineer currently
builds on a laptop and pushes by hand. You have been asked to move that into CI
so every image is reproducible. Walk through the pipeline you would write and
say what makes a Backstage build different from packaging an ordinary Node
service.

## Answer guide

- The pipeline installs the workspace with a frozen lockfile, type-checks the repository, produces the backend deployment bundle, and only then builds an image whose final stage installs no development dependencies. Backstage ships a `yarn install --immutable`, `yarn tsc`, `yarn build:backend` sequence for exactly this, and the resulting `dist/bundle.tar.gz` plus `dist/skeleton.tar.gz` are what the Dockerfile copies in.
- What differs from a normal Node service is that the repository is one Yarn workspace treated as a single TypeScript compilation unit, not a package that compiles itself. Type declarations land in `dist-types` and are shared across packages, the frontend is bundled into static assets served by the backend, and the skeleton archive exists purely so the image can install dependencies in a layer that changes less often than application code.
- Two packaging routes are supported and they trade different things. A host build compiles outside Docker and is faster with better dependency caching, but it needs a CI runner with the right Node and Yarn already present. A multi-stage build does everything inside the image and is the option when Docker-in-Docker is unavailable, at the cost of a longer build. Either way the runtime stage needs the native build prerequisites the project actually uses — Python and a compiler toolchain for the scaffolder's isolated-VM dependency, SQLite headers only if SQLite is still in play — and `NODE_ENV=production`.
- The failures worth naming are a non-frozen install that silently resolves new transitive versions and makes yesterday's image unbuildable; skipping the full type check in CI because the incremental cache made it look green locally; a runtime image that still carries build tooling and source; and building without deciding how the frontend will be served, since the documented deployment has the backend serve the bundled frontend and splitting it onto its own static server later changes what the bundle has to be built with.

## References

- [Backstage: Building a Docker image](https://backstage.io/docs/deployment/docker)
- [Backstage: Build System](https://backstage.io/docs/tooling/cli/build-system/)
- Further reading (blog): [Backstage blog: New release: Backstage 1.0](https://backstage.io/blog/2022/03/17/backstage-1.0/)

## What to learn next

- Official documentation: [Backstage CLI commands](https://backstage.io/docs/local-dev/cli-commands/)
- Manual or specification: [Yarn workspaces](https://yarnpkg.com/features/workspaces)
- Maintainer or personal blog: [Backstage Wrapped 2025](https://backstage.io/blog/2025/12/30/backstage-wrapped-2025)
- Technical blog: [Spotify Engineering — what the heck is Backstage anyway?](https://engineering.atspotify.com/2020/03/what-the-heck-is-backstage-anyway)
- Hands-on guide: [Backstage: create an app](https://backstage.io/docs/getting-started/create-an-app)
