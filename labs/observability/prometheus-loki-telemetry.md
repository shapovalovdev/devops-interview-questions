---
title: "Мониторинг и логи на существующем стенде: Prometheus + Alertmanager + Loki + Grafana"
theme: "observability"
difficulty: "middle"
question_ref: "observability/build-an-actionable-alert.md"
tags: [observability, monitoring, logging, prometheus, ansible]
why: "Monitoring appears in eight of the eight analyzed vacancies and logging in six of eight; Loki covers the practical logging side more cheaply and simply than ELK, and correlating metrics with logs in a single dashboard is exactly what Ostrovok, T1, and efin interviews ask for. A candidate with production Zabbix+Grafana experience and pet-level Prometheus closes the main gap here: transferring scattered Zabbix experience onto the Prometheus stack and learning to tie an alert to its cause through logs."
checklist:
  - "Prometheus и node_exporter подняты на всех 3 VM; все таргеты видны как UP в /targets."
  - "Scrape-конфиги объявлены декларативно (Ansible role или docker-compose) и воспроизводятся повторным запуском."
  - "Настроены 2–3 алерт-правила: instance down, disk usage > 85%, Flask 5xx/latency; правила загружены без ошибок (проверка через /rules)."
  - "Alertmanager доставляет алерт в реальный канал (email/webhook/Telegram), а не только в UI."
  - "Каждый алерт проверен генерацией реального события: остановлен exporter, заполнен диск, сгенерированы 5xx."
  - "Loki + Promtail запущены; journald и логи Flask/PostgreSQL реально приходят в Loki."
  - "LogQL-запросы работают: фильтрация по сервису, grep по ошибке, подсчёт rate за интервал."
  - "Единый Grafana-дашборд показывает метрики и логи рядом; корреляция по времени работает."
  - "Сломай-и-почини: уроненный exporter вызывает алерт; причина найдена по логам в Loki, а не по подсказке."
  - "Повторный deploy через Ansible (или docker-compose up) идемпотентен: nothing changed / контейнеры не пересоздаются без причины."
---

# Lab: Мониторинг и логи на существующем стенде: Prometheus + Alertmanager + Loki + Grafana

## Контекст и окружение

Стенд из предыдущих лабов: 3 VM на Ubuntu — `vm1` (Flask-приложение + nginx), `vm2` (PostgreSQL), `vm3` (Ansible control + app-хост). Всё управление — через Ansible. Задача — навесить полноценный observability-стек на живой стенд, не сломав приложение.

**Ключевое решение, которое нужно защитить:** деплой стека через Ansible role (systemd-сервисы) или через docker-compose на выделенной ноде. У обоих подходов есть цена: Ansible — больше ролей и шаблонов, зато единый менеджмент со стендом; docker-compose — быстрее поднять, но появляется вторая система деплоя. Выбор нужно аргументировать, а не взять по умолчанию.

Время на лаб: 6–8 часов. Машины: 3 VM, по 2 vCPU / 2–4 GB RAM.

---

## Exercise 1: Prometheus + node_exporter на все 3 VM

1. Установи Prometheus (сервер) и node_exporter (на все 3 VM) выбранным способом.
2. Напиши scrape-конфиг: статические таргеты для всех 3 VM (`:9100`), плюс app-метрики Flask (`/metrics` или через экспортер — если Flask их не отдаёт, добавь `prometheus_client` в приложение или поставь blackbox_exporter на http-эндпоинт).
3. Проверь: `http://<prometheus>:9090/targets` — все таргеты UP.
4. Сделай так, чтобы список таргетов не приходилось править руками при добавлении VM (inventory Ansible → шаблон `prometheus.yml.j2`, или file-based SD).

## Exercise 2: Осмысленные алерты через Alertmanager

1. Подними Alertmanager и соедини его с Prometheus.
2. Напиши 2–3 alert-правила, каждое из которых проходит тест «actionable alert» (см. question_ref):
   - `instance down` — `up == 0` больше 1–2 минут;
   - disk usage > 85% — `node_filesystem_avail_bytes / node_filesystem_size_bytes`;
   - Flask 5xx rate или p95 latency — по метрикам приложения.
3. Для каждого алерта: severity, описание с первым диагностическим шагом, routing в Alertmanager (например, critical → Telegram/webhook, warning → email).
4. **Проверка не «на глаз»:** каждый алерт обязан сработать от реального события (см. Exercise 5). Алерт, который ни разу не стрелял, считается не существующим.

## Exercise 3: Loki + Promtail: journald и логи сервисов

1. Подними Loki (single-binary достаточно) и Promtail на каждой VM.
2. Настрой Promtail: `journal`-scrape (unit-ы Flask, PostgreSQL, node_exporter) + файловые логи Flask/nginx, если они пишутся в файлы. Добавь метки: `host`, `unit`, `service`.
3. Проверь приход данных: запрос в Grafana Explore — `{job="journal", host="vm1"}` и `{service="flask"}`.
4. Ответь на вопрос защиты: почему метки в Loki — это не то же самое, что метки в Prometheus, и что будет с Loki при высококардинальных метках вроде user_id.

## Exercise 4: Единый Grafana-дашборд: метрики + логи рядом

1. Подключи Grafana к обоим источникам: Prometheus и Loki.
2. Собери один дашборд на стенд: CPU/memory/disk по VM, availability Flask, rate 5xx — и рядом log-панель с логами приложения за то же окно времени.
3. Проверь корреляцию: при инциденте из Exercise 5 в один клик видно всплеск метрики и соответствующие строки логов в том же временном окне.
4. Отработай ad-hoc LogQL: найти все 5xx за последний час, посчитать `rate` ошибок по сервисам, найти конкретный traceback.

## Exercise 5: Сломай-и-почини (мост к chaos-sandbox Phase 2)

1. Урони node_exporter на одной из VM: `sudo systemctl stop node_exporter`.
2. Пройди полный цикл реагирования: алерт пришёл → в Grafana видно, какой таргет пропал → по логам journald в Loki (`{unit="node_exporter"}`) найди причину остановки.
3. Повтори с более сложным сценарием: урони Flask так, чтобы nginx отдавал 5xx (или сгенерируй ошибки нагрузкой на сломанном бэкенде) — алерт по 5xx должен прийти, а причина — находиться в логах, а не угадываться.
4. Запиши TTR (time-to-recovery) для обоих инцидентов. Это прямая подготовка к Phase 2 chaos-sandbox: реконструкция инцидента по Grafana/Loki и blameless post-mortem.
5. Почини. Убедись, что алерт resolved пришёл тем же каналом.

## Exercise 6: Идемпотентность всего стека мониторинга

1. Весь стек мониторинга должен подниматься одним запуском Ansible-playbook (или `docker-compose up -d`) с нуля на чистых VM.
2. Запусти deploy повторно на живом стенде: сервисы не должны перезапускаться, конфиги — меняться, дашборды — дублироваться. Grafana-дашборды и datasource-ы декларативно (provisioning, не руками в UI).
3. Проверь: `ansible-playbook ... --check --diff` не показывает изменений; alert-правила и Promtail-конфигы шаблонизированы.
4. Защита: что произойдёт со стеком мониторинга при полном пересоздании стенда, и где ты это зафиксировал в коде, а не в памяти.

---

## Критерии сдачи

- Все пункты checklist закрыты скриншотами/выводом команд.
- Выбор Ansible vs docker-compose аргументирован (минимум 2 осмысленных аргумента за и 1 против своего выбора).
- Exercise 5 показан end-to-end: алерт → дашборд → логи → фикс → resolved.
