---
title: Trace a DNS lookup from an application to an answer
theme: networking
difficulty: middle
type: theory
tags: [dns, networking, troubleshooting]
---

# Trace a DNS lookup from an application to an answer

What happens when an application resolves a hostname, and where can you investigate when resolution fails?

## Answer guide

- The local resolver checks configured local sources and cache.
- It queries a recursive resolver, which uses cache or authoritative nameservers.
- Record types and TTLs matter; stale cache and bad search domains are common problems.
- Inspect resolver configuration, query results, network reachability, and application caches separately.
