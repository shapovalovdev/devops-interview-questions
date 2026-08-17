# Builder: render the Markdown corpus into build/site/ with the
# stdlib-only own-build pipeline.
FROM python:3.13-alpine AS builder
WORKDIR /site
COPY . .
RUN python3 scripts/build_site.py

# Runtime: nginx:alpine serving the static build unprivileged on 8080.
# Chosen over caddy for a smaller image, dead-simple static config, and
# busybox wget built in for the HEALTHCHECK.
FROM nginx:alpine
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /site/build/site /usr/share/nginx/html
EXPOSE 8080
USER nginx
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -q --spider http://127.0.0.1:8080/ || exit 1
CMD ["nginx", "-g", "daemon off;"]
