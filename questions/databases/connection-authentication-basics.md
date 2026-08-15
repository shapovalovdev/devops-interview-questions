---
title: Explain PostgreSQL connection authentication
theme: databases
difficulty: junior
type: theory
tags: [databases, postgresql, security, least-privilege]
sources:
  - url: https://www.postgresql.org/docs/current/client-authentication.html
    source_type: official-docs
    verified_on: 2026-08-06
  - url: https://mariadb.com/docs/server/reference/plugins/authentication-plugins
    source_type: official-docs
    verified_on: 2026-08-16
---

# Explain PostgreSQL connection authentication

How should an application authenticate to PostgreSQL safely?

## Answer guide

- PostgreSQL checks client authentication using `pg_hba.conf`; choose a network boundary, TLS where traffic can be observed, and a strong authentication method appropriate to the identity system. Create a dedicated role for the application rather than sharing a superuser.
- Grant only the database, schema, table, and routine privileges the workload needs, store credentials in a secret system, rotate them, and audit failed logins. Test authentication changes from a separate session before reloading configuration.
- Network filtering alone is not authorization, and role membership can widen access unexpectedly. A mistaken HBA rule, disabled certificate verification, or a leaked long-lived password can expose all data, so review effective access and incident response paths.
- The host-plus-method rule repeats elsewhere: MariaDB and MySQL scope accounts as user@host with a per-account authentication plugin and TLS requirement in place of pg_hba.conf lines, and SQL Server authenticates logins against the server — network position is never authorization on any of them.

## References

- [PostgreSQL documentation: client authentication](https://www.postgresql.org/docs/current/client-authentication.html)
- Further reading (blog): [pganalyze: PostgreSQL security](https://pganalyze.com/postgresql-security)
- [MariaDB — authentication plugins](https://mariadb.com/docs/server/reference/plugins/authentication-plugins)

## What to learn next

- Official documentation: [PostgreSQL: client authentication](https://www.postgresql.org/docs/current/client-authentication.html)
- Manual or specification: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/)
- Maintainer or personal blog: [Hironobu Suzuki — The Internals of PostgreSQL](https://www.interdb.jp/pg/)
- Technical blog: [pganalyze — PostgreSQL security](https://pganalyze.com/postgresql-security)
- Hands-on guide: [PostgreSQL client authentication configuration](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html)
