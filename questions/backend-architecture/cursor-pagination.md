---
title: Design cursor pagination
theme: backend-architecture
difficulty: middle
type: theory
tags: [databases, performance, http]
sources:
  - url: https://www.postgresql.org/docs/current/queries-limit.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design cursor pagination

Why is a cursor often safer than an offset for a changing, large collection?

## Answer guide

- A cursor encodes the ordered position after the last returned item, normally using a stable sort key plus a unique tie breaker. Query the next page with a keyset predicate and return an opaque, signed or validated cursor rather than internal query syntax.
- Specify the sort order, maximum page size, filtering compatibility, expiry, and whether the result is a snapshot or may change while clients page. Back the order with an index and monitor query plans and tail latency.
- Offset pagination can grow expensive and can skip or duplicate items when rows are inserted or deleted. Cursor pagination also fails if its ordering is not total or its cursor leaks trust boundaries; test concurrent writes, invalid cursors, and schema upgrades.

## References

- [PostgreSQL: LIMIT and OFFSET](https://www.postgresql.org/docs/current/queries-limit.html)
- Further reading (blog): [Shopify: relative cursor pagination](https://shopify.engineering/pagination-relative-cursors)

## What to learn next

- Official documentation: [PostgreSQL indexes](https://www.postgresql.org/docs/current/indexes.html)
- Manual or specification: [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- Maintainer or personal blog: [Brandur Leach's blog](https://brandur.org/)
- Technical blog: [Shopify Engineering](https://shopify.engineering/)
- Hands-on guide: [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
