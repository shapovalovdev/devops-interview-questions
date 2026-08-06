---
title: Explain and handle a zombie process
theme: processes
difficulty: junior
type: troubleshooting
tags: [linux, processes, debugging, pid1]
sources:
  - url: https://man7.org/linux/man-pages/man2/wait.2.html
    source_type: official-docs
    verified_on: 2026-08-06
---

# Explain and handle a zombie process

What is a zombie process, and how do you fix a growing number of them?

## Answer guide

- A zombie is a child that has terminated but still has a process-table entry so its parent can retrieve exit status with `wait`, `waitpid`, or a related call. It no longer executes application code, so sending it a signal cannot make it disappear.
- Find the zombie and its parent, confirm the state is `Z`, and inspect the parent’s child-reaping behavior. The repair is normally to fix or restart the live parent or its supervisor so it collects children; killing the zombie itself is neither possible nor useful.
- Treat many zombies as a capacity and correctness concern because process-table slots are finite. A burst may expose a parent that ignores SIGCHLD, fails to wait on error paths, or loses track of workers; capture parent logs and ownership before restart.
- In containers, ensure the namespace init or an explicit subreaper performs reaping. A shell entrypoint that fails to forward signals and collect children can create lifecycle failures even when the application logic is otherwise healthy.

## References

- [wait(2): wait for process state changes](https://man7.org/linux/man-pages/man2/wait.2.html)
- [exit(3): zombie state and reaping](https://man7.org/linux/man-pages/man3/exit.3.html)
- [pid_namespaces(7): namespace init responsibilities](https://man7.org/linux/man-pages/man7/pid_namespaces.7.html)
- Free book: [The Linux Documentation Project](https://tldp.org/)
- Further reading (blog): [Phusion: Docker and the PID 1 zombie reaping problem](https://www.phusionpassenger.com/library/indepth/docker/)

## What to learn next

- Official documentation: [man7 wait(2)](https://man7.org/linux/man-pages/man2/wait.2.html)
- Manual or specification: [Linux pid_namespaces(7)](https://man7.org/linux/man-pages/man7/pid_namespaces.7.html)
- Maintainer or personal blog: [Lennart Poettering — systemd](https://0pointer.net/blog/projects/systemd.html)
- Technical blog: [Phusion — PID 1 and child reaping](https://www.phusionpassenger.com/library/indepth/docker/)
- Hands-on guide: [Linux Journey — processes](https://linuxjourney.com/lesson/processes)
