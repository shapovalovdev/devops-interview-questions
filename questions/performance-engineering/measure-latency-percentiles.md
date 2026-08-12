---
title: Why use latency percentiles instead of an average?
theme: performance-engineering
difficulty: junior
type: theory
tags: [performance, monitoring, debugging, capacity-planning]
sources:
  - url: https://prometheus.io/docs/practices/histograms/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Why use latency percentiles instead of an average?

A dashboard reports a mean request latency of 40 ms while support tickets say the product is slow. What does a percentile show that the mean hides, and how must percentiles be combined across many instances?

## Answer guide

- Request latency is right-skewed and usually multimodal (cache hit versus miss, fast path versus a garbage-collection pause), so the mean sits in a gap where few real requests live. The p99 names a request that actually happened, and it matters more than its 1% share suggests: a page that fans out to 100 backend calls touches the slow tail on almost every load.
- Percentiles are not additive. You cannot average the p99 of twenty instances, and you cannot average five one-minute p99 values into an hourly one. Correct aggregation adds histogram bucket counts across instances and time and computes the quantile once at the end, which is what `histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))` does. Client-side summary quantiles (a Prometheus Summary, StatsD percentiles) are already reduced inside each process and cannot be re-aggregated at all.
- A classic histogram is only as precise as its bucket edges, because the quantile is interpolated linearly inside the bucket that contains it; a p99 that lands in the final `[2.5s, +Inf)` bucket is reported at the finite edge and is effectively unbounded. Prometheus native histograms (experimental since 2.40) trade fixed edges for a relative-error factor. Sample count matters too: a p99 over 50 requests in the window is one request, so the number will swing wildly on low-traffic endpoints.
- The classic measurement failure is coordinated omission: a closed-loop generator or an instrumented client that stalls while blocked never issues the requests that would have been slow, so the recorded p99 flatters the system. Instrumenting only the handler excludes accept-queue, TLS handshake, and connection-pool wait, which is exactly where an overloaded service spends its time. Head-based trace sampling at 1% discards most tail exemplars, so keep a full histogram for the numbers and use tail-based sampling if you need the slow traces themselves.

## References

- [Prometheus: Histograms and summaries](https://prometheus.io/docs/practices/histograms/)
- Further reading (blog): [Brendan Gregg — Performance analysis methodology](https://www.brendangregg.com/methodology.html)

## What to learn next

- Official documentation: [OpenTelemetry metrics specification](https://opentelemetry.io/docs/specs/otel/metrics/)
- Manual or specification: [Prometheus histogram guidance](https://prometheus.io/docs/practices/histograms/)
- Maintainer or personal blog: [Brendan Gregg — Performance methodologies](https://www.brendangregg.com/methodology.html)
- Technical blog: [Cloudflare blog — Performance](https://blog.cloudflare.com/tag/performance/)
- Hands-on guide: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
