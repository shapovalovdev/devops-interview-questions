---
title: "PostgreSQL: streaming replication, manual failover and PITR"
theme: "databases"
difficulty: "middle"
question_ref: "databases/high-availability-failover.md"
tags: [databases, postgresql, availability, storage, reliability, ansible]
why: "Backups, replication and point-in-time recovery are standing requirements for database operations roles, and Patroni diagnostics come up wherever PostgreSQL high availability is run: doing failover and recovery by hand builds the exact mental model Patroni automates, without installing it yet."
checklist:
  - "Deploy PostgreSQL primary and one streaming replica across two VMs, initialized with pg_basebackup (Ansible playbook preferred)."
  - "Create a table on the primary and confirm the row reaches the replica."
  - "Inspect pg_stat_replication on the primary and explain the lag columns."
  - "Point the Flask app's SELECT path at the replica and confirm reads are served."
  - "Stop the primary, promote the replica with pg_ctl promote, and reconnect the application."
  - "Rejoin the old primary using pg_rewind and verify it follows the new primary."
  - "Enable archive_mode plus archive_command and confirm WAL files land in the archive."
  - "Drop a table on purpose, then perform PITR with recovery_target_time to a moment before the drop."
  - "Write down when to use pg_dump versus a physical basebackup for this stand."
  - "Map each manual step to what Patroni automates and answer the three questions on sync vs async replication, async failover loss, and RPO/RTO."
---

# Lab: PostgreSQL — streaming replication, manual failover and PITR

The stand: 3 Ubuntu VMs (`vm1-primary`, `vm2-replica`, `vm3-app`, say). A Flask application with a PostgreSQL backend runs on `vm3-app`. Deploying through Ansible is preferred — it is a production skill, and it makes the stand reproducible.

## Exercise 0: Deploy baseline (Ansible)

Deploy PostgreSQL 16 onto two VMs in the roles `primary` and `replica`, and the application onto `vm3-app`.

1. Write a minimal playbook `pg.yml` with two host groups (`pg_primary`, `pg_replica`):
   ```bash
   ansible-playbook -i inventory pg.yml
   ```
2. The roles: `apt install postgresql`, `systemd enable --now postgresql`, and creating the user `app` and the database `appdb` — on the primary only.
3. Check: `pg_isready -h vm1-primary -p 5432`.

Useful: https://www.postgresql.org/docs/current/warm-standby.html

## Exercise 1: Primary + 1 streaming replica

1. On the primary, create the replication user:
   ```sql
   CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD '...';
   ```
2. In the primary's `postgresql.conf`:
   ```ini
   listen_addresses = '*'
   max_wal_senders = 10
   wal_level = replica
   ```
   In `pg_hba.conf`, allow replicator to connect from the replica's address.
3. Initialise the replica from a base backup:
   ```bash
   pg_basebackup -h vm1-primary -U replicator -D /var/lib/postgresql/16/main \
     -Fp -Xs -P -R --slot=replica1
   ```
   The `-R` flag writes `primary_conninfo` and `standby.signal` for you.
4. Start the replica and check the mode:
   ```sql
   SELECT pg_is_in_recovery();
   ```

## Exercise 2: Verify replication, and give the application a read replica

1. On the primary:
   ```sql
   CREATE TABLE t (id int);
   INSERT INTO t VALUES (42);
   ```
   On the replica (which is read-only):
   ```sql
   TABLE t;            -- the row arrived
   INSERT INTO t VALUES (1);  -- ERROR: read-only
   ```
2. Lag and slot state, on the primary:
   ```sql
   SELECT client_addr, state, sync_state,
          write_lag, flush_lag, replay_lag
   FROM pg_stat_replication;
   ```
   Explain to yourself the difference between write, flush and replay lag.
3. Split the DSN in the Flask application: writes go to the primary, reads to the replica (through two pools, say, or `dbname=... options='-c default_transaction_read_only=on'`).
4. Confirm the page listing the data still works while the application reads from the replica.

Diagnosing lag: https://www.postgresql.org/docs/current/monitoring-stats.html

## Exercise 3: Manual failover

