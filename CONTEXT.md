# DevOps Interview Questions

This repository is a public, topic-organized collection of DevOps interview questions. It is designed for contributors and learners to find and maintain questions consistently.

## Goal and current epic

The standing goal is a source-verified Question database a learner can navigate by deliberate sequence, not just by search. The current epic is the wayfinder map [Open the qemu-kvm Theme](https://github.com/shapovalovdev/devops-interview-questions/issues/128): a canonical `qemu-kvm` Theme at the 25-Question coverage floor, with a related-materials page and study order, a hands-on lab, and its Questions woven into the `devops-platform` learning path. Its release gate is the GitHub milestone [qemu-kvm v1](https://github.com/shapovalovdev/devops-interview-questions/milestone/2). Work is only dispatched on issues attached to that milestone; when the milestone closes, a new epic and release must be charted before further implementation work starts.

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
