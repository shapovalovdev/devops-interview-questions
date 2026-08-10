---
title: Define ingress and gateway boundaries
theme: container-networking
difficulty: senior
type: scenario
tags: [containers, kubernetes, networking, http, security, reliability, cca, ckne]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/gateway/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Define ingress and gateway boundaries

What should a platform team decide before standardizing application ingress with Gateway API?

## Answer guide

- Define who owns Gateway infrastructure, listener addresses, certificates, TLS policy, route delegation, and incident response. Gateway API separates infrastructure configuration from application routing intent.
- Select an implementation whose supported API features and operational model match the cluster. The API does not itself supply a dataplane or guarantee identical controller behavior.
- Create guarded route attachment and cross-namespace rules, then test hostname, path, TLS, and backend failure behavior before migration.
- Avoid treating gateway adoption as a simple YAML rename from Ingress; external load balancers, security controls, and observability ownership can change.

## References

- [Kubernetes Docs: Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)
- Further reading (blog): [Kubernetes: Gateway API v1](https://kubernetes.io/blog/2023/10/31/gateway-api-ga/)
## What to learn next

- Official documentation: [Docker networking documentation](https://docs.docker.com/network/)
- Manual or specification: [CNI specification](https://www.cni.dev/docs/spec/)
- Maintainer or personal blog: [Thomas Graf — networking articles](https://tgraf.io/)
- Technical blog: [Cilium engineering blog](https://cilium.io/blog/)
- Hands-on guide: [Docker standalone networking tutorial](https://docs.docker.com/engine/network/tutorials/standalone/)
