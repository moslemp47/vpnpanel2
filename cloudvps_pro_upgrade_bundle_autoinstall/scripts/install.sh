#!/usr/bin/env bash
set -euo pipefail

echo "▶ CloudVPS Pro – One-Line Installer (Docker)"
command -v docker >/dev/null 2>&1 || { echo "✖ Docker not found. Install Docker and try again."; exit 1; }

# docker compose plugin fallback to docker-compose
if docker compose version >/dev/null 2>&1; then
  DC="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
  DC="docker-compose"
else
  echo "✖ docker compose not found. Install Docker Compose."
  exit 1
fi

# Ensure we're in repo root
if [ ! -f "docker-compose.yml" ]; then
  echo "✖ Run this inside the project root (where docker-compose.yml exists)."
  exit 1
fi

# Generate .env if missing
if [ ! -f ".env" ]; then
  echo "• Generating .env"
  SECRET=$(python - <<'PY'\nimport secrets; print(secrets.token_urlsafe(48))\nPY\n)
  cat > .env <<EOF
APP_NAME=CloudVPS Pro
ENV=production
SECRET_KEY=${SECRET}
JWT_ACCESS_EXPIRES_MIN=30
JWT_REFRESH_EXPIRES_DAYS=30
DB_ENGINE=postgresql
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=cloudvps
POSTGRES_USER=cloudvps
POSTGRES_PASSWORD=cloudvps
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0
SMTP_HOST=
SMTP_PORT=587
SMTP_USER=
SMTP_PASSWORD=
SMTP_FROM=noreply@example.com
HCAPTCHA_SITEKEY=
HCAPTCHA_SECRET=
STRIPE_SECRET=
STRIPE_WEBHOOK_SECRET=
PAYPAL_CLIENT_ID=
PAYPAL_CLIENT_SECRET=
ZARINPAL_MERCHANT_ID=
NEXTPAY_API_KEY=
BTCPAY_SERVER_URL=
BTCPAY_API_KEY=
PROMETHEUS_MULTIPROC_DIR=/tmp
VITE_API_BASE=http://localhost:8000
VITE_APP_NAME=CloudVPS Pro
EOF
fi

echo "• Pulling & building images…"
$DC pull || true
$DC build --no-cache

echo "• Starting stack…"
$DC up -d

# Wait for backend health
echo -n "• Waiting for backend health"
RETRIES=60
until curl -fsS http://localhost:8000/healthz >/dev/null 2>&1; do
  sleep 2; printf "."
  RETRIES=$((RETRIES-1))
  if [ $RETRIES -le 0 ]; then
    echo; echo "✖ Backend failed to become healthy. Check logs: $DC logs backend"
    exit 1
  fi
done
echo " ok"

echo "• Running DB migrations…"
$DC exec -T backend alembic upgrade head || { echo "✖ Alembic migration failed"; exit 1; }

echo "• Smoke testing APIs…"
curl -fsS http://localhost:8000/api/v1/status >/dev/null
curl -fsS http://localhost:8000/metrics >/dev/null

echo "✔ Done!"
echo "Frontend:  http://localhost:5173"
echo "Backend:   http://localhost:8000 (Swagger: /docs)"
