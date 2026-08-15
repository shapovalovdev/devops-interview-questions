# Roadmap coverage

This map uses the DevOps roadmap as a coverage guide, not as copied content. Each competency area has a canonical Theme folder and at least one active Question.

| Roadmap competency | Theme |
| --- | --- |
| Hardware and remote management | `hardware` |
| Virtualization with QEMU, KVM, and libvirt | `qemu-kvm` |
| Linux and operating systems | `linux` |
| Linux networking | `linux-networking` |
| Linux processes | `processes` |
| Storage and filesystems | `storage` |
| Networked storage | `network-storage` |
| Shell and scripting | `shell-scripting` |
| Networking and web protocols | `networking` |
| Version control | `version-control` |
| Containers | `containers`, `advanced-containers`, `container-networking` |
| Kubernetes and orchestration | `kubernetes` |
| CI/CD | `ci-cd` |
| Infrastructure as Code | `infrastructure-as-code` |
| Configuration management | `configuration-management` |
| Cloud and identity | `cloud` |
| Databases | `databases` |
| Observability and alerting | `observability` |
| Logging | `logging` |
| Queues and event streaming | `queue-messaging` |
| Service mesh | `service-mesh` |
| Serverless and event-driven compute | `serverless` |
| Backend architecture | `backend-architecture` |
| Caching and content delivery | `caching` |
| Distributed systems | `distributed-systems` |
| Web servers and proxies | `web-servers` |
| Security and supply chain | `security` |
| Cross-domain troubleshooting | `troubleshooting` |
| Linux troubleshooting | `linux-troubleshooting` |
| Linux performance | `linux-performance` |
| Performance engineering | `performance-engineering` |
| Systems performance (Brendan Gregg concepts) | `systems-performance` |
| Site reliability engineering | `sre` |
| Testing strategy and quality | `testing-strategy` |
| Chaos engineering and resilience testing | `chaos-engineering` |
| Cloud financial management | `finops` |
| Platform engineering and internal developer platforms | `platform-engineering` |

## Coverage rule

When adding a roadmap competency, create a canonical Theme, declare it in `config/content-manifest.json`, add its Questions, register every Question in `assets/questions.js`, and update this map.

A Theme reaches the coverage floor at twenty-five active Questions with at least five junior, ten middle, five senior, and five staff-level Questions. A Theme that holds active Questions must be declared `complete` and must meet that floor: `tests/test_theme_coverage_policy.py` fails the build otherwise, so a new Theme lands as one complete drop rather than trickling onto the published site. A Theme still being scoped stays `planned` and holds no active Questions. The floor is a minimum — additional verified Questions are kept, not trimmed.
