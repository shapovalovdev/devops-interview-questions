---
title: Triage a suspected security incident
theme: security
difficulty: middle
type: troubleshooting
tags: [security, incident-response, logging, reliability]
sources:
  - url: https://csrc.nist.gov/pubs/sp/800/61/r2/final
    source_type: standard
    verified_on: 2026-08-06
---

# Triage a suspected security incident

What is the first operational response when monitoring suggests an account or workload was compromised?

## Answer guide

- Declare and scope the investigation, preserve relevant volatile and durable evidence, and establish an incident lead and communication channel.
- Contain the credible threat proportionately: revoke sessions or credentials, isolate affected workloads, block malicious paths, and preserve forensic copies before destructive cleanup where feasible.
- Eradicate the root cause, restore from known-good state, validate monitoring, and document decisions, timeline, and follow-up controls.
- Fast containment can damage availability or destroy evidence; slow containment expands attacker dwell time. Do not make uncoordinated production changes or announce unverified conclusions as facts.

## References

- Further reading (blog): [Complementary security practice article](https://snyk.io/blog/container-security-best-practices/)
- [NIST SP 800-61 Rev. 2: Computer Security Incident Handling Guide](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
- [CISA: Incident Response](https://www.cisa.gov/topics/cyber-threats-and-advisories/incident-response)
