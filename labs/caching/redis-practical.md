---
title: "Redis as a Flask application cache: from a hand-rolled cache to TTL and eviction"
theme: "caching"
difficulty: "middle"
question_ref: "caching/redis-maxmemory-tuning.md"
tags: [caching, redis, docker, prometheus, monitoring, memory, healthchecks]
why: "A cache layer is named in most infrastructure job descriptions, and Redis by name in many of them, yet candidates usually stop at installing it. This lab teaches hit-ratio thinking: cache-aside in the Flask app, TTL and invalidation choices, maxmemory eviction experiments with allkeys-lru versus volatile-star policies, and cache failure modes like stampede — the interview questions behind the install command."
checklist:
  - "Redis is added to the stand's docker-compose with a healthcheck (redis-cli ping) and a depends_on link from Flask; the container reports healthy."
  - "A cache-aside layer in Flask has cached a heavy read from PostgreSQL: the repeat request is served from Redis (proven by logs or the key's TTL)."
  - "Keys are named deliberately (entity prefix + id), and their lifetime is visible through TTL."
  - "TTLs are chosen and justified for slow-moving and fast-moving data; invalidation on UPDATE through the application is demonstrated."
  - "The staleness behaviour is decided: re-read from PG or serve stale — the decision is documented."
  - "The maxmemory experiment is done: under a small limit allkeys-lru evicts keys, noeviction returns OOM errors, and volatile-ttl with no TTL keys behaves like noeviction."
  - "The persistence decision is recorded: RDB/AOF on or off for a cache, with the cost of recovery argued."
  - "redis_exporter is wired into Prometheus; Grafana shows the hit ratio (keyspace hits/misses) and evicted_keys."
  - "A load test (ab/wrk/a script) shows the hit ratio rising after warm-up, and a drop on a cold cache before it."
  - "Answered in your own words: what a cache stampede is and how to soften it, what hit ratio is, and how a cache differs from a queue."
---

# Lab: Redis as a Flask application cache — from a hand-rolled cache to TTL and eviction

## The stand

The existing stand: 3 Ubuntu VMs — the Flask application + nginx, PostgreSQL, and the Ansible control host. The application already serves requests, and it contains one "heavy" read from PostgreSQL (a report, an aggregation, a list with JOINs) that takes longer than ~200 ms. The point of the lab is to move that read path into Redis and take the cache to a state worth showing at an interview: with a TTL, an eviction policy, metrics, and an understanding of its failure modes.

The mental frame for the whole lab: **a cache is about hit ratio and degradation, not about installation**. Each exercise ends not at "it works" but at "I understand what will break and how that shows on a graph".

Time for the lab: 5-7 hours.

Useful references:

- Eviction heuristics and policies in Redis: <https://redis.io/docs/latest/develop/reference/eviction/>
- Persistence in Redis (RDB/AOF): <https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/>
- The INFO command and its fields: <https://redis.io/docs/latest/commands/info/>
- redis_exporter for Prometheus: <https://github.com/oliver006/redis_exporter>
- Docker Compose: <https://docs.docker.com/compose/>
- Flask: <https://flask.palletsprojects.com/>

---

## Exercise 1: Redis in docker-compose + healthcheck

1. Add a Redis service to the application's existing `docker-compose.yml`: a pinned image version (not `latest`), and the port kept inside the compose network (do not publish 6379 outwards without a reason).
2. Declare a `healthcheck`:

   ```yaml
   healthcheck:
     test: ["CMD", "redis-cli", "ping"]
     interval: 5s
     timeout: 3s
     retries: 5
   ```

3. Tie the Flask service to Redis with `depends_on` and `condition: service_healthy` — the application should not start into a world where Redis is not answering yet.
4. Check: `docker compose ps` reports `healthy`, and `docker compose logs flask` shows a successful connection at start-up.
5. Test start-up resilience: `docker compose stop redis && docker compose up -d flask` — what happens? The application should either wait or fail with a clear error, but never hang silently.

## Exercise 2: The caching layer in Flask — cache-aside