1. Simulate the failure: `systemctl stop postgresql@16-main` on the primary (or power the VM off).
2. Promote the replica:
   ```bash
   su - postgres -c "/usr/lib/postgresql/16/bin/pg_ctl promote \
     -D /var/lib/postgresql/16/main"
   ```
   Check: `SELECT pg_is_in_recovery();` -> `f`.
3. Point the application at the new primary (change the DSN / the role in the inventory, then restart).
4. **What breaks:** the old primary, once it comes back up, is a split-brain candidate: it has its own timeline, and writing to it means lost or diverging data. Never write to two masters.
5. Bring the old primary back into the cluster as a replica:
   ```bash
   # on the old primary: stopped, then
   pg_rewind --target-pgdata=/var/lib/postgresql/16/main \
     --source-server="host=vm2-replica user=replicator password=..."
   ```
   Create `standby.signal`, fix up `primary_conninfo`, and start it. Confirm it catches the new master up through `pg_stat_replication` on vm2.

What pg_rewind does: https://www.postgresql.org/docs/current/app-pgrewind.html

## Exercise 4: PITR — archived WAL and recovery to a point in time

1. On the primary (the new one):
   ```ini
   archive_mode = on
   archive_command = 'test ! -f /var/lib/postgresql/archive/%f && cp %p /var/lib/postgresql/archive/%f'
   wal_level = replica
   ```
   Put the archive on a separate directory or disk (in production, a separate host or S3).
2. Confirm WAL is being archived: `SELECT * FROM pg_stat_archiver;`.
3. Take a physical base backup (this is the starting point for PITR):
   ```bash
   pg_basebackup -h vm2-replica -U replicator -D /var/lib/postgresql/backup -Fp -Xs -P
   ```
4. **The "I dropped a table" experiment**: note the current time
   ```sql
   SELECT now();
   DROP TABLE important_data;
   ```
5. Recover from the backup: copy it into a new `PGDATA`, and in `postgresql.conf`:
   ```ini
   restore_command = 'cp /var/lib/postgresql/archive/%f %p'
   recovery_target_time = '<the time from step 4>'
   ```
   Then `touch recovery.signal` and start it. Confirm the table is back.
6. Once verified, run `SELECT pg_wal_replay_resume();` and work out why the promote/pause at the recovery target matters.

Theory: https://www.postgresql.org/docs/current/continuous-archiving.html

## Exercise 5: Backup strategy: pg_dump against a physical basebackup

Build a "when to use which" table for your stand and write the conclusion into the stand's README:

- `pg_dump` / `pg_dumpall` — logical: moving to a different major version, a partial dump (one database or table), small size. But: no PITR, and a slow restore for large databases.
- A physical basebackup + WAL archive — the basis of PITR and of replicas: point-in-time snapshots of the whole cluster and continuous recovery. But: the same major version, and the size of the whole cluster.
- The rule: logical dumps for migrations and first aid, physical plus WAL for RPO/RTO.

A comparison: https://www.postgresql.org/docs/current/backup-dump.html

## Exercise 6: The bridge to Patroni (we do not install it — we understand it)

We do not install Patroni in this lab. From Exercises 1-4, list what exactly you did by hand and which of it Patroni plus etcd automates:

- electing a new leader on failure (your Exercise 3 — promoting by hand);
- restarting the old master as a replica (pg_rewind — Patroni does it itself);
- a single endpoint (DNS/HAProxy), so the application never has to be reconfigured;
- lag monitoring and restarter scripts.

Then answer three questions in writing:

1. Synchronous against asynchronous replication: what changes for write latency, and for durability when the master fails?
2. With asynchronous replication and a failover — which transactions exactly are lost, and what determines how much is lost?
3. RPO and RTO in plain words — what are they for your stand with Exercise 4, and without it?

What Patroni automates: https://patroni.readthedocs.io/

## What you should end up with

- A reproducible Ansible deploy of primary + replica + app.
- The promotion and the rejoin, step by step, written up in your notes.
- A WAL archive, a base backup, and a successful PITR to just before the table was dropped.
- The pg_dump against basebackup table, and three written answers to the questions.
