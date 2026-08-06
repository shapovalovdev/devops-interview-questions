---
title: Distinguish a container image from a running container
theme: containers
difficulty: junior
type: theory
tags: [containers, docker, images]
---

# Distinguish a container image from a running container

What is the difference between a container image and a container created from it?

## Answer guide

- An image is an immutable layered filesystem and configuration metadata.
- A container is a runtime instance with a writable layer and isolated process view.
- Multiple containers can start from one image without sharing writable layers.
- Persistent state should normally live outside the container writable layer.
