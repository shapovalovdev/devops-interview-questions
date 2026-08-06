---
title: Govern a high-risk distributed state change
theme: distributed-systems
difficulty: staff
type: scenario
tags: [change-management, reliability, recovery]
sources:
  - url: https://sre.google/sre-book/reliable-product-launches/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern a high-risk distributed state change

How would you deploy a protocol, schema, or replication change whose rollback may not be instantaneous?

## Answer guide

- Separate compatibility preparation from activation. Introduce readers before writers, make old and new nodes interoperable, gate activation on measured preconditions, and preserve sufficient data and binaries to reverse the change or migrate forward safely.
- Use a small canary scope, explicit stop conditions, ownership, audit record, and rehearsal against representative failure modes. Observe correctness signals, lag, error budget, and irreversible writes, not merely deployment completion.
- A simple rollback can be unsafe after new data has been written. Skipping backups, assuming homogeneous fleet versions, or rolling all regions together can combine a latent compatibility bug with an unavailable recovery path and cause systemic data loss.

## References

- [Google SRE: reliable product launches](https://sre.google/sre-book/reliable-product-launches/)
- Further reading (personal blog): [Brandur Leach: online migrations](https://brandur.org/online-migrations)

## What to learn next

- Official documentation: [Kubernetes deployment strategies](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- Manual or specification: [Google SRE book](https://sre.google/sre-book/table-of-contents/)
- Maintainer or personal blog: [Brandur Leach's writing](https://brandur.org/)
- Technical blog: [GitHub Engineering: deployment](https://github.blog/engineering/)
- Hands-on guide: [Kubernetes canary with Argo Rollouts](https://argo-rollouts.readthedocs.io/en/stable/)
