"""
Database model(s), via Flask-SQLAlchemy.

Sketch of what a Problem entry probably needs to hold — decide the actual
field types, nullability, and any defaults yourself:

- id
- title                (e.g. "Trapping Rain Water")
- pattern              (e.g. "Two Pointers")
- difficulty           (Easy / Medium / Hard)
- date_solved
- needed_help          (bool)
- notes                (free text — optional)
- retest_completed_at  (nullable — set once a due retest has been redone)

TODO: define `db = SQLAlchemy()` and the `Problem` model.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    pattern = db.Column(db.String(200), nullable=False)
    difficulty = db.Column(db.String(200), nullable=False)
    date_solved = db.Column(db.Date, nullable=False)
    needed_help = db.Column(db.Boolean, nullable=False)
    notes = db.Column(db.Text)
    retest_completed_at = db.Column(db.Date)