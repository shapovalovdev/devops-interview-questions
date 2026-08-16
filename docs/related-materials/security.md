# Security: related materials

Use the primary source and direct References in each Question to verify factual
claims. These five links are a stable, publicly accessible learning path for
the Security Theme; the personal blog is supplementary context, not authority.

## What to learn next

- Official documentation: [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- Manual or specification: [NIST SP 800-53 security controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- Maintainer or personal blog: [Scott Helme — practical web security](https://scotthelme.co.uk/)
- Technical blog: [Cloudflare Blog — security](https://blog.cloudflare.com/tag/security/)
- Hands-on guide: [OWASP WebGoat](https://owasp.org/www-project-webgoat/)

## Legal free books

- [Building Secure and Reliable Systems](https://google.github.io/building-secure-and-reliable-systems/)
  is published online by Google and is a legitimate free book about designing,
  operating, and improving secure production systems.
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
  is an openly published testing guide. Use its techniques only against systems
  you own or are explicitly authorized to assess.

## Suggested study order

Identity, access control, secrets, and TLS before delivery and container
controls, then detection and incident handling, then the risk governance and
recovery design that spend them.

1. [Apply least privilege to a workload identity](../../questions/security/least-privilege-iam.html)
    — Identity opens the Theme because every later control binds itself to one.
2. [Choose multi-factor authentication for privileged access](../../questions/security/multi-factor-authentication.html)
    — MFA for privileged access is the identity tier's strongest gate.
3. [Design zero-trust service access](../../questions/security/zero-trust-service-access.html)
    — Zero-trust access removes network location as an implicit grant.
4. [Describe a secure secret-management lifecycle](../../questions/security/secret-management-lifecycle.html)
    — The secret lifecycle governs the credentials the identity tier issues.
5. [Store application passwords safely](../../questions/security/password-storage.html)
    — Storing passwords safely is that lifecycle's most abused corner.
6. [Explain TLS certificate validation](../../questions/security/tls-certificate-basics.html)
    — TLS validation is the transport trust the tiers above ride on.
7. [Set web security headers deliberately](../../questions/security/security-headers.html)
    — Security headers complete the browser-facing controls of the transport
    tier.
8. [Secure shared CI runners](../../questions/security/secure-ci-runners.html) —
    Secure delivery opens with the runners, where pipeline code meets secrets.
9. [Deliver secrets to a GitOps-reconciled cluster](../../questions/security/gitops-secret-delivery.html)
    — Secret delivery to a reconciled cluster keeps GitOps honest about
    sensitive state.
10. [Verify container image provenance before deployment](../../questions/security/container-image-provenance.html)
    — Image provenance verifies what the delivery tier actually ships.
11. [Harden a container runtime workload](../../questions/security/container-runtime-hardening.html)
    — Runtime hardening bounds what the shipped workloads may do.
12. [Enforce Kubernetes Pod Security Standards](../../questions/security/kubernetes-pod-security.html)
    — Pod Security Standards enforce that hardening at the platform boundary.
13. [Design software supply-chain controls](../../questions/security/software-supply-chain-controls.html)
    — Supply-chain controls compose signing, provenance, and verification into
    one system.
14. [Design useful security event logging](../../questions/security/security-logging-basics.html)
    — Detection opens with deciding which events are worth logging.
15. [Triage a suspected security incident](../../questions/security/security-incident-triage.html)
    — Incident triage decides what the detected events actually mean.
16. [Respond to a leaked production secret](../../questions/security/secret-leak-response.html)
    — A leaked secret gets a response runbook, not just a rotation.
17. [Triage a production vulnerability report](../../questions/security/vulnerability-triage.html)
    — Vulnerability reports are triaged by exploitation reality, not CVSS
    folklore.
18. [Manage vulnerable application dependencies](../../questions/security/dependency-vulnerability-management.html)
    — Dependency management is vulnerability triage at fleet scale.
19. [Explain risk-based patch management](../../questions/security/patch-management-basics.html)
    — Risk-based patching closes detection and response with a defensible
    cadence.
20. [Design production network segmentation](../../questions/security/production-segmentation.html)
    — Resilience opens with segmentation that contains the blast radius.
21. [Design recoverable backups for ransomware](../../questions/security/ransomware-recovery-design.html)
    — Ransomware recovery assumes the adversary held the backups too.
22. [Govern security-control exceptions](../../questions/security/security-exception-governance.html)
    — Risk governance opens with exceptions that are owned, priced, and
    expiring.
23. [Define security metrics that drive engineering decisions](../../questions/security/security-metrics-program.html)
    — Metrics exist to drive engineering decisions rather than dashboard
    theatre.
24. [Establish a security platform risk model](../../questions/security/security-platform-risk-model.html)
    — The platform risk model names what the organization explicitly accepts.
25. [Deliver secure platform defaults at scale](../../questions/security/secure-platform-defaults.html)
    — Secure defaults at scale make the safe path the easy path for every team.
26. [Build organization-wide incident readiness](../../questions/security/organization-incident-readiness.html)
    — Organization-wide readiness is the Theme's close: every control rehearsed
    together.
