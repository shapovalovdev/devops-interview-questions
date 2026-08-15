# Shell Scripting: related materials

Use the shell standard and Bash manual for semantics; practise scripts with linting and disposable test fixtures.

## What to learn next

- Official documentation: [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
- Manual or specification: [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- Maintainer or personal blog: [Julia Evans](https://jvns.ca/)
- Technical blog: [Red Hat: Welcome to Enable Sysadmin](https://www.redhat.com/en/blog/welcome)
- Hands-on guide: [ShellCheck wiki](https://www.shellcheck.net/wiki/)

## Suggested study order

Learn the contract before the tricks: run a script with an explicit
interpreter, treat exit statuses as the automation contract, and keep quoting
and variable expansion under control, because every later technique defends one
of those three. Argument boundaries, getopts, arrays for command arguments, and
safe input reading extend the boundary; pipelines that preserve the failed
command and command substitution that does not hide failures extend the
contract. Strict mode, temporary-file hygiene, termination signals and cleanup,
and preventing overlapping scheduled runs turn a snippet into a service. Then
the fleet tier: idempotent remediation, controlled concurrency in a worker,
logs that stay useful without leaking secrets, safe debugging, and testing
before production, with static defect-finding and supply-chain governance
wrapped around them. The final questions are judgement: when to replace a
script with a real program, how to measure automation reliability, what a
fleet-remediation runbook owes its reader, and what an organization-wide
standard should actually mandate.
