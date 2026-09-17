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
from flask import Flask, render_template, request, redirect, url_for
from models import db, Problem
from datetime import date
import logic

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///practice.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def dashboard():
    # TODO: implement
    #
    # - query all Problem rows (Problem.query.all() or similar)
    # - separately figure out which ones are currently due for a cold
    #   retest — call logic.is_retest_due(row.date_solved, row.needed_help)
    #   for each row, using today's date
    # - pass both the full list and the "due" info to the template so the
    #   dashboard can highlight which ones need a retest

    problems = Problem.query.all()
    due_ids = []
    for problem in problems:
        if logic.is_retest_due(problem.date_solved, problem.needed_help, problem.retest_completed_at, date.today()) is True:
            due_ids.append(problem.id)

    return render_template('dashboard.html', problems=problems, due_ids=due_ids)


@app.route('/add', methods=['GET', 'POST'])
def add():
    # - GET: just render the form
    # - POST: read the submitted fields from request.form, build a new
    #   Problem row from them, add it to the db session, commit, then
    #   redirect back to the dashboard (url_for('dashboard'))

    if request.method == 'POST':
        title = request.form['title']
        pattern = request.form['pattern']
        difficulty = request.form['difficulty']
        date_solved = date.fromisoformat(request.form['date_solved'])
        needed_help = request.form.get('needed_help') == 'on'
        notes = request.form['notes']

        problem = Problem(title=title, pattern=pattern, difficulty=difficulty, date_solved=date_solved, needed_help=needed_help, notes=notes)
        db.session.add(problem)
        db.session.commit()
    return render_template('add.html')


@app.route('/problems/<int:problem_id>/retest', methods=['POST'])
def retest(problem_id):
    # - look up the Problem by id (Problem.query.get_or_404(problem_id) or
    #   similar)
    # - set its retest_completed_at to today's date
    # - commit the change, then redirect back to the dashboard
    problem = Problem.query.get_or_404(problem_id)
    problem.retest_completed_at = date.today()
    db.session.commit()
    
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
