# CloudVPS Pro – Upgrade Bundle for VPN Panel Pro

This bundle adds a **fake VPS landing site**, **advanced auth (2FA, email verify, captcha)**, **admin panel**, **payments (Stripe/PayPal/ZarinPal/NextPay/Crypto stubs)**, **PostgreSQL/Redis/Celery/WebSockets**, **API v1/v2 with Swagger**, **Prometheus metrics & health**, **security hardening**, **Grafana/Prometheus monitoring**, **alert hooks**, **mobile API**, **internationalization**, **PWA React SPA with Tailwind**, **CI/CD**, **Kubernetes/Terraform skeletons**, and **documentation**—while aiming for **backward compatibility** via API versioning and migrations.

> **How to use**: You can drop this into a new repo and migrate your existing code in, or copy folders piece‑by‑piece into your current project. Files are heavily commented. Start with `docker-compose.yml` for a turnkey dev environment.

## Quick Start (Dev)
```bash
# 1) Copy repo or unzip as-is
cp -r cloudvps_pro_upgrade_bundle your-project && cd your-project

# 2) Environment
cp .env.example .env
# Edit secrets (JWT, DB, SMTP, payment keys, Cloudflare, etc.)

# 3) Run everything
docker compose up --build

# Frontend: http://localhost:5173
# Backend:  http://localhost:8000
# Swagger:  http://localhost:8000/docs (v1), http://localhost:8000/redoc
# Admin:    http://localhost:5173/admin
```

## Backward Compatibility
- **API Versioning**: old clients can keep using `/api/v1`. New features on `/api/v2`.
- **DB Migrations**: Alembic migrations provided. Includes SQLite→PostgreSQL migration guide.
- **Auth Tokens**: JWT structure compatible with common clients; include `sub`, `exp`, and `scopes`.

See `docs/` for deployment guides and `infra/` for k8s/terraform.

## One-line Install (Docker)
After you push this repo to GitHub, you (or users) can run:
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/<your-username>/<your-repo>/main/scripts/install.sh)"
```
*(Replace `<your-username>/<your-repo>` with your GitHub path.)*

## GitHub Actions
- **CI**: builds frontend, runs backend tests, ensures compile passes.
- **Compose Smoke Test**: spins up the full stack in CI, runs health checks and Alembic migrations.

## Codespaces / Dev Container
Open in GitHub Codespaces or VS Code Remote Containers for a pre-wired environment.
