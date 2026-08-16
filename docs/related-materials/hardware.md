# Hardware related materials

Use these resources to connect server-component decisions to firmware, storage,
and performance practice. The final link is the openly published, free online
book *Operating Systems: Three Easy Pieces*; it is learning context rather than
an authority for any individual answer.

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)

## Suggested study order

Components before the diagnostics they produce, failures before the practice
tier that instruments them, and lifecycle economics only once a fleet is
trustworthy.

1. [Explain the roles of core server components](../../questions/hardware/server-component-basics.html)
    — What CPU, memory, NIC, controller, and PSU each contribute: every later
    diagnostic is one of those components talking.
2. [Interpret disk health signals without overtrusting SMART](../../questions/hardware/smart-health-basics.html)
    — SMART is the disks speaking for themselves, interpreted without
    overtrusting a single score.
3. [Triage a degrading production disk](../../questions/hardware/disk-failure-triage.html)
    — A degrading production disk is the first triage the health signals above
    must support.
4. [Respond to a suspected storage-controller failure](../../questions/hardware/storage-controller-failure-response.html)
    — The suspected controller failure is the disk trio's confounder, so it
    comes last among them.
5. [Respond to corrected and uncorrected memory errors](../../questions/hardware/ecc-memory-errors.html)
    — Corrected and uncorrected memory errors complete the set of components
    that actually fail.
6. [Explain RAID redundancy and its limits](../../questions/hardware/raid-redundancy-basics.html)
    — RAID follows the disks directly because it exists to survive their
    failure.
7. [Operate safely during a RAID rebuild](../../questions/hardware/raid-rebuild-safety.html)
    — The rebuild question follows RAID because a rebuild is when a degraded
    array is most dangerous.
8. [Govern rack power and cooling capacity](../../questions/hardware/rack-power-cooling-governance.html)
    — Power and cooling are taken as one unit with the compute they serve
    because they fail together.
9. [Diagnose thermal throttling on a server](../../questions/hardware/thermal-throttling-diagnosis.html)
    — Thermal throttling is the power-and-cooling unit's performance symptom.
10. [Isolate a server network-interface fault](../../questions/hardware/network-interface-fault-isolation.html)
    — NIC fault isolation moves from chassis failures out to the network edge.
11. [Place a latency-sensitive workload on a NUMA server](../../questions/hardware/numa-aware-workload-placement.html)
    — NUMA placement is the topology question the component question quietly
    opened.
12. [Design a representative hardware performance benchmark](../../questions/hardware/hardware-performance-benchmark.html)
    — The practice tier opens with benchmarks that represent the workloads,
    after the failures they instrument.
13. [Build a hardware capacity baseline](../../questions/hardware/hardware-capacity-baseline.html)
    — The capacity baseline is what a benchmark becomes when it is kept
    honestly.
14. [Plan a production server firmware upgrade](../../questions/hardware/firmware-upgrade-runbook.html)
    — Firmware upgrades are the practice tier's riskiest routine.
15. [Govern firmware risk across a server fleet](../../questions/hardware/fleet-firmware-governance.html)
    — Fleet firmware governance prices that upgrade risk across every host at
    once.
16. [Use secure boot and platform attestation appropriately](../../questions/hardware/secure-boot-attestation.html)
    — Secure boot and attestation turn the boot chain into a measured supply
    chain.
17. [Validate redundant server power paths](../../questions/hardware/redundant-power-validation.html)
    — Redundant power paths are proven rather than assumed, which is why
    validation follows the design.
18. [Maintain a trustworthy server hardware inventory](../../questions/hardware/asset-inventory-basics.html)
    — Lifecycle economics open with an inventory worth trusting.
19. [Plan a hardware refresh without service interruption](../../questions/hardware/hardware-refresh-migration.html)
    — Refresh planning spends the inventory and the failure models together.
20. [Design spares and failure-domain strategy for physical infrastructure](../../questions/hardware/spares-and-failure-domain-strategy.html)
    — Spares and failure domains decide what any single failure is allowed to
    cost.
21. [Define a standard hardware platform without blocking product teams](../../questions/hardware/platform-standardization.html)
    — The standard hardware platform is the lifecycle answer to heterogeneous
    fleets.
22. [Recover access to an unreachable server without physical presence](../../questions/hardware/out-of-band-server-recovery.html)
    — Recovering an unreachable server without physical presence is the
    operational extreme the inventory enables.
23. [Plan graceful shutdown for loss of utility power](../../questions/hardware/ups-graceful-shutdown.html)
    — Graceful shutdown on lost utility power is the other operational extreme,
    and the Theme's close.
