from flask import render_template
from app import app
from models import Question

@app.route('/')
@app.route('/index')
def index():
    questions = Question.query.all()
    return render_template("index.html", title='Home', questions=questions)