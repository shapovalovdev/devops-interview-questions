# CBA coverage map

This map aligns original canonical practice Questions with the public
[Certified Backstage Associate (CBA) program page](https://training.linuxfoundation.org/certification/certified-backstage-associate-cba/)
published by Linux Foundation Education, the CNCF's
[CBA program page](https://www.cncf.io/training/certification/cba/), and the
CNCF's open-sourced
[CBA exam curriculum PDF](https://github.com/cncf/curriculum/blob/master/CBA_Curriculum.pdf).
All three sources were reviewed on 2026-08-12 and publish the same four domains
and the same weights, so the curriculum is public and settled rather than
provisional. This is a study map, **not** a reproduction of exam questions,
confidential material, leaked content, or a promise of exam coverage. Check the
Linux Foundation program page before using the map: it is the current public
authority for exam domains and weights.

CBA publishes four domains: Backstage Development Workflow (24%), Backstage
Infrastructure (22%), Backstage Catalog (22%), and Customizing Backstage (32%).
The CNCF curriculum PDF carries no version or revision number; the competency
bullets quoted below are taken verbatim from that PDF and from the Linux
Foundation page, which agree.

CBA is a beginner-level, online, proctored, multiple-choice certification aimed
at developers and platform engineers. It is materially more product-specific
than the other programs in this database: several of its competencies are about
the Backstage repository itself — its Yarn workspace, its TypeScript build, its
container image, its plugin system, and its React app — rather than about a
general cloud-native practice. That shaped the gap decision below.

Every linked Question is an original learning prompt. Its own Markdown file, not
this certification map, provides its answer guide, primary-source metadata, and
complementary technical blog reading. Questions remain in their canonical Theme
folder so the database does not duplicate material into a CBA-only folder.

## Official domain mapping

| Official public domain and published competencies | Weight | Canonical original practice Questions | Coverage decision |
| --- | ---: | --- | --- |
| Backstage Development Workflow: build and run Backstage projects locally; understand local development workflows; compile a Backstage project with TypeScript; download and install dependencies for a Backstage project with NPM/Yarn; use Docker to build a container image of a Backstage project | 24% | [Produce a reproducible Backstage backend image from its Yarn workspace](../../questions/ci-cd/backstage-app-build-and-image.md); [Make a monorepo versus multirepo decision](../../questions/version-control/monorepo-decision.md); [Cache CI dependencies without using stale outputs](../../questions/ci-cd/cache-dependencies-safely.md); [Manage vulnerable application dependencies](../../questions/security/dependency-vulnerability-management.md); [Build a small runtime image with multi-stage builds](../../questions/containers/multi-stage-runtime-image.md); [Order a Dockerfile for safe cache reuse](../../questions/containers/build-cache-ordering.md); [Control Docker build context with .dockerignore](../../questions/containers/dockerfile-build-context.md) | One original gap Question added. The workspace, TypeScript compile, lockfile-install, and image-build sequence is specific to the Backstage repository and was not represented; the shared monorepo, dependency-caching, dependency-risk, and multi-stage image Questions supply the transferable mechanisms around it. |
| Backstage Infrastructure: understand the Backstage framework; configure Backstage; deploy Backstage to production; understand Backstage client-server architecture | 22% | [Move a Backstage instance from local defaults to production configuration](../../questions/backend-architecture/backstage-production-configuration.md); [Design a stateless backend service](../../questions/backend-architecture/stateless-service-design.md); [Separate authentication from authorization](../../questions/backend-architecture/authentication-authorization-boundary.md); [Deliver application configuration with ConfigMaps](../../questions/kubernetes/configmap-delivery.md); [Secure Kubernetes Secret access and rotation](../../questions/kubernetes/secrets-access-and-rotation.md); [Explain a Kubernetes Deployment rollout and rollback](../../questions/kubernetes/deployment-rollout-and-rollback.md); [Run a production-readiness review](../../questions/sre/run-production-readiness-review.md) | One original gap Question added. The `app-config` layering, in-memory-to-PostgreSQL move, `baseUrl` and CORS coupling, and frontend/backend split are Backstage-specific facts no shared Question states; configuration delivery, secret handling, rollout mechanics, and readiness review are already covered canonically. |
| Backstage Catalog: understand how/why to use Backstage Catalog; populate Backstage Catalog; using annotations; working with manually registered entity locations; troubleshooting entity ingestion; working with automated ingestion | 22% | [Diagnose why a service never appears in the Backstage catalog](../../questions/backend-architecture/backstage-catalog-ingestion-triage.md); [Design a developer-portal catalog contract teams can trust](../../questions/backend-architecture/developer-portal-catalog-contract.md); [Establish service ownership and reliability accountability](../../questions/sre/establish-service-ownership.md); [Distinguish labels, selectors, and annotations](../../questions/kubernetes/labels-selectors-and-annotations.md); [Establish data governance architecture](../../questions/backend-architecture/data-governance-architecture.md) | One original gap Question added. The existing catalog Question covers the entity model, ownership, and portal-as-integration-surface design; it does not cover the processing loop, static locations versus entity providers, annotation contracts, orphaned entities, or how ingestion actually fails, which is what four of the six published competencies ask about. |
| Customizing Backstage: understand frontend versus backend plugins; customizing Backstage plugins; make changes to React code in Backstage App; using Material UI components | 32% | [Decide whether a Backstage capability belongs in a frontend or backend plugin](../../questions/backend-architecture/backstage-plugin-boundaries.md); [Keep Backstage UI customizations upgradable](../../questions/backend-architecture/backstage-ui-customization-upgrades.md); [Govern evolutionary backend architecture](../../questions/backend-architecture/evolutionary-architecture-governance.md); [Govern API versioning and deprecation](../../questions/backend-architecture/api-versioning-policy.md) | Two original gap Questions added. This is the heaviest domain and the database had no coverage of it at all: nothing described the frontend/backend plugin split, plugin extension points, or theming a React app through `createUnifiedTheme` rather than forking components. The two governance Questions supply the upgrade and deprecation reasoning that makes those choices survivable. |

## Gap decision

Four domains, five original gap Questions, one decision per domain:

1. **Backstage Development Workflow — gap closed by one new Question.** The
   shared container and dependency Questions teach layer ordering, build
   context, lockfile discipline, and vulnerability triage, but none of them
   states what a Backstage build actually is: a Yarn workspace whose backend is
   compiled and bundled before it is copied into an image, with native modules
   and a host-build-versus-multi-stage choice. That is a genuine gap, so
   [Produce a reproducible Backstage backend image from its Yarn workspace](../../questions/ci-cd/backstage-app-build-and-image.md)
   was written against the upstream Docker and CLI build-system documentation.
2. **Backstage Infrastructure — gap closed by one new Question.** Generic
   configuration and secret Questions do not say that Backstage reads a layered
   `app-config`, that the demo database is not a production database, or that
   the frontend is served by the backend and breaks when `baseUrl` and CORS
   disagree. [Move a Backstage instance from local defaults to production configuration](../../questions/backend-architecture/backstage-production-configuration.md)
   closes that. Nothing else in the domain needed a new prompt; deployment,
   rollout, and readiness are already covered at useful depth.
3. **Backstage Catalog — gap closed by one new Question.** The existing
   [developer-portal catalog contract](../../questions/backend-architecture/developer-portal-catalog-contract.md)
   Question covers the design side of this domain well and is deliberately not
   duplicated. What it does not cover is the operational side the curriculum
   names — ingestion, annotations, manual locations, and troubleshooting — so
   [Diagnose why a service never appears in the Backstage catalog](../../questions/backend-architecture/backstage-catalog-ingestion-triage.md)
   was added instead of restating the design Question with a new tag.
4. **Customizing Backstage — gap closed by two new Questions.** At 32% this is
   the largest domain and it had zero coverage, because no Theme in this
   database previously discussed a portal's own plugin architecture or UI code.
   [Decide whether a Backstage capability belongs in a frontend or backend plugin](../../questions/backend-architecture/backstage-plugin-boundaries.md)
   covers the first two competencies and
   [Keep Backstage UI customizations upgradable](../../questions/backend-architecture/backstage-ui-customization-upgrades.md)
   covers the React and Material UI competencies. Two Questions rather than one
   because plugin placement and UI customization fail differently and have
   different owners.

No further Question is added. The remaining competencies are already covered at
useful operational depth by the canonical Questions in the table, and adding a
CBA-only prompt for dependency installation, container layering, secret
handling, or ownership metadata would repeat an existing Question rather than
close a genuine gap. Revisit this decision if the published curriculum adds a
competency that is not represented by the linked material — in particular if
CNCF publishes a versioned CBA curriculum, since the current PDF carries no
revision number.

## Deliberate exclusions

The published competencies include exercises a written interview Question cannot
honestly assess and this database will not fake: running `yarn dev` on a laptop,
typing a specific Backstage CLI flag, or naming which Material UI component
renders a particular card. This map does not invent command-recall prompts for
those. It covers the decisions, mechanisms, and failure modes behind them and
points at the upstream documentation where the commands live.

## Focused verification plan and evidence

`tests/test_cba_curriculum_map.py` provides a narrow regression gate for this
map. It verifies the three official curriculum URLs, the review date, the
current four-domain names and weights, the explicit no-exam-material statement,
and that the gap decision is stated per domain. It also requires every mapped
canonical Markdown file to exist, to carry structured primary-source metadata,
an answer guide, references, and a labelled complementary blog, and to be linked
by this document.

The focused check was run locally with:

```sh
python3 tests/test_cba_curriculum_map.py
```

The coordinator must run the repository-wide content validator and site check,
then use GitHub Actions as the final publication gate.

## Central publication handoff

These shared changes are made together so the public site never advertises a CBA
filter it cannot honour:

1. Add `cba` under `## Certifications` in `TAGS.md`.
2. Add `{"tag": "cba", "map": "docs/certifications/cba.md", "minimum_questions": 23}` to `config/content-manifest.json`, keeping the list sorted by tag.
3. Apply the `cba` tag to exactly the 23 canonical Questions linked in the table
   above, including the five new gap Questions. Do not tag a file merely because
   it sits in `backend-architecture`, `ci-cd`, or `containers`.
4. Regenerate `assets/questions.js` with `python3 scripts/generate_question_catalog.py`
   so every tagged Markdown Question appears exactly once as a Pages-rendered
   `.html` catalog record, and add the five new Questions to
   `docs/research/link-audit-manifest.json`.
5. Run the focused map check, the full validator, `tests/site_check.py`, and
   successful GitHub Actions before closing the issue.

This preserves the one-canonical-Question policy and prevents a public
certification label from overstating study coverage.
