# Curated learning-resource schema

Every Question will receive a `## What to learn next` section as it is audited.
It contains exactly five distinct HTTPS links in this format:

```md
## What to learn next

- Official documentation: [Descriptive title](https://example.com/official)
- Manual or specification: [Descriptive title](https://example.com/specification)
- Maintainer or personal blog: [Author — descriptive title](https://example.com/personal)
- Technical blog: [Publisher — descriptive title](https://example.com/blog)
- Hands-on guide: [Descriptive title](https://example.com/guide)
```

The section is learning context, not evidence for factual claims. Authoritative
sources remain in front matter and `## References`, as required by
`question-verifier`.

`docs/research/link-audit-manifest.json` is the audited scope. The validator
checks both the Question and its Theme's related-materials page for this schema.
It then follows every unique URL when run with `--check-live`.

## Curation rules

- Read each resource before adding it; never generate a link list from search
  snippets or reuse one merely because its URL looks plausible.
- The personal or maintainer link must identify an individual author or a
  project maintainer. It cannot be an anonymous content-farm article.
- Use the resource's stable canonical URL, avoid tracking query parameters, and
  use a descriptive link title.
- A 12-month review cycle applies. Replace a redirected, inaccessible, or no
  longer relevant resource after review.

## Live-check behavior

The CI validator first sends `HEAD`, then retries with `GET` when a host rejects
`HEAD` with a common method or bot-policy response (`403`, `405`, `406`, or
`501`). A successful GET is accepted. A `403`, `429`, or other non-2xx/3xx
result after that retry remains a failed link: it is not silently treated as
valid merely because an anti-bot system may be involved. Replace it with an
equally relevant, publicly readable resource or record why human review is
required before adding it to the audited manifest.
