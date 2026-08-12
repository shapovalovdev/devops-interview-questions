---
title: Place performance tests in CI
theme: testing-strategy
difficulty: senior
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://sre.google/sre-book/testing-reliability/
    source_type: official-docs
    verified_on: 2026-08-10
---

# Place performance tests in CI

You want a k6 load test to block merges when a change slows the API down. Every attempt so far either passed while latency regressed or failed for noise. How do you make the CI performance test trustworthy?

## Answer guide

- Separate the two jobs a performance test can do and run them differently. A short smoke-level test — a fixed low arrival rate for a couple of minutes with thresholds on `http_req_failed` and a p95 latency ceiling — runs on every pull request and answers whether the change broke something obvious. Capacity and soak tests answer how much load the system takes and run on a schedule against a production-like environment, because a shared CI runner cannot produce a meaningful number for that and pretending otherwise is where the false confidence comes from.
- Control the variables or the result is noise. Use a dedicated, consistently sized runner and target environment rather than a shared one; drive load with an open model (`constant-arrival-rate` in k6) so a slow system receives the same request rate instead of the closed-loop feedback that hides regressions; fix the dataset, cache state, and warm-up; and pin the load generator version. Express the gate as an explicit `thresholds` block in the script so k6 exits non-zero itself, rather than eyeballing a dashboard afterwards.
- Compare against a baseline, not an absolute. Run the candidate and the previous commit under the same conditions and gate on relative change with a band wide enough to absorb the environment's own variance, which you measure by running the same commit against itself several times. Alert on p95 and p99 rather than mean, since the mean absorbs exactly the tail that users feel, and record throughput and error rate alongside latency because a change that quietly sheds load can otherwise look like an improvement.
- Failure modes: a load generator saturating before the service does, so the test measures the runner; mocked dependencies that make the test measure only your process while the real bottleneck is the database; single-run comparison with no variance estimate, producing a gate that fails randomly and is disabled within a month; and a test that keeps passing because the threshold was raised each time it went red.

## References

- [Grafana k6 — automated performance testing](https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/)
- [Google SRE Book — testing for reliability](https://sre.google/sre-book/testing-reliability/)
- Further reading (blog): [Slack Engineering — continuous load testing](https://slack.engineering/continuous-load-testing/)

## What to learn next

- Official documentation: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/)
- Manual or specification: [Google SRE Book — testing for reliability](https://sre.google/sre-book/testing-reliability/)
- Maintainer or personal blog: [Brendan Gregg — active benchmarking](https://www.brendangregg.com/activebenchmarking.html)
- Technical blog: [Slack Engineering — continuous load testing](https://slack.engineering/continuous-load-testing/)
- Hands-on guide: [Grafana k6 — automated performance testing](https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/)
