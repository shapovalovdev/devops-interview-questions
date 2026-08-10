# DevOps Interview Questions

A public, Markdown-first database of DevOps interview questions and concise answer guides. Questions are grouped in one canonical theme folder and connected to related topics with tags.

## Start here

- Browse a topic in [`questions/`](./questions/).
- Use [`TAGS.md`](./TAGS.md) to understand the controlled tag vocabulary.
- Read [`CONTRIBUTING.md`](./CONTRIBUTING.md) before adding a question.
- Follow the certification study maps in [`docs/certifications/`](./docs/certifications/), beginning with [CKA coverage](./docs/certifications/cka.md).
- Practise with the public [interview drill deck](https://shapovalovdev.github.io/devops-interview-questions/session.html): select Themes and allocations, then share the generated URL to restore the same one-question-at-a-time session. The deck links to canonical Question pages for answer guides; it never duplicates answers in browser data.

## Repository tree

```text
devops_questions/
├── questions/
│   ├── advanced-containers/       # runtime isolation, image construction, container hardening
│   ├── ci-cd/                     # pipeline design and delivery safety
│   ├── cloud/                     # cloud reliability and identity
│   ├── configuration-management/  # desired-state host configuration
│   ├── container-networking/      # Docker and Kubernetes traffic paths
│   ├── containers/                # container fundamentals
│   ├── databases/                 # data reliability and performance
│   ├── hardware/                  # physical hosts and remote management
│   ├── infrastructure-as-code/    # declarative infrastructure and state
│   ├── kubernetes/                # workload orchestration
│   ├── linux/                     # operating-system fundamentals
│   ├── logging/                   # structured event records and correlation
│   ├── networking/                # DNS, TCP, and HTTP
│   ├── observability/             # metrics, logs, traces, and alerts
│   ├── queue-messaging/           # Kafka, RabbitMQ, and event delivery
│   ├── shell-scripting/           # safe command-line automation
│   ├── security/                  # secrets and supply-chain security
│   ├── storage/                   # filesystems and persistent data
│   ├── version-control/           # safe source-history workflows
│   └── web-servers/               # reverse proxies and request handling
├── CONTRIBUTING.md
├── CONTEXT.md
├── LICENSE.md
├── README.md
├── ROADMAP_COVERAGE.md
└── TAGS.md
```

## Content policy and attribution

All questions in this repository are original or substantively paraphrased. The initial coverage was informed by the public [Swfuse DevOps interview collection](https://github.com/Swfuse/devops-interview/blob/main/interview.md), which is credited as a source baseline; its text is not reproduced here. Topic coverage is also mapped broadly to the [roadmap.sh DevOps roadmap](https://roadmap.sh/devops).

Content is made available under [CC BY 4.0](./LICENSE.md).

## Question format

Every question file has YAML front matter with a title, canonical theme, difficulty, type, and normalized tags. The body contains the prompt, an answer guide, and optional follow-ups.

[`ROADMAP_COVERAGE.md`](./ROADMAP_COVERAGE.md) maps every supported DevOps-roadmap competency to its canonical Theme.
