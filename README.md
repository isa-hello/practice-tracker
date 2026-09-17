# Practice Tracker

A small web app to replace the hand-maintained `PROGRESS.md` in the `fall` repo:
log LeetCode problems as you solve them, flag which ones needed help, and
automatically surface which ones are due for a cold retest (per the
"revisit cold after ~3 days if it needed heavy help" rule already in use).

## Status

**Phase 1 (in progress):** core app running locally against SQLite.
**Phase 2 (not started):** Terraform config provisioning Azure App Service +
Azure Database for PostgreSQL Flexible Server.
**Phase 3 (not started):** deploy the real app to Azure, verified live.

## v1 scope (smaller)

- Add a solved problem: title, pattern/category, difficulty, date solved,
  whether it needed help, notes.
- View a list of all logged problems.
- See which problems are currently due for a cold retest.
- Mark a cold retest as completed.

Nothing else yet. No auth, no editing/deleting, no fancy UI. Get this working
end to end first.

## Stack

- Backend: Flask
- DB (local dev): SQLite via Flask-SQLAlchemy
- DB (deployed, later): Azure Database for PostgreSQL Flexible Server
- Frontend: plain Flask/Jinja2 templates, minimal CSS
- Infra (later): Terraform, targeting Azure (App Service + PostgreSQL)

## Local setup

```
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

## Files

- `app.py` — Flask routes. Stubbed with docstrings describing what each
  route should do — fill in the logic.
- `models.py` — the `Problem` database model. Field list is sketched as a
  comment — you decide the actual types/structure.
- `logic.py` — `is_retest_due()`, the one pure function with fixed test
  cases already written in `tests/test_logic.py`. Same pattern as the
  LeetCode stubs: tests are given, implementation isn't.
- `templates/` — empty for now. Build these once the routes work.
