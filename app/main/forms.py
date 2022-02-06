import email
from turtle import title
from click import password_option
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, ValidationError
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User, Subscribe

class LoginForm(FlaskForm):

    username = StringField("Username:", validators=[Required()])
    password = PasswordField("Password:", validators=[Required()])
    submit = SubmitField("login")

class EditPostForm(FlaskForm):

    title = StringField("", validators=[Required()])
    content = TextAreaField("", validators=[Required()])
    submit = SubmitField("post")

class SignUpForm(FlaskForm):

    name = StringField("Name:", validators=[Required()])
    username = StringField("Username:", validators=[Required()])
    email = StringField("Email:", validators=[Required(),Email()])
    password = PasswordField('Password', validators = [Required(),EqualTo('password_confirm',message = 'Passwords do not match')])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField("signUp")

def validate_email(self, data_field):
    if User.query.filter_by(email = data_field.data).first():
        raise ValidationError("Email account already Taken")

def validate_username(self, data_field):
    if User.query.filter_by(username = data_field.data).first():
        raise ValidationError("Username already exists")

class SubscribeForm(FlaskForm):

    email = StringField("Email:", validators=[Required(), Email()])
    submit = SubmitField("subscribe")

    def validate_email(self, data_field):
        if Subscribe.query.filter_by(email = data_field.data).first():
            raise ValidationError("Email already Subscribed")