# Processes: related materials

Use the Question-level sources for factual verification. This page is a curated learning path, not a substitute for validating production behavior against the running kernel, service manager, and runtime version.

## What to learn next

- Official documentation: [Linux man-pages: proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- Manual or specification: [Linux man-pages: signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html)
- Maintainer or personal blog: [Brendan Gregg’s Linux performance writing](https://www.brendangregg.com/linuxperf.html)
- Technical blog: [Red Hat — What is a Linux process?](https://www.redhat.com/en/topics/linux/what-is-a-linux-process)
- Hands-on guide: [The Linux Documentation Project](https://tldp.org/)

## Suggested study order

Start with `/proc`, PIDs, process states, and signals. Then study fork/exec/wait and file-descriptor inheritance. Next, use systemd’s unit, cgroup, and kill semantics to reason about real service lifecycles. Finish with resource controls, observability, incident triage, and organization-wide guardrails.
