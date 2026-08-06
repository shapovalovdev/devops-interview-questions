# ICA coverage map

This map aligns original practice Questions to the current [Istio Certified Associate
(ICA) curriculum](https://training.linuxfoundation.org/certification/istio-certified-associate-ica/).
It is a study map, not a reproduction of exam questions or confidential exam content. The
curriculum was reviewed on 2026-08-06; consult the official page before studying because
the program can change.

| Official domain | Weight | Canonical practice Questions tagged `ica` |
| --- | ---: | --- |
| Installation, Upgrade & Configuration | 20% | Select an Istio data-plane mode; customize an Istio installation safely; upgrade Istio with a bounded canary |
| Traffic Management | 35% | Configure Istio ingress and egress boundaries; route mesh traffic with a VirtualService; apply traffic policies with a DestinationRule; shift traffic progressively with Istio; connect a mesh workload to an external service; design an Istio resilience policy; use Istio fault injection safely |
| Securing Workloads | 25% | Enforce Istio mutual TLS incrementally; combine JWT authentication and authorization in Istio; secure edge traffic at an Istio gateway |
| Troubleshooting | 20% | Triage an Istio configuration that is not taking effect; distinguish Istio control-plane and data-plane failures |

Every mapped Question has original wording, a complete answer guide, primary-source metadata,
and a separate complementary technical blog link. The canonical files live in `questions/service-mesh/`
so related service-mesh coverage can be reused by other certification maps without copies.
