# Practice Tracker

A small web app to replace the hand-maintained `PROGRESS.md` in the `fall` repo:
log LeetCode problems as you solve them, flag which ones needed help, and
automatically surface which ones are due for a cold retest (per the
"revisit cold after ~3 days if it needed heavy help" rule already in use).

## Status

**Phase 1 (done, now hardening):** the app runs locally against SQLite and
covers more than the original v1 scope. What remains in this phase is
robustness fixes and the "How it works" section below.
**Phase 2 (not started):** move configuration to environment variables, then
a Terraform config provisioning Azure App Service + Azure Database for
PostgreSQL Flexible Server.
**Phase 3 (not started):** deploy the real app to Azure, verified live.

## Features

- Log a solved problem: title, pattern/category, difficulty, date solved,
  whether it needed help, whether to repeat retests, notes.
- Dashboard listing every logged problem with its full retest status.
- A problem is due for a cold retest when it needed help and enough days
  have passed since the last event (the solve, or the most recent retest).
  The default interval is 3 days.
- Mark a retest as completed. With "repeat retests" on, the interval
  doubles after each completed retest (3, 6, 12 days, and so on).
- Edit and delete logged problems.

Out of scope for now: auth or multi-user support, LeetCode import/scraping,
notifications, an API layer.

## Stack

- Backend: Flask
- DB (local dev): SQLite via Flask-SQLAlchemy
- DB (deployed, later): Azure Database for PostgreSQL Flexible Server
- Frontend: Flask/Jinja2 templates with a small hand-written stylesheet
- Tests: pytest
- Infra (later): Terraform, targeting Azure (App Service + PostgreSQL)

## Local setup

```
python3 -m venv venv          # on Windows: python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Run the tests with `pytest`.

The local database is created on first run at `instance/practice.db`. That
file is git-ignored, so each machine starts with its own empty database.

## Files

- `app.py` — Flask app setup and routes: dashboard, add, retest, edit, delete.
- `models.py` — the `Problem` database model.
- `logic.py` — `is_retest_due()`, a pure function kept separate from Flask
  and the database so it can be tested on its own.
- `templates/` — `base.html` (shared layout), `dashboard.html`, `add.html`,
  `edit.html`.
- `static/style.css` — styling.
- `tests/test_logic.py` — pytest cases for `is_retest_due()`, including
  completed retests and growing intervals.

## How it works

_To be written in your own words as each piece lands. The prompts below are
questions to answer, not the answers._

- What happens, step by step, from typing the site's address into the browser
  to seeing the dashboard? Which file handles each step?
- What happens when you submit the "Log a Solved Problem" form? Where does the
  data go, and what does the browser see afterwards?
- Where is "is this problem due for a retest?" decided, and how does that
  answer reach the page? Is it decided in more than one place?
- Why is `is_retest_due()` in its own file instead of inside `app.py`?
- What has to change, and in which files, if you add a new field to a problem?
