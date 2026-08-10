---
title: Manage database connections from serverless functions
theme: serverless
difficulty: middle
type: troubleshooting
tags: [cloud, databases, reliability, performance, postgresql]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/configuration-database.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Manage database connections from serverless functions

A relational database starts refusing connections whenever a function scales up. What is happening, and how do you fix it properly?

## Answer guide

- The direct cause is that connection count scales with concurrency, not with instance count. Each execution environment holds its own connection, so a function at a thousand concurrent invocations wants a thousand backend connections, and a relational engine that allocates a process or a large per-connection buffer runs out of memory or hits `max_connections` long before that.
- The mechanism worth stating: a traditional pool amortises expensive connection setup across many threads inside one long-lived process. Functions have no such shared process, so a per-environment "pool" of size ten multiplies the problem by ten rather than bounding it. Set per-environment pool size to one or two and bound the total at the platform layer.
- The correct controls are an external connection proxy or pooler that multiplexes many client connections onto a small backend set, plus reserved concurrency on the function so the database can never see more clients than it can serve. Data APIs or HTTP-fronted stores remove the problem entirely by making each call stateless.
- Create clients outside the handler so they are reused across invocations on the same environment, but keep TCP keepalive and driver timeouts shorter than the platform's idle-environment reclaim window, and validate a connection before use because a frozen environment can resume holding a socket the server already closed.
- Failure modes to expect: connection storms during a cold-start burst, idle connections pinned by environments that are frozen rather than terminated, transaction-mode poolers breaking prepared statements or session state, and a proxy that silently becomes the new bottleneck because its own connection limit was never sized or alerted on.

## References

- [Working with AWS Lambda and database connections](https://docs.aws.amazon.com/lambda/latest/dg/configuration-database.html)
- Further reading (blog): [AWS Database Blog — connection management articles](https://aws.amazon.com/blogs/database/)

## What to learn next

- Official documentation: [Amazon RDS Proxy connection pooling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)
- Manual or specification: [AWS Lambda API reference — PutFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionConcurrency.html)
- Maintainer or personal blog: [Jeremy Daly — serverless database connection management](https://www.jeremydaly.com/)
- Technical blog: [AWS Database Blog](https://aws.amazon.com/blogs/database/)
- Hands-on guide: [Tutorial: use a Lambda function to access an Amazon RDS database](https://docs.aws.amazon.com/lambda/latest/dg/services-rds-tutorial.html)
