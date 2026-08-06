---
title: Govern base images across product teams
theme: advanced-containers
difficulty: staff
type: scenario
tags: [containers, images, security, governance, supply-chain, platform-engineering]
sources:
  - url: https://docs.docker.com/build/building/best-practices/#choose-the-right-base-image
    source_type: official-docs
    verified_on: 2026-08-06
---

# Govern base images across product teams

How would you reduce base-image risk without blocking teams that need different language runtimes?

## Answer guide

- Publish maintained, documented base-image families with ownership, supported platforms, patch cadence, source/digest policy, and clear deprecation dates.
- Automate update proposals and compatibility testing, then let product teams own application-level acceptance. Central ownership cannot know every runtime behavior.
- Restrict or review unapproved bases based on exposure and risk, while retaining an exception process. A prohibition without an escape hatch encourages unofficial mirrors and stale images.
- Measure adoption, age of deployed base digests, unresolved critical findings, and migration lead time. Use those signals to invest in the most impactful shared images.

## References

- [Docker Docs: Choose the right base image](https://docs.docker.com/build/building/best-practices/#choose-the-right-base-image)
- Further reading (blog): [Docker: Intro guide to Dockerfile best practices](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)
