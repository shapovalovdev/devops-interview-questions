---
title: Define an internal developer platform
theme: platform-engineering
difficulty: junior
type: theory
tags: [platform-engineering, internal-developer-platform, architecture, self-service]
sources:
  - url: https://tag-app-delivery.cncf.io/whitepapers/platforms/
    source_type: standard
    verified_on: 2026-08-11
---

# Define an internal developer platform

What is an internal developer platform, and how is it different from the collection of tools a company already runs?

## Answer guide

- The CNCF Platforms White Paper defines a platform for cloud-native computing as a curated, integrated set of capabilities offered as an internal product to development teams, with the platform's own interfaces, documentation, and support. The distinguishing word is *curated*: the platform is not the inventory of every tool in the company, it is the deliberately chosen subset that has been wired together, given a supported interface, and made available without a ticket.
- Mechanically, a platform sits between application teams and the underlying capability providers — clusters, cloud accounts, CI systems, secret stores, databases. It exposes those through a platform interface: an API, a CLI, a template or scaffolder, a portal, or a declarative workload file such as Score. The team using it declares intent ("I need an HTTP service with a Postgres database and a public hostname") and the platform resolves that into the provider-specific resources, which is exactly the split the white paper calls capabilities versus interfaces.
- Constraints: a platform is only a platform if someone owns and operates it as a product with a roadmap, a support model, and stated compatibility promises. A shared Terraform module repository with no owner is a library, not a platform. The white paper is explicitly technology-neutral — Backstage, Crossplane and Score are common implementations, not part of the definition — and adopting one of those tools does not by itself create a platform.
- Failure modes: rebranding the existing operations ticket queue as a "platform" without changing the interaction model; building an interface that only wraps one provider so every new requirement becomes a platform change; letting the curated set grow until it is again the full tool inventory; and calling a single Kubernetes cluster the platform, so any team whose workload is not a container has no paved route at all.

## References

- [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Further reading (blog): [Backstage blog](https://backstage.io/blog)

## What to learn next

- Official documentation: [CNCF platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- Manual or specification: [Score specification reference](https://docs.score.dev/docs/score-specification/score-spec-reference/)
- Maintainer or personal blog: [Gregor Hohpe — The Architect Elevator](https://architectelevator.com/blog/)
- Technical blog: [Backstage blog](https://backstage.io/blog)
- Hands-on guide: [Backstage getting started](https://backstage.io/docs/getting-started/)
