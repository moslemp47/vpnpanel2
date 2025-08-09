# CHANGELOG

## v3.0.0 – 2025-08-09
- Brand-new **CloudVPS Pro** landing (fake VPS store) with blue/gray theme.
- **Advanced Auth**: 2FA (TOTP), email verification, password reset, sessions/devices, avatar upload, captcha.
- **Admin panel** under `/admin` with users/plans/servers/logs/finance/settings/tickets.
- **Payments**: Stripe, PayPal, ZarinPal, NextPay, Crypto (stubs with webhooks & invoice PDFs).
- **PostgreSQL**, **Redis** (cache/session), **Celery** (email, auto-renew, alerts), **WebSockets** (notifications).
- **Monitoring**: Prometheus metrics, health endpoints, Grafana dashboards stubs, alert hooks.
- **Security**: WAF rules samples, Cloudflare notes, IP lists, geo-blocking hooks, CSP/HSTS, rate limits.
- **User features**: i18n (en, fa, ar, zh), dark/light, QR codes, 1‑click copy, usage charts, speed tests,
  multi-config management, auto-renew, app downloads, export formats.
- **DevOps**: Docker, docker-compose, GitHub Actions, k8s manifests, Terraform skeletons, backups, blue‑green.
- **Compliance**: GDPR helpers, ToS/Privacy versions, data export & deletion, cookie consent.
- **Docs**: User/Admin/Developer guides, Postman collection, troubleshooting & security best practices.
