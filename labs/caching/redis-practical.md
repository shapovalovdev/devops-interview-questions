---
title: "Redis как кэш Flask-приложения: от ручного кэша к TTL и eviction"
theme: "caching"
difficulty: "middle"
question_ref: "caching/redis-maxmemory-tuning.md"
tags: [caching, redis, docker, prometheus, monitoring, memory, healthchecks]
why: "A cache layer is named in four of the eight analyzed vacancies (Interlizing, efin, T1 pattern names Redis explicitly), yet candidates usually stop at installing it. This lab teaches hit-ratio thinking: cache-aside in the Flask app, TTL and invalidation choices, maxmemory eviction experiments with allkeys-lru versus volatile-star policies, and cache failure modes like stampede — the interview questions behind the install command."
checklist:
  - "Redis добавлен в docker-compose стендa с healthcheck (redis-cli ping) и зависит_от-связью с Flask; контейнер healthy."
  - "Cache-aside слой в Flask закэшировал тяжёлую выборку из PostgreSQL: повторный запрос идёт из Redis (проверено логами/TTL ключа)."
  - "Ключи именованы осознанно (префикс сущности + id), время жизни видно через TTL."
  - "TTL подобран и обоснован для медленно и быстро меняющихся данных; инвалидация при UPDATE через приложение показана."
  - "Поведение при устаревании определено: перечитать из PG или отдать stale — решение задокументировано."
  - "Эксперимент с maxmemory: при малом лимите allkeys-lru вытесняет ключи, noeviction возвращает OOM-ошибки; volatile-ttl без TTL-ключей ведёт себя как noeviction."
  - "Решение по persistence зафиксировано: RDB/AOF включены или выключены для кэша — с обоснованием цены восстановления."
  - "redis_exporter подключён к Prometheus; в Grafana виден hit ratio (keyspace hits/misses) и evicted_keys."
  - "Нагрузочный тест (ab/wrk/скрипт) показывает рост hit ratio после прогрева; до прогрева — падение на холодном кэше."
  - "Даны ответы своими словами: что такое cache stampede и как его смягчить, что такое hit ratio, чем кэш отличается от очереди."
---

# Lab: Redis как кэш Flask-приложения — от ручного кэша к TTL и eviction

## Контекст стенда

