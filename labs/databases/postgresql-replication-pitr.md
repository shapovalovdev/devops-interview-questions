---
title: "PostgreSQL: streaming-репликация, failover вручную и PITR"
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

Стенд: 3 Ubuntu VM (например `vm1-primary`, `vm2-replica`, `vm3-app`). На `vm3-app` крутится Flask-приложение с PostgreSQL-бэкендом. Деплой предпочтителен через Ansible — это прод-навык и он делает стенд воспроизводимым.

## Exercise 0: Deploy baseline (Ansible)

Разверни PostgreSQL 16 на двух VM роли `primary` и `replica`, приложение — на `vm3-app`.

1. Напиши минимальный playbook `pg.yml` с двумя host groups (`pg_primary`, `pg_replica`):
   ```bash
   ansible-playbook -i inventory pg.yml
   ```
2. Роли: `apt install postgresql`, `systemd enable --now postgresql`, создание пользователя `app` и БД `appdb` — только на primary.
3. Проверь: `pg_isready -h vm1-primary -p 5432`.

Полезно: https://www.postgresql.org/docs/current/warm-standby.html

## Exercise 1: Primary + 1 streaming replica

1. На primary создай пользователя репликации:
   ```sql
   CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD '...';
   ```
2. В `postgresql.conf` primary:
   ```ini
   listen_addresses = '*'
   max_wal_senders = 10
   wal_level = replica
   ```
   В `pg_hba.conf` разреши подключение replicator с адреса реплики.
3. Инициализируй реплику через base backup:
   ```bash
   pg_basebackup -h vm1-primary -U replicator -D /var/lib/postgresql/16/main \
     -Fp -Xs -P -R --slot=replica1
   ```
   Флаг `-R` сам запишет `primary_conninfo` и `standby.signal`.
4. Стартуй реплику и проверь режим:
   ```sql
   SELECT pg_is_in_recovery();
   ```

## Exercise 2: Проверка репликации и читающая реплика для приложения

1. На primary:
   ```sql
   CREATE TABLE t (id int);
   INSERT INTO t VALUES (42);
   ```
   На реплике (она read-only):
   ```sql
   TABLE t;            -- строка приехала
   INSERT INTO t VALUES (1);  -- ERROR: read-only
   ```
2. Лаг и состояние слота — на primary:
   ```sql
   SELECT client_addr, state, sync_state,
          write_lag, flush_lag, replay_lag
   FROM pg_stat_replication;
   ```
   Объясни себе разницу между write/flush/replay lag.
3. В Flask-приложении раздели DSN: пишет → primary, читает → replica (например, через два пула или `dbname=... options='-c default_transaction_read_only=on'`).
4. Убедись, что страница со списком данных работает, пока приложение ходит на реплику.

Диагностика лага: https://www.postgresql.org/docs/current/monitoring-stats.html

## Exercise 3: Ручной failover

1. Сымитируй аварию: `systemctl stop postgresql@16-main` на primary (или погаси VM).
2. Промоти реплику:
   ```bash
   su - postgres -c "/usr/lib/postgresql/16/bin/pg_ctl promote \
     -D /var/lib/postgresql/16/main"
   ```
   Проверь: `SELECT pg_is_in_recovery();` → `f`.
3. Переведи приложение на новую primary (поменяй DSN / роль в inventory, перезапусти).
4. **Что ломается:** старый primary после включения — это «split-brain-кандидат»: у него свой timeline, и запись туда = потеряные/расходящиеся данные. Никогда не пиши на два мастера.
5. Верни старый primary в кластер как реплику:
   ```bash
   # на старом primary: остановлен, затем
   pg_rewind --target-pgdata=/var/lib/postgresql/16/main \
     --source-server="host=vm2-replica user=replicator password=..."
   ```
   Создай `standby.signal`, поправь `primary_conninfo`, стартуй. Проверь, что он догоняет новый мастер по `pg_stat_replication` на vm2.

Что делает pg_rewind: https://www.postgresql.org/docs/current/app-pgrewind.html

## Exercise 4: PITR — archived WAL + восстановление «до момента»

1. На primary (уже новом):
   ```ini
   archive_mode = on
   archive_command = 'test ! -f /var/lib/postgresql/archive/%f && cp %p /var/lib/postgresql/archive/%f'
   wal_level = replica
   ```
   Архив положи на отдельную директорию/диск (в проде — отдельный хост или S3).
2. Проверь, что WAL архивируется: `SELECT * FROM pg_stat_archiver;`.
3. Сними физический base backup (это точка старта для PITR):
   ```bash
   pg_basebackup -h vm2-replica -U replicator -D /var/lib/postgresql/backup -Fp -Xs -P
   ```
4. **Эксперимент «удалил таблицу»**: запиши текущее время
   ```sql
   SELECT now();
   DROP TABLE important_data;
   ```
5. Восстановись на резервной копии: скопируй backup в новый `PGDATA`, в `postgresql.conf`:
   ```ini
   restore_command = 'cp /var/lib/postgresql/archive/%f %p'
   recovery_target_time = '<время из п.4>'
   ```
   + `touch recovery.signal`, стартуй. Проверь, что таблица снова на месте.
6. После проверки — `SELECT pg_wal_replay_resume();` и пойми, почему промот/пауза на recovery target важны.

Теория: https://www.postgresql.org/docs/current/continuous-archiving.html

## Exercise 5: Стратегия бэкапов: pg_dump vs physical basebackup

Составь таблицу «когда что» для своего стенда и запиши вывод в README стенда:

- `pg_dump` / `pg_dumpall` — логический: перенос на другую мажорную версию, частичный дамп (одна БД/таблица), малый размер. Но: нет PITR, медленный restore больших БД.
- Physical basebackup + WAL archive — основа PITR и реплик: моментальные снимки всего кластера, непрерывное восстановление. Но: та же мажорная версия, размер всего кластера.
- Правило: логические дампы — для миграций и «скорой помощи», физические + WAL — для RPO/RTO.

Сравнение: https://www.postgresql.org/docs/current/backup-dump.html

## Exercise 6: Patroni-мост (НЕ ставим — понимаем)

Patroni мы в этой лабе не устанавливаем. Составь список из Exercise 1–4: что именно ты делал руками, и что из этого автоматизирует Patroni + etcd:

- выбор нового лидера при аварии (твой Exercise 3 — promote руками);
- перезапуск старого мастера как реплики (pg_rewind — Patroni делает сам);
- единый endpoint (DNS/HAProxy), чтобы приложение не переконфигурировать;
- контроль lag и restarter-скрипты.

Затем ответь письменно на 3 вопроса:

1. Синхронная vs асинхронная репликация: что меняется для latency записи и для durability при аварии мастера?
2. При асинхронной репликации и failover — какие именно транзакции теряются и от чего зависит объём потери?
3. RPO и RTO простыми словами — каковы они в твоём стенде с Exercise 4 и без него?

Что автоматизирует Patroni: https://patroni.readthedocs.io/

## Что должно получиться

- Воспроизводимый Ansible-деплой primary + replica + app.
- Promotion и rejoin по шагам, записанные в конспект.
- Архив WAL, base backup и успешный PITR «до удаления таблицы».
- Таблица pg_dump vs basebackup и три письменных ответа на вопросы.
