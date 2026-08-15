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

Ground yourself in the component question first — what CPU, memory, NIC,
controller, and PSU each contribute — because every later diagnostic is one of
those components talking. Study the disk trio next — SMART interpreted without
overtrusting it, triage of a degrading production disk, the suspected
storage-controller failure — then corrected and uncorrected memory errors,
since drives and DIMMs are what actually fail. RAID redundancy and its limits
follow the disks directly, and the rebuild question follows RAID, because a
rebuild is when a degraded array is most dangerous. Take power, cooling, and
thermal throttling as one unit — they fail together — then the
network-interface fault and NUMA placement. The practice tier comes after the
failures it instruments: representative benchmarks, the capacity baseline,
firmware upgrades and fleet firmware risk, secure boot and attestation,
redundant power paths. Finish with lifecycle economics — a trustworthy
inventory, refresh planning, spares and failure domains, the standard hardware
platform — plus the two operational extremes: recovering an unreachable server
without physical presence and shutting down gracefully on lost utility power.