1. Find the heavy PostgreSQL read in the application (or create one: `SELECT ... GROUP BY ...` over a large table, so the query takes 100-500 ms).
2. Implement the **cache-aside** pattern (lazy loading): the application looks for the key in Redis first, and on a miss reads PostgreSQL and writes the result back. Serialise with JSON or msgpack.
3. Name keys on a scheme like `entity:id` or `report:region:date` — a deliberate key design, not `cache_17`.
4. Measure the effect: log the response time before and after. The first request is a miss (as slow as it was), the repeats are single-digit milliseconds.
5. Handle Redis being unavailable, without fail: if the cache does not answer, the application must go to PostgreSQL — a cache makes things faster, it is not the single source of truth. Demonstrate it: `docker compose stop redis` — the application answers slowly, but it answers.

## Exercise 3: TTL and invalidation

1. Set a TTL on every key (`SET ... EX <seconds>` or `setex`). Choose different TTLs for different data: a slow-moving reference table gets hours, a live aggregation gets seconds.
2. Check: `TTL <key>` shows the remainder; once it expires the key disappears, and the next request is a miss and a re-read from PG.
3. Implement invalidation on write: on `UPDATE`/`DELETE` of the affected entity, the application deletes or overwrites the key (`DEL`, or writing the new values). The cache must never serve data older than the source by more than the TTL.
4. **A decision to make:** on staleness, do you re-read from PG (plain cache-aside) or serve the old value and refresh in the background (stale-while-revalidate)? Implement the simple one, describe the second in words, and explain when it is justified.

## Exercise 4: Eviction policies and the maxmemory experiment

1. Set a small `maxmemory` in the Redis config (2-4 MB, say) — small enough that the cache certainly will not fit.
2. With `maxmemory-policy allkeys-lru`, fill the cache from a script (hundreds of keys, a few KB each). Watch `redis-cli INFO memory`: `used_memory` presses against the limit, and `evicted_keys` climbs in `INFO stats`.
3. Switch to `noeviction`: watch writes start failing with `OOM command not allowed`. Explain why that is a poor default for a pure cache.
4. Switch to `volatile-ttl` and remove the TTL from some of the keys: confirm that keys without a TTL are not evicted, and that with no TTL keys at all the policy behaves like `noeviction` — the classic trap.
5. State the selection rule: `allkeys-lru` when Redis is only a cache; `volatile-*` when one instance holds both cache keys with a TTL and keys that must not be lost (and why doing that is a compromise).

## Exercise 5: Observability — redis_exporter → Prometheus/Grafana

1. Stand up `redis_exporter` (in compose) and add it as a target to the stand's existing Prometheus.
2. In Grafana, build a panel for the **hit ratio**: `rate(redis_keyspace_hits_total[5m]) / (rate(redis_keyspace_hits_total[5m]) + rate(redis_keyspace_misses_total[5m]))`, plus `redis_evicted_keys_total`, `redis_memory_used_bytes`, and `redis_connected_clients`.
3. Warm the cache with a load script (`ab`, `wrk`, or a Python loop): the hit ratio should climb to ~0.9+; then stop Redis or clear the keys (`FLUSHDB`) and watch it fall to 0 with a spike in misses.
4. Answer in writing: what hit ratio counts as acceptable for your case, and at what value does the cache stop paying for itself?

## Exercise 6: Defence and understanding — persistence and three questions

1. **Does a cache need persistence?** Work through RDB and AOF: what each gives you, and what it costs in writes and in disk. For a pure cache, persistence is usually turned off (`save ""`, `appendonly no`): after a restart the cache simply warms up again. Record the decision and its price (a cold start, and the hit PG takes during warm-up).
2. Test your understanding on three questions — answer in your own words, without a search engine, then check yourself against the question bank:
   - What is a **cache stampede**, and how do you soften it (TTL jitter, a lock around the re-read, warm-up)?
   - What is **hit ratio**, and why is it the cache's headline metric rather than memory used?
   - How does a **cache differ from a message queue** (Redis is often used as both here — what is the difference in semantics: read speed against delivery guarantees)?
3. Talk through the failure scenario: Redis has died in production — what does the user see, what does the hit ratio show, and how does PostgreSQL degrade. This is the favourite "what if..." format at interviews.
