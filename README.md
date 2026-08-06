# DevOps Interview Questions

A public, Markdown-first database of DevOps interview questions and concise answer guides. Questions are grouped in one canonical theme folder and connected to related topics with tags.

## Start here

- Browse a topic in [`questions/`](./questions/).
- Use [`TAGS.md`](./TAGS.md) to understand the controlled tag vocabulary.
- Read [`CONTRIBUTING.md`](./CONTRIBUTING.md) before adding a question.

## Repository tree

```text
devops_questions/
├── questions/
│   ├── advanced-containers/       # runtime isolation, image construction, container hardening
│   ├── ci-cd/                     # pipeline design and delivery safety
│   ├── cloud/                     # cloud reliability and identity
│   ├── container-networking/      # Docker and Kubernetes traffic paths
│   ├── containers/                # container fundamentals
│   ├── infrastructure-as-code/    # declarative infrastructure and state
│   ├── kubernetes/                # workload orchestration
│   ├── linux/                     # operating-system fundamentals
│   ├── networking/                # DNS, TCP, and HTTP
│   ├── observability/             # metrics, logs, traces, and alerts
│   └── security/                  # secrets and supply-chain security
├── CONTRIBUTING.md
├── CONTEXT.md
├── LICENSE.md
├── README.md
└── TAGS.md
```

## Content policy and attribution

All questions in this repository are original or substantively paraphrased. The initial coverage was informed by the public [Swfuse DevOps interview collection](https://github.com/Swfuse/devops-interview/blob/main/interview.md), which is credited as a source baseline; its text is not reproduced here. Topic coverage is also mapped broadly to the [roadmap.sh DevOps roadmap](https://roadmap.sh/devops).

Content is made available under [CC BY 4.0](./LICENSE.md).

## Question format

Every question file has YAML front matter with a title, canonical theme, difficulty, type, and normalized tags. The body contains the prompt, an answer guide, and optional follow-ups.
