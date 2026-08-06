---
title: Respond to a leaked production secret
theme: security
difficulty: middle
type: troubleshooting
tags: [security, incident-response, logging, least-privilege, kcsa]
sources:
  - url: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to a leaked production secret

What should the on-call team do after finding a production credential in a public repository?

## Answer guide

- Treat the value as compromised: immediately revoke or rotate it, disable dependent access if necessary, and replace consumers through the approved secret path.
- Preserve evidence and determine scope from repository, CI, secret-manager, and target-service audit logs. Remove the value from current content, but do not assume history removal makes it safe again.
- Validate the replacement and investigate whether the credential was used; notify owners according to the incident process.
- Rotation can break dependencies, so plan rollout and monitoring. Simply deleting a commit, masking a log, or reusing the same shared credential leaves an attacker with usable access.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [OWASP: Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [GitHub: Removing sensitive data from a repository](https://docs.github.com/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

## What to learn next

- Official documentation: [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- Manual or specification: [NIST SP 800-53 security controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- Maintainer or personal blog: [Scott Helme — practical web security](https://scotthelme.co.uk/)
- Technical blog: [Cloudflare Blog — security](https://blog.cloudflare.com/tag/security/)
- Hands-on guide: [OWASP WebGoat](https://owasp.org/www-project-webgoat/)
