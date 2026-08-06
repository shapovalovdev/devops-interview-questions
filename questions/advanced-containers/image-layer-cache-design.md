---
title: Design a Dockerfile for predictable cache reuse
theme: advanced-containers
difficulty: middle
type: scenario
tags: [docker, images, containers, automation]
---

# Design a Dockerfile for predictable cache reuse

How would you organize a Dockerfile so routine source changes do not invalidate expensive dependency-install layers?

## Answer guide

- Order instructions from stable inputs to frequently changing inputs.
- Copy dependency manifests and install dependencies before copying application source.
- Use a suitable `.dockerignore` to minimize changed build context.
- Prefer multi-stage builds so build tooling stays out of the runtime image.
