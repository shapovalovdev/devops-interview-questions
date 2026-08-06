---
title: Explain database index trade-offs
theme: databases
difficulty: middle
type: theory
tags: [databases, postgresql, reliability, troubleshooting]
---

# Explain database index trade-offs

Why can an index speed up a query yet still make an application slower overall?

## Answer guide

- Indexes can reduce reads for matching queries.
- Each index consumes storage and adds work during inserts, updates, and deletes.
- Choose indexes from observed query patterns and verify plans and production impact.
