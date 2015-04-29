from flask import render_template, request, flash, session, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from werkzeug import check_password_hash, generate_password_hash
from app import app
from app import db
from app import login_manager
from forms import LoginForm, RegisterForm, QuestionForm, AnswerForm
from models import User, Question, Answer
from datetime import datetime


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'))


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/questions')
def questions():
    questions = Question.query.all()
    return render_template("questions.html", questions=questions)

@app.route('/questions/<id>', methods = ['GET', 'POST'])
def details(id):
    question = Question.query.filter_by(id=id).first()
    if question == None:
        flash('Question with ID ' + id + ' not found.', 'warning')
        return redirect(url_for('questions'))
    answers = Answer.query.filter_by(question_id=id).all()
    vote = request.args.get('vote')
    if vote != None:
        answer = Answer.query.filter_by(id=vote).first()
        answer.votes += 1
        db.session.commit()
    form = AnswerForm(request.form)
    if form.validate_on_submit():
        answer = Answer(text=form.text.data,
                        date=datetime.utcnow(),
                        owner=question)
        db.session.add(answer)
        db.session.commit()
        flash('Your answer succesfully posted', 'success')
        return redirect(url_for('questions'))
    return render_template("question.html", question=question, form=form, answers=answers)


@app.route('/add', methods = ['GET', 'POST'])
@login_required
def add():
    form = QuestionForm(request.form)
    if form.validate_on_submit():
        question = Question(text=form.text.data,
                            date=datetime.utcnow(),
                            owner=current_user)
        db.session.add(question)
        db.session.commit()
        flash('Your question succesfully posted', 'success')
        return redirect(url_for('questions'))
    return render_template('add_question.html',
        form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Welcome %s' % user.name, 'success')
            return redirect(url_for('index'))
        else:
            flash('Wrong email or password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html',
        form = form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        exist = User.query.filter_by(email=form.email.data).first()
        if exist:
            flash('User with such email already exists', 'danger')
            return redirect(url_for('register'))
        user = User(name=form.name.data, email=form.email.data, \
            password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Thanks for registering', 'success')
        return redirect(url_for('index'))
    return render_template("register.html",
        form=form)