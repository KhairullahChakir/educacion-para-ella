#!/usr/bin/env bash
# Build only the isolated Render testing service.
# Never point this service at production data.
set -euo pipefail

if [[ "${DJANGO_ENV:-}" != "production" || "${DEBUG:-}" != "False" ]]; then
    echo "Testing deployment requires DJANGO_ENV=production and DEBUG=False." >&2
    exit 1
fi

# Require an explicitly named Neon test database. Do not silently fall back to
# the local SQLite database or accept a Render/Postgres production URL.
python - <<'PY'
import os
from urllib.parse import unquote, urlsplit

database_url = os.environ.get("DATABASE_URL", "")
test_database_name = os.environ.get("NEON_TEST_DATABASE_NAME", "")
try:
    parsed = urlsplit(database_url)
    database_name = unquote(parsed.path.removeprefix("/").split("/", 1)[0])
except ValueError:
    parsed = None
    database_name = ""

if (
    parsed is None
    or parsed.scheme not in {"postgres", "postgresql", "postgresql+psycopg2"}
    or not parsed.hostname
    or not parsed.hostname.endswith(".neon.tech")
    or not test_database_name
    or database_name != test_database_name
):
    raise SystemExit(
        "Testing deployment requires DATABASE_URL for the Neon database named by "
        "NEON_TEST_DATABASE_NAME."
    )

print("Verified Neon testing database target (connection details hidden).")
PY

pip install -r requirements.txt

# Create/update the schema before collectstatic or the web process can access it.
python manage.py migrate --noinput
python manage.py migrate --check

# Fail the build if the table implicated in the reported error is still absent.
python manage.py shell -c "from django.db import connection; tables = set(connection.introspection.table_names()); assert 'core_footersetting' in tables, 'Required table core_footersetting is missing after migrations.'"

python manage.py collectstatic --no-input
