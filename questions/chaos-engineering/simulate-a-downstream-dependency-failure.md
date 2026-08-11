---
title: Simulate a downstream dependency failure
theme: chaos-engineering
difficulty: middle
type: scenario
tags: [chaos-engineering, fault-injection, dependencies, resilience]
sources:
  - url: https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Simulate a downstream dependency failure

How do you test what happens when a service one layer down stops answering?

## Answer guide

- Decide which failure you mean, because they are not equivalent. Fast connection refusal, slow responses that end in a timeout, partial error rates, malformed or empty payloads, and a black hole that swallows packets without resetting all exercise different code paths. Blackholing and error injection are exactly the distinction the AWS Fault Injection Service action list draws, and a service that survives a clean refusal often collapses on silent packet drops.
- The point of the experiment is to classify the dependency. A critical dependency should degrade the journey visibly and predictably; a non-critical one should be shed with a fallback, a cached value, or a reduced feature. Most teams discover at least one dependency they described as optional that turns out to block a request path, and one described as critical that nobody has ever tested failing.
- Material constraints: the caller needs a finite timeout shorter than its own client's timeout, bounded retries with jitter, a bulkhead or connection-pool limit so one slow dependency cannot consume every worker, and a circuit breaker whose thresholds you have actually measured. Run the fault long enough for the breaker to open and then close again, since the recovery transition is where most defects live.
- Failure modes: fallbacks that call another unhealthy service, caches that were only warm because the dependency was healthy, retry storms that turn a partial outage into a total one, and a health check that keeps reporting green because it never touches the failed dependency. Verify recovery explicitly rather than assuming the fault's removal restores service.

## References

- [AWS Fault Injection Service actions reference](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)
- Further reading (blog): [Netflix Technology Blog](https://netflixtechblog.com/)

## What to learn next

- Official documentation: [AWS Fault Injection Service actions reference](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)
- Manual or specification: [Chaos Mesh — simulate network chaos on Kubernetes](https://chaos-mesh.org/docs/simulate-network-chaos-on-kubernetes/)
- Maintainer or personal blog: [Adrian Cockcroft — architecture and resilience writing](https://adrianco.medium.com/)
- Technical blog: [Gremlin blog](https://www.gremlin.com/blog)
- Hands-on guide: [AWS Builders' Library — avoiding fallback in distributed systems](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/)
