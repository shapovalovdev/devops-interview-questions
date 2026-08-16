# Shell Scripting: related materials

Use the shell standard and Bash manual for semantics; practise scripts with linting and disposable test fixtures.

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)

## Suggested study order

The contract before the tricks: interpreter, exit statuses, and quoting carry
every later technique from snippet to fleet service.

1. [Execute a shell script with an explicit interpreter](../../questions/shell-scripting/execute-a-script-portably.html)
    — Running with an explicit interpreter is the contract underneath every
    later technique.
2. [Use exit statuses as an automation contract](../../questions/shell-scripting/use-exit-statuses.html)
    — Exit statuses are the automation contract everything downstream reads.
3. [Explain shell quoting and variable expansion](../../questions/shell-scripting/shell-quoting-and-expansion.html)
    — Quoting and variable expansion under control is the third thing every
    later technique defends.
4. [Prevent command injection in an automation script](../../questions/shell-scripting/avoid-command-injection.html)
    — Command injection is what uncontrolled quoting costs, met immediately
    after quoting.
5. [Handle shell-script arguments without losing boundaries](../../questions/shell-scripting/handle-script-arguments.html)
    — Argument boundaries extend the contract to the inputs a script accepts.
6. [Parse command-line options with getopts](../../questions/shell-scripting/parse-options-with-getopts.html)
    — getopts parses options without losing the boundaries established above.
7. [Use Bash arrays for command arguments](../../questions/shell-scripting/use-arrays-for-arguments.html)
    — Arrays carry command arguments as words rather than one fragile string.
8. [Read arbitrary input lines safely in Bash](../../questions/shell-scripting/read-lines-safely.html)
    — Reading arbitrary input lines safely is the boundary tier's last skill.
9. [Preserve the failed command in a pipeline](../../questions/shell-scripting/preserve-pipeline-failures.html)
    — Pipelines that preserve the failed command extend the exit-status
    contract.
10. [Use command substitution without hiding failures](../../questions/shell-scripting/use-command-substitution-deliberately.html)
    — Command substitution used deliberately does not hide the failures inside
    it.
11. [Apply Bash strict mode with context](../../questions/shell-scripting/choose-strict-mode.html)
    — Strict mode is the first step from snippet toward service.
12. [Create and clean temporary files safely](../../questions/shell-scripting/manage-temporary-files.html)
    — Temporary-file hygiene keeps the service from littering its host.
13. [Handle termination signals and cleanup](../../questions/shell-scripting/handle-signals-and-cleanup.html)
    — Termination signals and cleanup make the exit paths deliberate.
14. [Prevent overlapping scheduled script runs](../../questions/shell-scripting/lock-singleton-job.html)
    — Preventing overlapping scheduled runs completes the snippet-to-service
    tier.
15. [Make a remediation script idempotent](../../questions/shell-scripting/implement-idempotent-remediation.html)
    — The fleet tier opens with remediation that is safe to re-run.
16. [Control concurrent jobs in a Bash worker](../../questions/shell-scripting/control-concurrent-jobs.html)
    — Controlled concurrency keeps the worker from stampeding the fleet it
    serves.
17. [Make shell-script logs useful without leaking secrets](../../questions/shell-scripting/log-without-secrets.html)
    — Fleet logs stay useful without leaking the secrets they pass near.
18. [Debug a failing production script safely](../../questions/shell-scripting/debug-production-script-safely.html)
    — Debugging in production preserves evidence rather than destroying it.
19. [Test a shell script before production](../../questions/shell-scripting/test-shell-scripts.html)
    — Testing before production is the fleet tier's own gate.
20. [Find shell-script defects before deployment](../../questions/shell-scripting/debug-with-shellcheck.html)
    — Static defect-finding wraps the fleet tier from the outside.
21. [Govern the shell-script supply chain](../../questions/shell-scripting/govern-shell-script-supply-chain.html)
    — Supply-chain governance wraps the same tier from the other side.
22. [Decide when to replace a shell script](../../questions/shell-scripting/decide-when-to-replace-shell.html)
    — The judgement tier opens with knowing when shell is the wrong tool.
23. [Measure shell-automation reliability](../../questions/shell-scripting/measure-automation-reliability.html)
    — Reliability measurement makes the fleet's scripts an accountable service.
24. [Design a fleet-remediation runbook](../../questions/shell-scripting/design-fleet-remediation-runbook.html)
    — The runbook owes its reader judgement, not just a command list.
25. [Define a safe shell-automation standard](../../questions/shell-scripting/define-shell-automation-standard.html)
    — The organization-wide standard closes the Theme by deciding what to
    actually mandate.
