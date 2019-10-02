from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email


class Login(FlaskForm):
    user_name = StringField('User Name')
    password = PasswordField('Password')
    signup = SubmitField('Register')
    login = SubmitField('Login')


class Register(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
