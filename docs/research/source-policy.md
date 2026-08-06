# Authoritative source policy for Question verification

## Purpose

Use this policy when reviewing or adding a Question. The answer guide is a
learning aid, so its important technical claims must be accurate, sufficiently
complete for the Question, and traceable to sources that own the relevant
technology or standard.

## Acceptance rule

An active Question is source-verified only when:

1. Its answer guide directly answers every part of the prompt and contains the
   operational qualifications needed to avoid a misleading answer.
2. Each material factual claim is supported by one or more primary sources.
3. It has structured source metadata (source URL, `source_type`, and
   `verified_on` ISO date) plus a `## References` section with at least one
   descriptive Markdown link to the supporting external documentation. A source
   must support the claim it is attached to; a generic product home page does
   not qualify.
4. The reviewer marks uncertain, version-specific, or vendor-dependent
   statements as such.

Use the current stable documentation unless the Question intentionally teaches
an older version; in that case, name the version in the prompt or answer.

## Source hierarchy

Prefer sources in this order:

1. Official specification, standards body, or upstream project documentation.
2. Official product/vendor documentation and maintained source repositories.
3. A first-party security advisory, release note, or API reference.

Do not use blogs, tutorials, search-result snippets, AI output, or interview
collections as factual authority. They can suggest a Question but cannot verify
its answer. Use more than one source where an answer crosses boundaries (for
example, Kubernetes behavior plus a CNI implementation).

CI can reliably reject missing metadata, malformed dates, non-HTTPS URLs,
unapproved source types, and broken links. It cannot prove that a source entails
an answer or that an answer is complete; retain the human review checklist for
those judgement calls.

## Recommended primary sources

| Area | Preferred sources | Verification notes |
| --- | --- | --- |
| Kubernetes | [Kubernetes documentation](https://kubernetes.io/docs/home/), [Kubernetes API reference](https://kubernetes.io/docs/reference/kubernetes-api/) | Check the target Kubernetes version and feature state. NetworkPolicy also requires documentation for the installed CNI, because Kubernetes does not itself implement enforcement. |
| Containers and container networking | [Docker Docs](https://docs.docker.com/), [OCI specifications](https://opencontainers.org/), [containerd documentation](https://github.com/containerd/containerd/tree/main/docs) | Distinguish Docker CLI behavior, OCI image/runtime requirements, and runtime-specific behavior. |
| Terraform and infrastructure as code | [Terraform language documentation](https://developer.hashicorp.com/terraform/language), [Terraform provider documentation](https://registry.terraform.io/browse/providers) | Verify state and language semantics with HashiCorp; verify resource behavior with the provider's own docs. |
| Linux, boot, processes, filesystems, and networking | [Linux kernel documentation](https://www.kernel.org/doc/html/latest/), [systemd manual pages](https://www.freedesktop.org/software/systemd/man/latest/), [man7.org Linux man-pages](https://man7.org/linux/man-pages/) | State distribution-specific behavior and version where it matters. Use the upstream project manual before a distribution guide. |
| TCP/IP, DNS, TLS, HTTP | [IETF RFC index](https://www.rfc-editor.org/rfc-index.html), [IANA protocol registries](https://www.iana.org/protocols) | Cite the relevant RFC or registry for protocol semantics; product documentation alone is not sufficient. |
| CI/CD, Git, and GitHub Actions | [Git documentation](https://git-scm.com/doc), [GitHub Actions documentation](https://docs.github.com/actions) | Attribute provider-specific pipeline behavior to the provider; distinguish it from general deployment practice. |
| Cloud and managed services | The cloud provider's official documentation | Name the provider and service. Do not generalize provider behavior as a universal cloud property. |
| Security and supply chain | [NIST publications](https://csrc.nist.gov/publications), [SLSA specification](https://slsa.dev/spec/v1.0/), relevant vendor security documentation | Prefer standards/specifications for concepts and first-party product docs for implementation details. |

## Review checklist

- Does the answer explain the mechanism, not just name a command or feature?
- Does it include constraints, prerequisites, and meaningful failure cases?
- Is each answer bullet either sourced or clearly identified as a recommendation?
- Do the References directly support the answer and remain publicly accessible?
- Does the answer avoid unqualified claims that vary by version, distribution,
  CNI, cloud, or provider?

## Example reference section

```md
---
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
    source_type: official-docs
    verified_on: 2026-08-06
---

## References

- [Kubernetes: Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Cilium: Network Policy](https://docs.cilium.io/en/stable/security/policy/)
```
