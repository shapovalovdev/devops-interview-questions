---
title: "RabbitMQ in practice: asynchronous processing around an existing application"
theme: "queue-messaging"
difficulty: "middle"
question_ref: "queue-messaging/design-rabbitmq-dead-lettering.md"
tags: [rabbitmq, message-queues, event-driven, observability, reliability]
why: "Message brokers are a standing interview topic, while the queue-messaging Theme holds Questions with no practical footing. RabbitMQ is the cheapest entry into the topic: one evening with a compose stand teaches the basic vocabulary (exchange, binding, ack, DLQ) and removes the fear of those interview questions. Roles that run RabbitMQ clusters and roles that ask for Kafka concepts both start from the same place: understanding how a broker differs from a log."
checklist:
  - "RabbitMQ is up through docker-compose, with the management UI reachable on port 15672."
  - "A vhost, a user and permissions are created through rabbitmqctl or the UI."
  - "A Flask endpoint publishes a task to a queue and answers 202 immediately."
  - "A consumer worker takes tasks off the queue and writes results into PostgreSQL."
  - "The asynchronous path is proven end to end: POST -> queue -> worker -> a row in PG."
  - "A direct exchange with a routing key per priority is described and demonstrated."
  - "The consumer has been killed: the retry looped, and the poison message went to the DLQ."
  - "The DLQ has been worked by hand: the message was inspected and either republished or dropped deliberately."
  - "Queue depth is visible in Grafana (through the management API or rabbitmq_exporter)."
  - "The three defence questions (durability, ack, at-least-once) are answered in your own words."
---

# Lab: RabbitMQ in practice — asynchronous processing around an existing application

## Where you are starting from

You are a production engineer with no broker experience. You have the usual stand: 3 Ubuntu VMs running a Flask + PostgreSQL application. Everything is synchronous: a user asks for a report, Flask generates it inside the request, and the request hangs for 30 seconds. The point of the lab is to move the heavy work outside the HTTP request and, on the way, to learn the broker vocabulary: exchange, binding, routing key, ack, dead-letter.

## Environment

*   **VMs:** the 3-VM Ubuntu stand (for example `vm1-control`, `vm2-db`, `vm3-app`).
*   **Application:** Flask + PostgreSQL (the existing one, from the earlier labs).
*   **Broker:** RabbitMQ 3.x in docker-compose on `vm3-app`, with the management plugin (UI on `:15672`).

## Exercise 1: Stand up RabbitMQ + the management UI, vhost/user/perms

1. On `vm3-app`, write a `docker-compose.yml` with a `rabbitmq:3-management` service publishing ports `5672` and `15672`.
2. Bring it up: `docker compose up -d`. Open `http://<vm3-ip>:15672` and log in as `guest/guest` (remember: guest only works from localhost — either go through an SSH tunnel or create a separate user).
3. Create the vhost `reports` and the user `app` with a password, and grant permissions on the vhost:
   ```bash
   docker compose exec rabbitmq rabbitmqctl add_vhost reports
   docker compose exec rabbitmq rabbitmqctl add_user app <password>
   docker compose exec rabbitmq rabbitmqctl set_permissions -p reports app ".*" ".*" ".*"
   ```
4. In the UI, confirm the vhost and the user are visible and that there are no connections yet.

## Exercise 2: Producer — a Flask endpoint puts a task on the queue

1. Add an endpoint `POST /reports` to the Flask application, with a body of `{"period": "2026-07"}`.
2. Instead of generating synchronously, publish a message (through `pika` on Python, for example) to an exchange with a routing key, and return `202 Accepted` to the client with a task identifier.
3. Publish to the default exchange straight into the `reports.tasks` queue first — the shortest path — and confirm the message is visible in the UI (the queue header, then `Get messages`).
4. Measure the endpoint's response time before and after: it was ~30 s, it is now tens of milliseconds.

## Exercise 3: Consumer — a worker drains tasks and writes the result to PG

