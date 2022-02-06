from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, ValidationError
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User, Subscribe

class LoginForm(FlaskForm):

    username = StringField("Username:", validators=[Required()])
    password = PasswordField("Password:", validators=[Required()])
    submit = SubmitField("login")