---
title: Control end-to-end test scope
theme: testing-strategy
difficulty: middle
type: scenario
tags: [testing-strategy, quality, reliability, delivery]
sources:
  - url: https://playwright.dev/docs/best-practices
    source_type: official-docs
    verified_on: 2026-08-10
  - url: https://abseil.io/resources/swe-book/html/ch14.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Control end-to-end test scope

The browser suite has grown to 400 Playwright specs, runs for fifty minutes, and fails for a non-product reason about once per run. Which journeys should stay end-to-end, and where does the rest of that coverage go?

## Answer guide

- Keep end-to-end coverage for the handful of journeys where the integration itself is the risk and no cheaper test can observe the failure: authentication, checkout or payment, and the one or two flows whose breakage pages someone. Google's testing guidance and the test-pyramid literature agree that beyond a small fraction of total tests, spend buys more one layer down. Everything else moves to component tests with the network layer stubbed, or to API-level tests that hit a real backend without a browser.
- Scope each surviving spec to one user-visible outcome and make it self-sufficient. Create its data through the API rather than by driving the UI, authenticate by injecting saved storage state instead of replaying the login form in every test, and never let one spec depend on another's ordering or leftovers. Assert through user-visible roles and text with auto-retrying web-first assertions rather than CSS selectors and fixed sleeps, which is where most timing flake originates.
- Manage runtime and signal explicitly: shard across runners, set per-test and per-assertion timeouts so a hung spec fails fast, and capture trace, video, and console output on failure so a red run is diagnosable from artifacts rather than by rerunning locally. Track flake rate per spec as a first-class metric with an owner, because a suite that is red half the time stops being a gate no matter what the policy document says.
- Failure modes: the ratchet where every incident adds one more end-to-end test, growing runtime without narrowing risk; specs that reach into internal state through the UI and break on every redesign; a suite pinned to a shared environment whose other tenants cause most failures; and the gate being made advisory under release pressure, after which nobody restores it.

## References

- [Playwright — best practices](https://playwright.dev/docs/best-practices)
- [Software Engineering at Google — larger testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Further reading (blog): [Google Testing Blog — just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)

## What to learn next

- Official documentation: [Playwright — best practices](https://playwright.dev/docs/best-practices)
- Manual or specification: [Software Engineering at Google — larger testing](https://abseil.io/resources/swe-book/html/ch14.html)
- Maintainer or personal blog: [Toby Clemson — testing strategies in a microservice architecture](https://martinfowler.com/articles/microservice-testing/)
- Technical blog: [Google Testing Blog — just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)
- Hands-on guide: [Playwright — writing tests](https://playwright.dev/docs/writing-tests)
