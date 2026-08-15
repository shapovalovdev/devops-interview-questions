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

The CI validator checks every unique URL in the manifest on every run — nothing
is sampled, skipped, or allowlisted for speed. Work is scheduled by host: the
URLs are grouped per host, the busiest queue is started first, and up to 32
queues run at once, one worker per host. A worker therefore only ever waits out
the interval owed to its own host, so a paced host cannot stall the hosts that
are ready. The run is bounded by the busiest host's queue rather than by the
total URL count. It sends `HEAD` first, then retries with `GET` when a host
rejects `HEAD` with a common method or bot-policy response (`403`, `405`,
`406`, or `501`).

Rate-limit and temporary-server responses (`403`, `418`, `429`, and `5xx`),
plus timeouts and connection resets, are retried three times with bounded
exponential backoff. When a response includes `Retry-After`, the validator
honours it (up to 30 seconds). A URL that is still rate limited or temporarily
unavailable after those attempts is reported explicitly as *liveness
indeterminate*, not as a broken resource: a host denying or timing out a GitHub
runner does not prove that the curated material has disappeared.

A URL the checking host cannot route to at all — `ENETUNREACH`, `EHOSTUNREACH`,
or `ENETDOWN` — is also *liveness indeterminate*. A runner without IPv6
connectivity reports this for a dual-stack host that is perfectly healthy over
IPv4; `gnu.org` is the recurring example. That is a fact about the checker's
network, not evidence that the resource is gone.

The checker sends at most one request per second to any single host, whatever
the concurrency across hosts, and
`tests/test_validate_learning_resources.py` proves that under many workers with
a stubbed transport rather than asserting it in a comment. A permanent HTTP
status is then re-checked up to three times with a browser `User-Agent`,
spaced two, five, and fifteen seconds apart, before the link is declared dead. Some hosts answer an unrecognised agent with `404`
rather than `403`, and only after they have seen a few requests: `csrc.nist.gov`
failed a different pair of URLs on each CI run while its other thirteen
citations passed, and every one of them served `200` to a browser agent. A
status alone cannot separate a withdrawn document from a bot-blocked one, so the
validator confirms with a differently shaped request. A genuinely removed page
answers `404` to any agent, so the gate is not weakened.

A very small number of hosts cannot be liveness-checked from CI at all:
`csrc.nist.gov` answers GitHub-hosted runners with `404` for documents that
exist, and the failing set changes from run to run. Those hosts are listed in
`docs/research/unverifiable-hosts.json` with evidence and a manual verification
date, and a permanent status from one of them is reported as *unverifiable*
rather than broken. This is the one place the gate stops protecting the
database, so `tests/test_unverifiable_hosts.py` caps the list, requires stated
evidence, and fails the build when an entry has not been re-verified inside the
review window.

Permanent failures remain hard errors. In particular, a `404` confirmed under
both agents, other permanent HTTP failures, DNS errors, and certificate-verification errors fail the
live-check gate and must be fixed or removed after review. A host that has
actually disappeared fails DNS resolution, which is why DNS failure stays a hard
error even though it arrives as an `OSError` like the unroutable cases above.
The retry policy is status-based and applies to every host; it is not a domain
allowlist.

For local certificate-store setups that do not trust public roots by default,
run the check with `SSL_CERT_FILE="$(python3 -m certifi)"` after installing
`certifi`.
