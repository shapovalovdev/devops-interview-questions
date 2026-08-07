---
title: Measure and improve tail latency
theme: observability
difficulty: senior
type: troubleshooting
tags: [observability, monitoring, reliability, troubleshooting, prometheus, pca]
sources:
  - url: https://prometheus.io/docs/practices/histograms/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Measure and improve tail latency

Average latency is stable, but users report occasional slowness. How do you investigate tail latency?

## Answer guide

- Measure latency distributions with a histogram and evaluate a high quantile appropriate to the user journey, segmented by operation, dependency, region, and workload where labels remain bounded.
- Correlate slow buckets with traces, saturation, queueing, garbage collection, connection pools, and downstream duration; compare before and after a release or traffic shift.
- Choose histogram buckets around SLO boundaries so quantile estimates are useful for the action you need to take.
- An average masks outliers, and a client-side summary cannot generally be aggregated across replicas. Do not promise an exact percentile when bucket granularity only permits an estimate.

## References

- Further reading (blog): [Complementary observability practice article](https://www.honeycomb.io/blog/the-lost-art-of-structured-logging)
- [Prometheus histogram and summary practices](https://prometheus.io/docs/practices/histograms/)
- [Further reading: Google SRE—Addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/)

## What to learn next

- Official documentation: [Prometheus histograms and summaries](https://prometheus.io/docs/practices/histograms/)
- Manual or specification: [Dean and Barroso — The Tail at Scale](https://research.google/pubs/the-tail-at-scale/)
- Maintainer or personal blog: [Brian Brazil — how does a Prometheus histogram work?](https://www.robustperception.io/how-does-a-prometheus-histogram-work/)
- Technical blog: [AWS Builders' Library](https://aws.amazon.com/builders-library/)
- Hands-on guide: [HdrHistogram — recording high-percentile latency](https://hdrhistogram.github.io/HdrHistogram/)