1. Write a separate worker process (`python worker.py`) that connects to `reports.tasks`, reads tasks, and generates the same report Flask used to.
2. Write the result into PostgreSQL (a table `reports(id, period, status, generated_at)`), updating the status: `queued → done` (or `failed`).
3. Acknowledge the message (`basic_ack`) **only** after the write to PG has succeeded. Note what follows: kill the worker between processing and the ack and the message returns to the queue. That is not a bug, that is the semantics.
4. Run it end to end: `curl POST /reports` → a message on the queue → the worker picks it up → a row in PG with status `done`.

## Exercise 4: Exchange/queue/binding — a routing key per priority

1. Declare a direct exchange `reports.ex` and two queues: `reports.tasks.high` and `reports.tasks.low`.
2. Bind them: routing key `report.high` → the high queue, `report.low` → the low queue. Describe in one line each how direct differs from topic and from fanout.
3. In the producer, add a priority to the payload or to the routing key, and publish to the right key.
4. In the management UI, on the exchange tab, send a test message with the key `report.high` and confirm it landed only in the high queue.
5. (Optional) run a second worker on the high queue and watch urgent reports overtake background ones.

## Exercise 5: Dead-letter — retry → DLQ, worked by hand

1. Declare `reports.tasks` with the arguments `x-dead-letter-exchange` and `x-dead-letter-routing-key` pointing at the DLX `reports.dlx` and the queue `reports.dlq`.
2. In the worker, on a processing error, issue `basic_nack` with `requeue=false` — that sends the poison message to the DLQ instead of spinning it round the loop.
3. Kill the consumer (`kill` the worker) halfway through processing, and watch in the UI that the unacked message came back to the queue (redelivered = true).
4. Publish a task that is guaranteed to fail (a non-existent period raising an exception in the worker, say). Show the chain in the UI: attempt → nack → DLQ. Check the scenario against the bank question `queue-messaging/design-rabbitmq-dead-lettering.md`.
5. Work the DLQ by hand: read the message, look at the `x-death` headers (how many times it died and why), then either republish it corrected or delete it deliberately. "Quietly dropping a business message" is the anti-pattern named in the bank's answer.

## Exercise 6: Observability — queue depth in Grafana

1. Collect the queue-depth metric by either route:
    * the management API: `curl -u app:<pass> http://<vm3-ip>:15672/api/queues/reports` → the `messages` field;
    * or the ready-made `rabbitmq_exporter` (in docker, beside the broker).
2. Add the source to the existing Prometheus/Grafana stack and build a dashboard panel: the depth of `reports.tasks` and `reports.dlq`, plus the publish/deliver rate.
3. Load the endpoint with a loop of 100 requests and stop the worker — show the queue depth climbing on the graph, then start the worker and watch it drain. State it plainly: what queue depth means "time to call someone" for you, and why.

## Exercise 7: Defence — RabbitMQ vs Kafka, three questions of understanding

Prepare answers in your own words (a paragraph each, not a retelling of the documentation):

1. **Durability.** What do a durable queue plus a persistent message guarantee in RabbitMQ, and what do they not? Why is that usually enough for reports but not enough where a week of replay is asked for?
2. **Ack.** How does a consumer ack differ from a publisher confirm? What happens to an unacked message when the worker dies, and why does that make the processing at-least-once rather than exactly-once?
3. **At-least-once.** Given a message can arrive twice, what must the consumer do so that this does not break the business logic? Give your own example from this lab (the write to PG).

Then check yourself against the bank questions `queue-messaging/choose-a-queue-or-log.md` and `queue-messaging/explain-delivery-semantics.md` — an answer to "when RabbitMQ, when Kafka" has to rest on the difference between a queue and a distributed log.

## Readiness criteria

The broker is up through compose; the asynchronous path works end to end (202 → queue → PG); priorities on the routing key are demonstrated; the DLQ is shown and worked by hand; queue depth is visible in Grafana; and the three defence questions have clear answers.
