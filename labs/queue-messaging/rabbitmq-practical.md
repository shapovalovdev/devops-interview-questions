---
title: "RabbitMQ на практике: асинхронная обработка вокруг существующего приложения"
theme: "queue-messaging"
difficulty: "middle"
question_ref: "queue-messaging/design-rabbitmq-dead-lettering.md"
tags: [rabbitmq, message-queues, async-processing, observability, reliability]
why: "Брокеры сообщений упоминаются в 4 из 8 актуальных вакансий, а в банке лежит ~30 вопросов по queue-messaging без практической опоры. RabbitMQ — самый дешёвый вход в тему: один вечер с compose-стендом даёт базовый язык (exchange, binding, ack, DLQ) и снимает страх перед вопросами. Интерлизинг в вакансиях требует RabbitMQ-кластеры, efin — Kafka-концепты: обе собеседовательные ветки начинаются с понимания, чем брокер отличается от лога."
checklist:
  - "RabbitMQ поднят через docker-compose, management UI доступен на порту 15672."
  - "Создан vhost, пользователь и permissions через rabbitmqctl или UI."
  - "Flask-эндпоинт публикует задачу в очередь и сразу отвечает 202."
  - "Consumer-воркер забирает задачи и пишет результаты в PostgreSQL."
  - "Асинхронный путь проверен end-to-end: POST → очередь → воркер → строка в PG."
  - "Direct-exchange с routing key по приоритетам описан и продемонстрирован."
  - "Consumer уронен: retry зациклился, poison-сообщение ушло в DLQ."
  - "DLQ разобрана вручную: сообщение изучено и переопубликовано или отброшено осознанно."
  - "Метрика глубины очереди видна в Grafana (management API или rabbitmq_exporter)."
  - "Даны ответы на три защитных вопроса (durability, ack, at-least-once) своими словами."
---

# Lab: RabbitMQ на практике — асинхронная обработка вокруг существующего приложения

## Контекст кандидата

Ты — прод-инженер без опыта с брокерами сообщений. Есть привычный стенд: 3 Ubuntu VM, приложение Flask + PostgreSQL. Всё синхронно: пользователь просит отчёт — Flask генерирует его в запросе, запрос висит 30 секунд. Цель лабы — вынести тяжёлую работу за пределы HTTP-запроса и по пути освоить словарь брокера: exchange, binding, routing key, ack, dead-letter.

## Environment

*   **VM:** стенд из 3 Ubuntu VM (например `vm1-control`, `vm2-db`, `vm3-app`).
*   **Приложение:** Flask + PostgreSQL (существующее, из предыдущих лаб).
*   **Брокер:** RabbitMQ 3.x в docker-compose на `vm3-app`, с management-плагином (UI на `:15672`).

## Exercise 1: Поднять RabbitMQ + management UI, vhost/user/perms

1. На `vm3-app` создай `docker-compose.yml` с сервисом `rabbitmq:3-management` и пробросом портов `5672` и `15672`.
2. Подними: `docker compose up -d`. Открой `http://<vm3-ip>:15672`, войди `guest/guest` (помни: guest работает только с localhost — либо зайди через SSH-туннель, либо заведи отдельного пользователя).
3. Создай vhost `reports`, пользователя `app` с паролем и выдай permissions на vhost:
   ```bash
   docker compose exec rabbitmq rabbitmqctl add_vhost reports
   docker compose exec rabbitmq rabbitmqctl add_user app <password>
   docker compose exec rabbitmq rabbitmqctl set_permissions -p reports app ".*" ".*" ".*"
   ```
4. В UI проверь, что vhost и пользователь видны, соединений ещё нет.

## Exercise 2: Producer — Flask-эндпоинт кладёт задачу в очередь

1. Добавь в Flask-приложение эндпоинт `POST /reports` с телом `{"period": "2026-07"}`.
2. Вместо синхронной генерации опубликуй сообщение (например, через `pika` на Python) в exchange с routing key, а клиенту верни `202 Accepted` с идентификатором задачи.
3. Сначала опубликуй в default exchange напрямую в очередь `reports.tasks` — самый короткий путь, убедись, что сообщение видно в UI (заголовок очереди, `Get messages`).
4. Замерь время ответа эндпоинта до и после: было ~30 с, стало десятки миллисекунд.

## Exercise 3: Consumer — воркер разбирает задачи и пишет результат в PG

