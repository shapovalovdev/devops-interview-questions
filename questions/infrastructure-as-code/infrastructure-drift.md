---
title: Detect and handle infrastructure drift
theme: infrastructure-as-code
difficulty: middle
type: scenario
tags: [terraform, infrastructure-as-code, reliability, troubleshooting]
---

# Detect and handle infrastructure drift

How do you identify a manually changed cloud resource that no longer matches declared infrastructure, and how do you restore control safely?

## Answer guide

- Run a plan or equivalent comparison against the remote system.
- Establish whether the declaration or the live change is intended before applying changes.
- Import, update declaration, or reconcile deliberately; prevent repeated manual edits with access and workflow controls.
