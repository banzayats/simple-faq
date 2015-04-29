from flask import render_template, request, flash, session, redirect, url_for
from flask.ext.login import login_user, logout_user
from werkzeug import check_password_hash, generate_password_hash
from app import app
from app import db
from app import login_manager
from forms import LoginForm, RegisterForm
from models import User, Question


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
    questions = Question.query.all()
    return render_template("index.html", questions=questions)


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