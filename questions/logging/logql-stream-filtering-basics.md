---
title: Select and filter log streams with LogQL
theme: logging
difficulty: junior
type: theory
tags: [logging, loki, grafana, debugging]
sources:
  - url: https://grafana.com/docs/loki/latest/query/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Select and filter log streams with LogQL

Given a Loki deployment where services log in JSON, how do you progressively narrow from all lines to the errors of one service, and what does each part of `{job="api"} |= "error"` actually do?

## Answer guide

- Start with a stream selector in braces that matches labels, for example `{job="api", environment="production"}`. LogQL returns whole streams, so the selector is the index lookup: the narrower the label match, the less data the query has to scan.
- Then apply line filters to the log content: `|= "error"` keeps lines containing the substring, `!= "healthcheck"` drops noise, and `|~ "timeout|refused"` matches a regular expression. Filters run after stream selection, so they cost query time but never index size.
- Parse structured lines before filtering on fields: `| json` extracts JSON attributes so you can write `| json | level="error"` or `| json | status_code >= 500`. For unstructured logs, `| pattern` and `| regexp` extract fields with a template.
- The same expression scales up to metrics: wrap it in `rate(...[5m])` or `count_over_time(...[1h])` to graph error rates, which is what turns ad-hoc grepping into a dashboard panel and an alerting rule.

## References

- [Loki querying: LogQL](https://grafana.com/docs/loki/latest/query/)
- Further reading (blog): [Grafana: how labels in Loki can make log queries faster and easier](https://grafana.com/blog/how-labels-in-loki-can-make-log-queries-faster-and-easier/)

## What to learn next

- Official documentation: [Loki query API and LogQL](https://grafana.com/docs/loki/latest/query/)
- Manual or specification: [Loki labels and stream identity](https://grafana.com/docs/loki/latest/get-started/labels/)
- Maintainer or personal blog: [Grafana Labs blog](https://grafana.com/blog/)
- Technical blog: [How labels in Loki can make log queries faster and easier](https://grafana.com/blog/how-labels-in-loki-can-make-log-queries-faster-and-easier/)
- Hands-on guide: [Send data to Loki and query it back](https://grafana.com/docs/loki/latest/send-data/)
