# SQLite → PostgreSQL Migration
1) Stop the app and back up your SQLite file (`/data/app.db`).
2) Export with `sqlite3 /data/app.db .dump > dump.sql` and transform types as needed.
3) Create Postgres schema via Alembic (`alembic upgrade head`).
4) Transform and import data into Postgres.
