SHELL := /bin/bash
.PHONY: up down logs migrate seed test build ci

up:
	docker compose up -d

down:
	docker compose down -v

logs:
	docker compose logs -f --tail=200

migrate:
	docker compose exec backend alembic upgrade head

test:
	pytest -q backend

build:
	docker compose build

ci: build up migrate test
