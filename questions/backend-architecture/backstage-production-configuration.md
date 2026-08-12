---
title: Move a Backstage instance from local defaults to production configuration
theme: backend-architecture
difficulty: senior
type: scenario
tags: [architecture, platform-engineering, configuration-management, security, iam]
sources:
  - url: https://backstage.io/docs/conf/
    source_type: official-docs
    verified_on: 2026-08-12
  - url: https://backstage.io/docs/deployment/k8s
    source_type: official-docs
    verified_on: 2026-08-12
---

# Move a Backstage instance from local defaults to production configuration

A proof-of-concept Backstage portal has been running from a laptop for a month
and the organization now wants it available to everyone. Which parts of its
configuration must change before it is a production service, and how does
Backstage's configuration system make that safe or dangerous?

## Answer guide

- The changes that matter are the database, the URLs, the identity setup, and where secrets come from. The demo defaults keep catalog state in an in-memory or file database that is lost on restart; production points at PostgreSQL with real credentials. `app.baseUrl` and `backend.baseUrl` must both name the externally reachable address, and the auth provider's callback configuration has to agree with them or the sign-in pop-up never completes.
- The mechanism is layered static configuration. Backstage reads `app-config.yaml` first, then environment-specific files such as `app-config.production.yaml`, then local files, with later layers overriding earlier ones and all non-local files loaded before local ones. Values are plain YAML with `$env` and `$file` for injecting data that must not be committed, and the assembled configuration is validated against a JSON schema contributed by the installed plugins and packages.
- The constraint people miss is visibility. Configuration is backend-only by default, and a key reaches the browser only when its schema marks it as frontend-visible; that visibility is applied when the frontend bundle is built, so a frontend-visible value is effectively baked into the image rather than read per environment at start-up. Backend-only values, including database credentials and integration tokens, should arrive as environment variables from a secret store rather than being written into a committed file.
- Realistic failure modes: a portal that loses its catalog on every pod restart because nobody moved off the development database; sign-in that works locally and fails behind the ingress because the base URLs still say `localhost`; a token pasted into `app-config.yaml` and pushed to the repository; and a per-environment override placed in a layer that a later file silently overrides, which looks like the setting being ignored rather than being overwritten.

## References

- [Backstage: Static Configuration](https://backstage.io/docs/conf/)
- [Backstage: Deploying with Kubernetes](https://backstage.io/docs/deployment/k8s)
- Further reading (blog): [Backstage blog: The 2024 Backstage Security Audit](https://backstage.io/blog/2024/12/17/backstage-security-audit-2024)

## What to learn next

- Official documentation: [Backstage: writing configuration](https://backstage.io/docs/conf/writing)
- Manual or specification: [Backstage: defining configuration schema](https://backstage.io/docs/conf/defining)
- Maintainer or personal blog: [Backstage blog: New release: Backstage 1.0](https://backstage.io/blog/2022/03/17/backstage-1.0/)
- Technical blog: [GitGuardian — building your developer portal with Backstage, part 2](https://blog.gitguardian.com/platform-engineering-building-your-developer-portal-with-backstage-part-2/)
- Hands-on guide: [Backstage: building a Docker image](https://backstage.io/docs/deployment/docker)
