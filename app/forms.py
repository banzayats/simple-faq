from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo, Email
from flask.ext.babel import gettext

class LoginForm(Form):
    email = TextField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])


class RegisterForm(Form):
    name = TextField('Name', [Required()])
    email = TextField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Repeat Password', [
        Required(),
        EqualTo('password', message=gettext('Passwords must match'))
        ])


class QuestionForm(Form):
    text = TextField('Question', [Required()])


class AnswerForm(Form):
    text = TextField('Answer', [Required()])
