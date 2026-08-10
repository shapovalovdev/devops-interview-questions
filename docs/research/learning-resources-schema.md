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

The CI validator checks unique URLs concurrently across hosts, but spaces
requests to the same host. It sends `HEAD` first, then retries with `GET` when a
host rejects `HEAD` with a common method or bot-policy response (`403`, `405`,
`406`, or `501`).

Rate-limit and temporary-server responses (`403`, `418`, `429`, and `5xx`),
plus timeouts and connection resets, are retried three times with bounded
exponential backoff. When a response includes `Retry-After`, the validator
honours it (up to 30 seconds). A URL that is still rate limited or temporarily
unavailable after those attempts is reported explicitly as *liveness
indeterminate*, not as a broken resource: a host denying or timing out a GitHub
runner does not prove that the curated material has disappeared.

Permanent failures remain hard errors. In particular, `404` and other permanent
HTTP failures, DNS errors, and TLS errors fail the live-check gate and must be
fixed or removed after review. The retry policy is status-based and applies to
every host; it is not a domain allowlist.

For local certificate-store setups that do not trust public roots by default,
run the check with `SSL_CERT_FILE="$(python3 -m certifi)"` after installing
`certifi`.
