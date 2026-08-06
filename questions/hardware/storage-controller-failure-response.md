---
title: Respond to a suspected storage-controller failure
theme: hardware
difficulty: senior
type: troubleshooting
tags: [hardware, raid, storage, troubleshooting, incident-response, reliability]
sources:
  - url: https://docs.kernel.org/admin-guide/md.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Respond to a suspected storage-controller failure

Multiple disks disappear from a server at once. How do you respond without making a recoverable controller problem worse?

## Answer guide

- Declare and contain the incident: stop writes or fail over when possible, record controller, enclosure, and kernel events, and confirm backup/recovery status before invasive changes.
- Treat simultaneous member loss as a shared-path clue—controller, cable, expander, power, or firmware—not automatically independent drive failure. Escalate using the vendor’s recovery procedure.
- Do not initialize arrays, clear metadata, or rebuild onto an uncertain topology. Those actions can overwrite the evidence needed to assemble the original data set.

## References

- [Linux kernel: Multiple Devices (MD)](https://docs.kernel.org/admin-guide/md.html)
- Further reading (blog): [Backblaze: managing for hard-drive failure and data corruption](https://www.backblaze.com/blog/?p=91405)

## What to learn next

- Official documentation: [Intel Software Developer's Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- Manual or specification: [NVM Express specifications](https://nvmexpress.org/specifications/)
- Maintainer or personal blog: [Brendan Gregg — systems performance](https://www.brendangregg.com/)
- Technical blog: [ServeTheHome](https://www.servethehome.com/)
- Hands-on guide: [Operating Systems: Three Easy Pieces — free online book](https://pages.cs.wisc.edu/~remzi/OSTEP/)