Существующий стенд: 3 VM на Ubuntu — Flask-приложение + nginx, PostgreSQL, Ansible control. Приложение уже обрабатывает запросы; в нём есть «тяжёлая» выборка из PostgreSQL (отчёт, агрегация, список с JOIN'ами), которая выполняется дольше ~200 мс. Цель лабы — вынести этот путь чтения в Redis и довести кэш до состояния, которое не стыдно показать на интервью: с TTL, eviction-политикой, метриками и пониманием режимов отказа.

Ментальная рамка на всю лабу: **кэш — это про hit ratio и деградацию, а не про установку**. Каждое упражнение заканчивается не «работает», а «понимаю, что сломается и как это видно на графике».

Время на лаб: 5–7 часов.

Полезные ссылки:

- Эвристики и политики eviction в Redis: <https://redis.io/docs/latest/develop/reference/eviction/>
- Persistence в Redis (RDB/AOF): <https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/>
- Команда INFO и её поля: <https://redis.io/docs/latest/commands/info/>
- redis_exporter для Prometheus: <https://github.com/oliver006/redis_exporter>
- Docker Compose: <https://docs.docker.com/compose/>
- Flask: <https://flask.palletsprojects.com/>

---

## Exercise 1: Redis в docker-compose + healthcheck

1. Добавь сервис Redis в существующий `docker-compose.yml` приложения: фиксированная версия образа (не `latest`), порт только внутри сети compose (не публикуй 6379 наружу без нужды).
2. Пропиши `healthcheck`:

   ```yaml
   healthcheck:
     test: ["CMD", "redis-cli", "ping"]
     interval: 5s
     timeout: 3s
     retries: 5
   ```

3. Свяжи Flask-сервис с Redis через `depends_on` с `condition: service_healthy` — приложение не должно стартовать в мир, где Redis ещё не отвечает.
4. Проверь: `docker compose ps` показывает `healthy`, а `docker compose logs flask` — успешное подключение при старте.
5. Проверь отказоустойчивость старта: `docker compose stop redis && docker compose up -d flask` — что произойдёт? Приложение должно либо дождаться, либо упасть с внятной ошибкой, но не виснуть молча.

## Exercise 2: Кэширующий слой в Flask — cache-aside

1. Найди в приложении тяжёлую выборку из PostgreSQL (или создай её: `SELECT ... GROUP BY ...` по большой таблице, чтобы запрос занимал 100–500 мс).
2. Реализуй паттерн **cache-aside** (lazy loading): приложение сначала ищет ключ в Redis, при промахе читает PostgreSQL и записывает результат обратно. Серийизация — JSON или msgpack.
3. Ключи именуй по схеме `entity:id` или `report:region:date` — осознанный дизайн ключа, а не `cache_17`.
4. Померь эффект: логируй время ответа до и после. Первый запрос — промах (время как было), повторные — единицы миллисекунд.
5. Обязательно обработай недоступность Redis: если кэш не отвечает, приложение должно идти в PostgreSQL (кэш ускоряет, а не является единственной точкой правды). Продемонстрируй: `docker compose stop redis` — приложение отвечает медленно, но отвечает.

## Exercise 3: TTL и инвалидация

1. Назначь TTL на каждый ключ (`SET ... EX <seconds>` или `setex`). Подбери разные TTL для разных данных: медленно меняющийся справочник — часы, «живая» агрегация — секунды.
2. Проверь: `TTL <key>` показывает остаток; после истечения ключ исчезает, следующий запрос — снова промах и перечитывание из PG.
3. Реализуй инвалидацию при записи: на `UPDATE`/`DELETE` затронутой сущности приложение удаляет или перезаписывает ключ (`DEL`, или запись новых значений). Кэш никогда не должен отдавать данные старше, чем источник, дольше чем на TTL.
4. **Вопрос на решение:** что отдаём при устаревании — перечитать из PG (простой cache-aside) или сначала отдать старое, а обновить фоном (stale-while-revalidate)? Реализуй простой вариант, второй — опиши словами и объясни, когда он оправдан.

## Exercise 4: Eviction-политики и эксперимент с maxmemory

1. Установи в конфиге Redis маленький `maxmemory` (например, 2–4 MB) — так, чтобы кэш заведомо не влез.
2. С `maxmemory-policy allkeys-lru` наполни кэш скриптом (сотни ключей по несколько KB). Наблюдай в `redis-cli INFO memory`: `used_memory` упирается в лимит, в `INFO stats` растёт `evicted_keys`.
3. Переключи на `noeviction`: увидь, что записи начинают падать с ошибкой `OOM command not allowed`. Объясни, почему это плохой дефолт для чистого кэша.
4. Переключи на `volatile-ttl` и убери TTL у части ключей: убедись, что ключи без TTL не вытесняются, и при отсутствии TTL-ключей политика ведёт себя как `noeviction` — классическая ловушка.
5. Сформулируй правило выбора: `allkeys-lru` — когда Redis только кэш; `volatile-*` — когда в одном инстансе живут и кэш-ключи с TTL, и ключи, которые нельзя терять (и почему так делать — компромисс).

## Exercise 5: Наблюдаемость — redis_exporter → Prometheus/Grafana

1. Подними `redis_exporter` (compose) и добавь его таргетом в существующий Prometheus стенда.
2. В Grafana построй панель с **hit ratio**: `rate(redis_keyspace_hits_total[5m]) / (rate(redis_keyspace_hits_total[5m]) + rate(redis_keyspace_misses_total[5m]))`, плюс `redis_evicted_keys_total`, `redis_memory_used_bytes`, `redis_connected_clients`.
3. Прогрей кэш нагрузочным скриптом (`ab`, `wrk` или цикл на Python): hit ratio должен расти до ~0.9+; останови Redis или почисти ключи (`FLUSHDB`) — увидь падение в 0 и всплеск misses.
4. Ответь письменно: какой hit ratio считается приемлемым для твоего случая и при каком значении кэш перестаёт окупаться?

## Exercise 6: Защита и понимание — persistence и три вопроса

1. **Persistence для кэша — нужен ли?** Разберись с RDB и AOF: что даёт каждый, сколько стоит по записи и по диску. Для чистого кэша обычно persistence отключают (`save ""`, `appendonly no`): после рестарта кэш просто прогревается заново. Зафиксируй решение и его цену (холодный старт, удар по PG при прогреве).
2. Проверь осознанность на трёх вопросах — ответь своими словами, без гугла, потом сверься с банком вопросов:
   - Что такое **cache stampede** и как его смягчить (TTL-шум, блокировка перечитывания, прогрев)?
   - Что такое **hit ratio** и почему это главная метрика кэша, а не объём памяти?
   - Чем **кэш отличается от очереди сообщений** (Redis здесь часто используют и так, и так — в чём разница semantics: скорость чтения против гарантии доставки)?
3. Проговори сценарий отказа: Redis упал в проде — что видит пользователь, что показывает hit ratio, как деградирует PostgreSQL. Это любимый формат вопросов «а что если…» на интервью.