1. Напиши отдельный процесс-воркер (`python worker.py`), который подключается к `reports.tasks`, читает задачи и генерирует тот же отчёт, что раньше делал Flask.
2. Результат записи клади в PostgreSQL (таблица `reports(id, period, status, generated_at)`), а статус обновляй: `queued → done` (или `failed`).
3. Подтверждай сообщение (`basic_ack`) только после успешной записи в PG. Обрати внимание: если уронить воркер между обработкой и ack — сообщение вернётся в очередь. Это не баг, это семантика.
4. Прогони end-to-end: `curl POST /reports` → сообщение в очереди → воркер подобрал → строка в PG со статусом `done`.

## Exercise 4: Exchange/queue/binding — routing key с приоритетами

1. Заведи direct exchange `reports.ex` и две очереди: `reports.tasks.high` и `reports.tasks.low`.
2. Сделай binding: routing key `report.high` → очередь high, `report.low` → очередь low. Опиши в одну строку, чем direct отличается от topic и fanout (по одной фразе на каждую).
3. В producer добавь приоритет в payload или в routing key и публикуй в нужный ключ.
4. В management UI на вкладке exchange отправь тестовое сообщение с ключом `report.high` и убедись, что оно попало только в high-очередь.
5. (Опционально) второй воркер на high-очередь и наблюдение, что срочные отчёты обгоняют фоновые.

## Exercise 5: Dead-letter — retry → DLQ, разбор вручную

1. Объяви `reports.tasks` с аргументами `x-dead-letter-exchange` и `x-dead-letter-routing-key`, указывающими на DLX `reports.dlx` и очередь `reports.dlq`.
2. В воркере при ошибке обработки делай `basic_nack` с `requeue=false` — так poison-сообщение уходит в DLQ, а не крутится циклом.
3. Урони consumer (`kill` воркера) на середине обработки — посмотри в UI, что unacked-сообщение вернулось в очередь (redelivered = true).
4. Опубликуй задачу, которая гарантированно падает (например, несуществующий период → исключение в воркере). Покажи в UI цепочку: попытка → nack → DLQ. Сверь сценарий с вопросом банка `queue-messaging/design-rabbitmq-dead-lettering.md`.
5. Разбери DLQ вручную: прочитай сообщение, посмотри заголовки `x-death` (сколько раз и почему умерло), затем либо переопубликуй исправленным, либо удали осознанно. «Молча выпилить бизнес-сообщение» — анти-паттерн из ответа банка.

## Exercise 6: Наблюдаемость — queue depth в Grafana

1. Собери метрику глубины очереди любым из двух путей:
    * management API: `curl -u app:<pass> http://localhost:15672/api/queues/reports` → поле `messages`;
    * или готовый `rabbitmq_exporter` (docker, рядом с брокером).
2. Добавь источник в существующий Prometheus/Grafana-стек, сделай дашборд-панель: глубина `reports.tasks`, `reports.dlq`, rate publish/deliver.
3. Нагрузи эндпоинт циклом из 100 запросов и останови воркер — покажи на графике рост глубины очереди, затем запуск воркера и дренаж. Сформулируй: какая глубина очереди для тебя «пора звонить» и почему.

## Exercise 7: Защита — RabbitMQ vs Kafka, три вопроса на понимание

Подготовь ответы своими словами (по одному абзацу, без пересказа документации):

1. **Durability.** Что значит durable queue + persistent message в RabbitMQ, что гарантируется и что нет? Почему этого обычно хватает для отчётов, но не хватает там, где просят реплеи за неделю?
2. **Ack.** Чем consumer ack отличается от publisher confirm? Что происходит с unacked-сообщением при падении воркера и почему это делает обработку at-least-once, а не exactly-once?
3. **At-least-once.** Раз сообщение может прийти дважды — что обязан делать consumer, чтобы это не ломало бизнес-логику? Приведи свой пример из лабы (запись в PG).

Затем сверься с вопросами банка: `queue-messaging/choose-a-queue-or-log.md` и `queue-messaging/explain-delivery-semantics.md` — ответ на «когда RabbitMQ, когда Kafka» обязан опираться на разницу «очередь vs распределённый лог».

## Критерии готовности

Брокер поднят через compose; асинхронный путь работает end-to-end (202 → очередь → PG); приоритеты на routing key продемонстрированы; DLQ показана и разобрана вручную; глубина очереди видна в Grafana; на три защитных вопроса есть внятные ответы.
