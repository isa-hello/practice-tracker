"""
Database model(s), via Flask-SQLAlchemy.

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
    retest_interval_days = db.Column(db.Integer, nullable=False, default=3)
    repeat_retests = db.Column(db.Boolean, nullable=False, default=False)