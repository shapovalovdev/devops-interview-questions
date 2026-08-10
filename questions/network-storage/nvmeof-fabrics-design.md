---
title: Design an NVMe over Fabrics deployment
theme: network-storage
difficulty: senior
type: scenario
tags: [storage, networking, performance, reliability, security]
sources:
  - url: https://nvmexpress.org/specification/nvm-express-over-fabrics-specification/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Design an NVMe over Fabrics deployment

What must be designed before presenting NVMe namespaces across a fabric?

## Answer guide

- NVMe over Fabrics extends NVMe access across transports such as TCP or RDMA. Design stable discovery and controller identities, namespace access controls, independent fabric paths, host multipathing, and an explicit ownership model for each namespace.
- Benchmark end-to-end latency, queue depth, CPU cost, congestion behavior, and failover using the chosen transport and driver. Monitor controller state, path errors, retransmissions or RDMA counters, namespace capacity, and application tail latency.
- Low protocol latency does not eliminate network loss, switch faults, or split-brain writers. Do not expose the same conventional filesystem to uncoordinated hosts, and do not claim an RDMA design is faster until it is measured with its production NIC, switch, and workload.

## References

- [Linux kernel: NVMe documentation](https://docs.kernel.org/nvme/index.html)
- [NVM Express over Fabrics specification](https://nvmexpress.org/specification/nvm-express-over-fabrics-specification/)
- Further reading (blog): [Red Hat Blog: storage](https://www.redhat.com/en/blog)

## What to learn next

- Official documentation: [Linux NVMe documentation](https://docs.kernel.org/nvme/index.html)
- Manual or specification: [Linux NVMe over Fabrics](https://nvmexpress.org/specification/nvm-express-over-fabrics-specification/)
- Maintainer or personal blog: [Linux NVMe maintainer mailing list](https://lists.infradead.org/mailman/listinfo/linux-nvme)
- Technical blog: [Red Hat Blog: storage](https://www.redhat.com/en/blog)
- Hands-on guide: [nvme-cli project](https://github.com/linux-nvme/nvme-cli)
