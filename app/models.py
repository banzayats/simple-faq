from app import db
from flask.ext.login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(255))
    questions = db.relationship('Question', backref='owner', lazy='dynamic')

    def __repr__(self):
        return self.name


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answers = db.relationship('Answer', backref='owner', lazy='dynamic')

    def __repr__(self):
        return self.text


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    date = db.Column(db.DateTime)
    votes = db.Column(db.Integer, default=0)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))