---
title: Choose between CMD and ENTRYPOINT in a Docker image
theme: containers
difficulty: middle
type: theory
tags: [containers, docker, images]
---

# Choose between CMD and ENTRYPOINT in a Docker image

How do `CMD` and `ENTRYPOINT` interact, and which form best supports a container that accepts useful runtime arguments?

## Answer guide

- `ENTRYPOINT` defines the executable; `CMD` commonly supplies default arguments.
- Exec form avoids an unnecessary shell and provides predictable argument and signal handling.
- Design the image so users can override defaults without replacing its primary executable unintentionally.
