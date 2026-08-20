# DevOps Interview Questions

This repository is a public, topic-organized collection of DevOps interview questions. It is designed for contributors and learners to find and maintain questions consistently.

## Goal and current epic

The standing goal is a source-verified Question database a learner can navigate by deliberate sequence, not just by search. The epic [Publish the site anywhere, not only GitHub Pages](https://github.com/shapovalovdev/devops-interview-questions/issues/164) and its release [Publish anywhere v1](https://github.com/shapovalovdev/devops-interview-questions/milestone/8) closed on 2026-08-17 with every issue verified.

The epic [Epic: immutable corpus snapshot service](https://github.com/shapovalovdev/devops-interview-questions/issues/176) and release [Snapshot service v1](https://github.com/shapovalovdev/devops-interview-questions/milestone/11) closed 2026-08-18 with every issue verified. `GET /api/v1/meta` exposes source commit, corpus digest, API version, reproducible timestamp, and CC BY attribution; every API response carries `X-Content-Snapshot`; each main push publishes or verifies a digest-addressed snapshot release artifact, independently verifiable offline.

The active epic, charted 2026-08-19, is [Epic: deploy immutable snapshot service to k3s](https://github.com/shapovalovdev/devops-interview-questions/issues/205), release **Snapshot service k3s v1**. It deploys the read-only immutable Content API to k3s using one Helm chart; a Kustomize overlay consumes that chart instead of owning duplicate Kubernetes resources. The static GitHub Pages site remains a separate publisher. The API chart must preserve image build provenance, default to no write credential, and make `/api/v1/health` and `/api/v1/meta` available through a ClusterIP Service.

## Language

**Question**:
A standalone, original or substantively paraphrased interview prompt stored as one Markdown file.
_Avoid_: Copied question, entry

**Source baseline**:
An external collection used for topic coverage and inspiration, but not reproduced verbatim.
_Avoid_: Canonical content, source of truth

**Tag**:
A concise, normalized label in a question's front matter used to classify and discover questions across themes.
_Avoid_: Keyword, label

**Theme**:
The single canonical topic folder that owns a question. A question may relate to additional themes only through tags.
_Avoid_: Category, duplicate location

**Answer guide**:
A concise set of expected points that characterizes a strong answer to a question.
_Avoid_: Full solution, official answer

**Question type**:
The interview format of a question: theory, scenario, or troubleshooting.
_Avoid_: Format, kind

**Content policy**:
The rule that repository questions must be original or substantively paraphrased, even when an external collection informs coverage.
_Avoid_: Copying, transcription

**License**:
The reuse terms for this repository's content: Creative Commons Attribution 4.0 International.
_Avoid_: Proprietary terms

**Coverage target**:
The baseline every canonical Theme must reach before it is declared complete: at least twenty-five active Questions, with at least five junior, ten middle, five senior, and five staff-level Questions. It is a floor, not a cap. A Theme that grows past the baseline through certification or roadmap coverage keeps that verified material; Questions are never deleted to satisfy an exact count. `config/content-manifest.json` is the authority, and CI enforces it.
_Avoid_: Broad-topic quota, approximate coverage, exact-count cap

**Primary source**:
An official standard, upstream project document, or vendor document used to verify a Question's factual claims.
_Avoid_: Blog, interview collection

**Further reading**:
An optional explanatory article linked for learning context but not used as factual authority.
_Avoid_: Verification source

**Staff-level Question**:
A Question about cross-system design, reliability, cost-risk trade-offs, or technical leadership rather than isolated tool knowledge.
_Avoid_: Obscure senior trivia

**Queue messaging**:
The canonical Theme for message brokers and event-streaming systems, including RabbitMQ and Kafka.
_Avoid_: Generic networking, application queue

**Service mesh**:
The canonical Theme for service-to-service traffic management, identity, and policy systems such as Istio and Linkerd.
_Avoid_: Generic Kubernetes networking

**Backend architecture**:
The canonical Theme for application-service boundaries, APIs, persistence design, and operational architecture.
_Avoid_: Generic programming

**Distributed systems**:
The canonical Theme for coordination, consistency, replication, fault tolerance, and system-wide trade-offs.
_Avoid_: Backend architecture

**Network storage**:
The canonical Theme for storage accessed over a network, including NFS, SMB, iSCSI, SAN, NAS, and object-storage operational trade-offs.
_Avoid_: Local filesystems, generic cloud

**Certification tag**:
A normalized label that maps a canonical Question to one or more CNCF or Linux Foundation certification programs without duplicating the Question.
_Avoid_: Certification-specific copy

**Lab**:
A guided hands-on exercise that prepares a learner for one specific Question, stated as a checklist of steps a learner performs on real infrastructure. A Lab is published corpus material on the same terms as a Question: English, employer-neutral, and served from `window.labs` in the site's Labs view. `config/content-manifest.json` is the authority on how many Labs a Theme carries, in `lab_policy`; a Theme opts into the floor by declaring `labs: complete`, and CI enforces it from that point in both directions.
_Avoid_: Tutorial, exercise page, walkthrough, unpublished artifact

**Content store**:
The queryable database record of every Question and Lab, holding the same fields the Markdown corpus carries.
_Avoid_: Cache, index, mirror

**Content API**:
The versioned HTTP interface that reads and modifies Questions and Labs in the Content store.
_Avoid_: Backend, service, endpoint

**API contract**:
The published OpenAPI description of the Content API, which is authored first and which every implementation and client is tested against.
_Avoid_: Swagger docs, API scheme, endpoint list

**Ingest**:
The build step that loads the Markdown corpus into the Content store.
_Avoid_: Import, seeding, sync

**Export**:
The reverse step that writes Content store records back to Markdown files so git remains the reviewable, durable record of content.
_Avoid_: Dump, backup, snapshot

**Drift**:
Divergence between the Content store and the Markdown corpus, which CI detects and refuses.
_Avoid_: Conflict, staleness, mismatch

**Write credential**:
The secret an API client must present to modify a Question or a Lab. Reads never require one.
_Avoid_: Login, user account, session
