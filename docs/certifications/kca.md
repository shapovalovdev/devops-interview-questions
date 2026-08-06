# KCA coverage map

This map aligns original practice Questions with the public [Kyverno Certified
Associate (KCA) curriculum](https://github.com/cncf/curriculum/tree/master/kca)
and the [CNCF KCA program page](https://www.cncf.io/training/certification/kca/).
Both sources were reviewed on 2026-08-06. It is a study map, **not** a
reproduction of exam questions, confidential material, or a promise of exam
coverage. Recheck the official curriculum before using this map for a future
exam preparation plan.

KCA is a multiple-choice certification focused on Kyverno policy management.
Each linked Question is original, has an answer guide, primary-source metadata,
and a separately labelled complementary technical blog. Questions remain in the
canonical `kubernetes` Theme; the `kca` certification tag makes shared material
discoverable without copying it into a certification-specific folder.

## Official domain mapping

| Official domain | Weight | Canonical original practice Questions | Mapping status |
| --- | ---: | --- | --- |
| Fundamentals of Kyverno | 18% | [Explain Kyverno policy-engine fundamentals](../../questions/kubernetes/kyverno-policy-engine-basics.md) | Original gap completed. |
| Installation, Configuration, and Upgrades | 18% | [Install or upgrade Kyverno without blocking the cluster](../../questions/kubernetes/kyverno-installation-upgrade-safety.md) | Original gap completed. |
| Kyverno CLI | 12% | [Test Kyverno policy changes with the CLI in CI](../../questions/kubernetes/kyverno-cli-policy-ci.md) | Original gap completed. |
| Applying Policies | 10% | [Roll out Kyverno enforcement using policy reports](../../questions/kubernetes/kyverno-enforcement-and-policy-reports.md) | Original gap completed. |
| Writing Policies | 32% | [Design a maintainable Kyverno policy set](../../questions/kubernetes/kyverno-policy-authoring-design.md) | Original gap completed. |
| Policy Management | 10% | [Govern the Kyverno policy lifecycle and exceptions](../../questions/kubernetes/kyverno-policy-lifecycle-governance.md) | Original gap completed. |

## Mapping decision

The existing canonical Questions cover generic Kubernetes admission guardrails
and exception governance, but none covers Kyverno's own policy types,
controllers, CLI, reports, or exception model at the scope required by the
public KCA domains. The six Questions above are therefore genuine product-level
gaps, rather than duplicated generic admission Questions. They are original
practice material derived from official documentation; they are not reconstructed
or leaked exam items.

## Central publication gate

The new files deliberately carry `kyverno` and `kca` Tags before central
integration. To publish this map truthfully, the coordinator must make one
atomic shared change:

1. Add `kyverno` to the technology vocabulary and `kca` to `TAGS.md`'s
   certification section.
2. Add `{"tag": "kca", "map": "docs/certifications/kca.md", "minimum_questions": 6}`
   to `config/content-manifest.json`.
3. Add the six rendered `.html` paths to `assets/questions.js` exactly once.
4. Run the full validator, site check, and GitHub Actions before activating or
   closing the issue.

This preserves the one-canonical-Question policy and prevents a certification
filter from claiming coverage before all six source-verified Questions are
discoverable on the public site.
