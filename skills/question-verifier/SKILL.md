---
name: question-verifier
description: Verify or improve DevOps interview Questions stored as Markdown. Use when adding, reviewing, or auditing Questions that need a full answer guide and authoritative external sources; validates answer completeness, source metadata, and reference quality.
---

# Question Verifier

Read `docs/research/source-policy.md`, then verify one Question at a time.

1. List factual claims in the prompt and answer guide.
2. Research with MCP/web tools. Prefer standards, upstream documentation, or official vendor documentation; never use blogs or interview collections as factual authority.
3. Rewrite the answer so it directly answers the prompt, explains the mechanism, gives material constraints or version caveats, and notes operational failure modes.
4. Add front-matter sources with `url`, `source_type` (`standard`, `official-docs`, or `official-api`), and ISO `verified_on` date.
5. Add a `## References` section with descriptive links that support the material claims.
6. Run the repository validator and report any gap needing human expert review.

## Full-answer standard

A complete answer includes the direct answer, the reason it is true, relevant constraints, and meaningful failure modes or trade-offs.

```yaml
sources:
  - url: https://example.org/official-documentation
    source_type: official-docs
    verified_on: YYYY-MM-DD
```

```md
## References

- [Descriptive official source](https://example.org/official-documentation)
```
