---
title: Convert journald and Flask logs to structured JSON
theme: logging
difficulty: junior
type: scenario
tags: [logging, observability, debugging, journald]
sources:
  - url: https://www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html
    source_type: official-docs
    verified_on: 2026-08-16
  - url: https://flask.palletsprojects.com/en/stable/logging/
    source_type: official-docs
    verified_on: 2026-08-16
---

# Convert journald and Flask logs to structured JSON

A Flask service behind gunicorn writes prose logs to the journal. Convert the pipeline so every downstream consumer receives structured JSON, and explain why that matters for the rest of the logging stack.

## Answer guide

- Structured logging means each line is a JSON object with stable field names — at minimum `timestamp`, `level`, `service`, `message`, plus request identifiers — instead of prose that every consumer must re-parse with fragile regular expressions. Machines parse JSON once; humans still read the rendered message.
- journald is already structured: every record carries well-known fields such as `_PID`, `_SYSTEMD_UNIT`, `MESSAGE`, `PRIORITY`, and `__REALTIME_TIMESTAMP`, and `journalctl -o json` emits them directly. A collector like Alloy or Promtail can read the journal natively and map those fields into the exported log payload.
- For Flask, configure the application logger instead of printing: set up Python's `logging` through `dictConfig` in the app factory, attach a JSON formatter (for example `python-json-logger`), and route gunicorn's error and access logs through the same formatter so web-server lines and application lines share one schema. `app.logger` and `current_app.logger` then inherit it.
- JSON lines are what make the rest of the stack cheap: Loki's `| json` parser turns fields into queryable attributes without regex, `level` and `status` become filters and alert rules, and correlation IDs survive into dashboards. Unstructured logs force every tool downstream to guess the format; structured logs make the schema the contract.

## References

- [systemd.journal-fields: well-known journal fields](https://www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html)
- [Flask logging documentation](https://flask.palletsprojects.com/en/stable/logging/)
- Further reading (blog): [Real Python: logging in Python](https://realpython.com/python-logging/)

## What to learn next

- Official documentation: [Flask logging](https://flask.palletsprojects.com/en/stable/logging/)
- Manual or specification: [systemd journal fields](https://www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html)
- Maintainer or personal blog: [structlog documentation and blog](https://www.structlog.org/en/stable/)
- Technical blog: [Real Python: logging in Python](https://realpython.com/python-logging/)
- Hands-on guide: [Python logging HOWTO](https://docs.python.org/3/howto/logging.html)
