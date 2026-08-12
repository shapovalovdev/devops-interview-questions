---
title: Decide whether a Backstage capability belongs in a frontend or backend plugin
theme: backend-architecture
difficulty: senior
type: scenario
tags: [architecture, platform-engineering, security, least-privilege, automation]
sources:
  - url: https://backstage.io/docs/backend-system/architecture/plugins/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://backstage.io/docs/frontend-system/architecture/plugins
    source_type: official-docs
    verified_on: 2026-08-12
---

# Decide whether a Backstage capability belongs in a frontend or backend plugin

A team wants their deployment tool surfaced in the developer portal: engineers
should see recent deployments on a service page and be able to trigger a
redeploy. Where does that logic go in a Backstage plugin, and how do you decide
between extending an existing plugin and writing a new one?

## Answer guide

- Anything that needs a credential, talks to a system the browser should not reach directly, or must be authorized belongs in a backend plugin; what renders in the page belongs in a frontend plugin. For this example the deployment API client, the token, and the authorization check for "may this user redeploy" live in a backend plugin, and the frontend plugin contributes the service-page card and the button that calls it. Splitting it the other way puts a deployment credential into a bundle you ship to every browser.
- The two systems are shaped differently and that shapes the decision. A backend plugin is created with `createBackendPlugin`, carries a plugin ID matching its package name, declares the services it needs by dependency injection, and is installed with `backend.add()`; the documentation treats each one as close to a separate microservice that communicates over the network. A frontend plugin is a collection of extensions built from blueprints and attached to the app declaratively, so a plugin is a unit of packaging and routing rather than a running process.
- Prefer extending over forking. Both systems publish deliberate seams — extension points that a backend plugin exposes for modules to hook into, and extension blueprints that let a frontend plugin add a card, tab, or route to an existing page — and using them keeps you on the upgrade path. Write a new plugin when the capability owns its own data, routes, or lifecycle; write a module or an extension when you are adding behaviour to something that already exists. Configuration alone is the cheapest option when it is sufficient.
- The failure modes are asymmetric. A misplaced backend concern leaks secrets or lets the browser call an internal system directly. A misplaced frontend concern is cheaper but produces a page that fetches from many origins, breaks under CORS, and cannot be authorized consistently. Both systems have live migrations from their legacy predecessors, so a plugin written against the old APIs is a maintenance debt with a known due date, and a plugin patched by editing a copy of upstream code will block the next upgrade.

## References

- [Backstage: backend plugins](https://backstage.io/docs/backend-system/architecture/plugins/)
- [Backstage: frontend plugins](https://backstage.io/docs/frontend-system/architecture/plugins)
- Further reading (blog): [Backstage blog: Backstage Backend System Alpha](https://backstage.io/blog/2023/02/15/backend-system-alpha/)

## What to learn next

- Official documentation: [Backstage: backend extension points](https://backstage.io/docs/backend-system/architecture/extension-points)
- Manual or specification: [Backstage: frontend extension blueprints](https://backstage.io/docs/frontend-system/architecture/extension-blueprints)
- Maintainer or personal blog: [From zero to maintainer: my open source journey with Backstage](https://backstage.io/blog/2025/05/12/from-zero-to-maintainer-my-opensource-journey-with-backstage)
- Technical blog: [Backstage blog: releasing Backstage Search 1.0](https://backstage.io/blog/2022/07/19/releasing-backstage-search-1.0/)
- Hands-on guide: [Backstage: create a plugin](https://backstage.io/docs/plugins/create-a-plugin)
