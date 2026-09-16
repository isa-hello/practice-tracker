"""
Flask app entry point.

Routes to implement (v1 scope only — see README):

GET  /                a dashboard: list all logged problems, and separately
                       highlight which ones are currently due for a cold
                       retest (use logic.is_retest_due against each row)

GET  /add              render a form to log a new solved problem
POST /add               handle that form submission, save a new Problem row,
                       redirect back to the dashboard

POST /problems/<id>/retest   mark that problem's retest as completed
                       (set retest_completed_at to now), redirect back to
                       the dashboard

TODO: implement app setup (Flask app, db init, config) and the routes above.
"""
from flask import Flask
from models import db, Problem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///practice.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Hello!"

if __name__ == '__main__':
    app.run(debug=True)