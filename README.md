# DevOps Interview Questions

A public, Markdown-first database of DevOps interview questions and concise answer guides. Questions are grouped in one canonical theme folder and connected to related topics with tags.

## Start here

- Browse a topic in [`questions/`](./questions/).
- Use [`TAGS.md`](./TAGS.md) to understand the controlled tag vocabulary.
- Read [`CONTRIBUTING.md`](./CONTRIBUTING.md) before adding a question.
- Follow the certification study maps in [`docs/certifications/`](./docs/certifications/), beginning with [CKA coverage](./docs/certifications/cka.md).
- Practise with the public [interview drill deck](https://shapovalovdev.github.io/devops-interview-questions/session.html): select Themes and allocations, then share the generated URL to restore the same one-question-at-a-time session. The deck links to canonical Question pages for answer guides; it never duplicates answers in browser data.
- For a short, cross-theme review, open the [must-know study collection](https://shapovalovdev.github.io/devops-interview-questions/#collection=must-know). Its controlled selection criteria are documented in [`docs/must-know.md`](./docs/must-know.md).
- To study in order rather than by topic, follow a learning path: the [SRE track](https://shapovalovdev.github.io/devops-interview-questions/#path=sre-track) runs from what reliability means to staff-level error-budget governance, with every step stating why it comes where it does. Paths are ordered data in [`config/learning-paths.json`](./config/learning-paths.json) and the schema is documented in [`docs/learning-paths.md`](./docs/learning-paths.md).
- To practise rather than read, browse the [hands-on labs view](https://shapovalovdev.github.io/devops-interview-questions/#labs): every lab is a guided exercise grouped by Theme, states why it exists, and links to the interview Question it prepares you for. Opening a Theme (`#theme=<slug>`) adds a collapsible labs strip listing only that Theme's labs. Labs are Markdown in [`labs/`](./labs/) and reach the site through `window.labs` in [`assets/questions.js`](./assets/questions.js).

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

## Self-hosting

The site is fully static and ships as a Docker image: `docker build -t devops-questions . && docker run -p 8080:8080 devops-questions`. The full publishing matrix — GitHub Pages, Docker, and any plain static web server over `build/site/` — is documented in [`docs/publishing.md`](./docs/publishing.md).

## Questions and Labs over an API

The corpus is also built into a queryable SQLite Content store and served by a versioned Content API, so a
trainer, a mobile client, or an interview bot can ask questions of the database instead of parsing Markdown:

```bash
docker compose up --build      # static site on :8080, Content API on :8000
curl "http://127.0.0.1:8000/api/v1/questions?theme=kubernetes&difficulty=senior"
```

Reads are anonymous; writes need a credential and a matching `If-Match`. Markdown in git stays the durable
record — writes are exported back to files and CI refuses any Drift between the two. The endpoints,
configuration, and workflow are documented in [`docs/content-api.md`](./docs/content-api.md).

Each `main` snapshot is also published as a GitHub Release named `snapshot-<content_digest>`. Its
`content-snapshot-<content_digest>.tar.gz` asset contains `content.db`, the exact `/api/v1/meta` payload in
`snapshot.json`, and `SHA256SUMS` for those files. The adjacent `.tar.gz.sha256` release asset checks the
archive itself; it is separate because an archive cannot contain a truthful checksum of its own final bytes.
Verify a downloaded snapshot without a running API using:

```bash
python3 scripts/build_snapshot_artifact.py --verify content-snapshot-<content_digest>.tar.gz \
  --checksum content-snapshot-<content_digest>.tar.gz.sha256
```

## k3d Content API

`deploy/content-api` is the single source of Kubernetes resources for the read-only API. The
`kustomize/k3d` overlay consumes that chart with Kustomize's Helm generator; it does not duplicate a
Deployment or Service. To build an image that names the checked-out corpus, import it into `k3d-proto`,
deploy the isolated namespace, smoke the API, and remove only that namespace:

```bash
scripts/smoke_k3d_content_api.sh
```

The script requires a k3d cluster named `proto` (context `k3d-proto`), Docker, Helm, Kustomize, and kubectl.
It passes `SOURCE_COMMIT` and `BUILD_TIMESTAMP` to `Dockerfile.api`, uses k3d's default image-import mode,
confirms the commit-tagged image is visible in the node's `k8s.io` containerd namespace, checks
`/api/v1/health`, `/api/v1/meta`, and `X-Content-Snapshot`, and always deletes `content-api-206` on exit.

## Content policy and attribution

All questions in this repository are original or substantively paraphrased. The initial coverage was informed by the public [Swfuse DevOps interview collection](https://github.com/Swfuse/devops-interview/blob/main/interview.md), which is credited as a source baseline; its text is not reproduced here. Topic coverage is also mapped broadly to the [roadmap.sh DevOps roadmap](https://roadmap.sh/devops).

Content is made available under [CC BY 4.0](./LICENSE.md).

## Question format

Every question file has YAML front matter with a title, canonical theme, difficulty, type, and normalized tags. The body contains the prompt, an answer guide, and optional follow-ups.

[`ROADMAP_COVERAGE.md`](./ROADMAP_COVERAGE.md) maps every supported DevOps-roadmap competency to its canonical Theme.
