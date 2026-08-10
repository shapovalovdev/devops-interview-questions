---
title: Reduce a serverless deployment package and its dependency weight
theme: serverless
difficulty: middle
type: scenario
tags: [cloud, performance, dependencies, deployment, supply-chain]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-zip.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Reduce a serverless deployment package and its dependency weight

A function's package has grown until deploys are slow and cold starts hurt. How do you shrink it without breaking the runtime contract?

## Answer guide

- Measure before cutting. Produce a size breakdown per dependency and separate three costs that people conflate: archive size (affects upload and deploy time), uncompressed size (counts against the platform quota), and the bytes actually loaded and initialised at import time (the part that shows up as cold-start latency).
- The usual wins are mechanical: exclude tests, docs, type stubs, and source maps; ship only the runtime dependencies rather than the whole development tree; drop libraries the platform's runtime already provides; and prefer a narrowly scoped client package over a monolithic SDK. Tree-shaking and bundling help interpreted runtimes most, because they cut module-resolution work as well as bytes.
- Structural options change the trade-off rather than the number. Shared layers deduplicate common dependencies across functions but add a versioning and compatibility surface; container-image packaging raises the size ceiling substantially and gives you normal image tooling, at the cost of a different caching model. Splitting one oversized function into several narrower ones is often the honest fix.
- Native extensions must match the platform's architecture and libc, so build them in a matching image rather than on a developer laptop. Pin dependency versions and keep a lockfile, because a silent transitive upgrade is the most common cause of a package that suddenly stops fitting.
- Failure modes to expect: an architecture-mismatched binary wheel that fails only at runtime, a layer updated underneath a function that was never retested, aggressive bundling that breaks dynamic imports or reflection, and lazily importing a heavy module inside the handler, which moves cold-start cost onto the first real request instead of removing it.

## References

- [Deploying Lambda functions with .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-zip.html)
- Further reading (blog): [AWS Compute Blog — packaging and performance articles](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
- Manual or specification: [AWS Lambda API reference — PublishLayerVersion](https://docs.aws.amazon.com/lambda/latest/api/API_PublishLayerVersion.html)
- Maintainer or personal blog: [Yan Cui — theburningmonk on function packaging and cold starts](https://theburningmonk.com/)
- Technical blog: [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)
- Hands-on guide: [Create a Lambda container image](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)
